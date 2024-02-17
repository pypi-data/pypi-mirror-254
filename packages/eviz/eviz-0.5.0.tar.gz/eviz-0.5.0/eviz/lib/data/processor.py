from dataclasses import dataclass, field
from typing import Any, Tuple
import logging
import numpy as np
from scipy.interpolate import interp1d
import xarray as xr

from eviz.lib.eviz.config import Config


@dataclass
class Processor:
    config: Config
    data: list = field(default_factory=list)

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    def __post_init__(self):
        self.data = []
        self.tropp = None
        self.tropp_conversion = None
        self.trop_ok = False

    def process_data(self) -> None:
        logging.getLogger(__name__).info("Processing data")
        processed_data = []

        for reader, input_data in zip(self.config.readers, self.config.app_data['inputs']):
            to_plot = input_data['to_plot']
            for k, v in to_plot.items():
                field_name = k
                plot_type = v
            data = reader.read_data()

            if plot_type == 'xy':
                processed_data.append((field_name, self.process_xy(data, field_name)))
            elif plot_type == 'yz':
                processed_data.append((field_name, self.process_yz(data, field_name)))
            elif plot_type == 'scat':
                pass
            #     processed_data.append((field_name, self.process_scat(data, field_name)))
            else:
                print(f"Unsupported plot type: {plot_type}")
        if plot_type == 'scat':
            self.data = data
        else:
            self.data = processed_data

        if not plot_type == 'scat':

            # Process field_name comparisons
            if self.config.compare:
                for field_name in self.config.compare_fields:
                    data = self.get_processed_data(field_name)
                    if data is not None:
                        processed_data.append((field_name, self.process_difference(data, data)))

            self.data.extend(processed_data)

    def trop_field(self, ds_meta, findex=0):
        """ Get tropopause field and apply to a given experiment _name

        Parameters:
            ds_meta (dict) : Dateset metadata
            findex (int) : Dataset index (default=0, i.e. just one dataset)
       """
        if self.config.use_trop_height:
            if findex not in ds_meta['trop_height_meta']:
                return
            if ds_meta['trop_height_meta'][findex]['exp_name'] == ds_meta['exp_name']:
                try:
                    trop_filename = ds_meta['trop_height_meta'][findex]['filename']
                    self.logger.debug(f"Processing {trop_filename}...")

                    with xr.open_dataset(trop_filename) as f:
                        trop_field = ds_meta['trop_height_meta'][findex]['trop_field_name']
                        tropp = f.data_vars.get(trop_field)
                        # TODO: remove assumption that 'time=0' is used
                        self.tropp = tropp.isel(time=0)

                        units = get_dst_attribute(tropp, 'units')
                        if units == 'Pa':
                            self.tropp_conversion = 1 / 100.0
                        elif units == 'hPa':
                            self.tropp_conversion = 1.0
                        else:
                            self.tropp_conversion = 1.0
                    self.trop_ok = True

                except FileNotFoundError:
                    self.logger.warning(self.config.get_trop_field_filename()+' not found')
                    self.tropp = None
            else:
                self.trop_ok = False
                self.tropp = None

    def sphum_field(self, ds_meta, findex=0):
        """ Get specific humidity field and apply to a given experiment _name

        Parameters:
            ds_meta (dict) : Dateset metadata
            findex (int) : Dataset index (default=0, i.e. just one dataset)
        """
        if not self.config.use_sphum_conv:
            return
        radionuclides = ['Be10', 'Be10s', 'Be7', 'Be7s', 'Pb210', 'Rn222']

        to_convert = set(self.config.to_plot).intersection(set(radionuclides))
        if to_convert:
            if ds_meta['sphum_conv_meta'][findex]['exp_name'] == ds_meta['exp_name']:
                try:
                    sphum_filename = ds_meta['sphum_conv_meta'][findex]['filename']
                    self.logger.debug(f"Processing {sphum_filename}...")

                    with xr.open_dataset(sphum_filename) as f:
                        sphum_field = ds_meta['sphum_conv_meta'][findex]['sphum_field_name']
                        specific_hum = f.data_vars.get(sphum_field)
                        # Assume 'time=0' is used
                        self.specific_hum = specific_hum.isel(time=0)

                except FileNotFoundError:
                    self.logger.warning(
                        self.config.get_sphum_filename()+" file could not be opened. Setting QV=0.0")
                    self.specific_hum = 0.0  # assume dry air conditions
                else:
                    for name in to_convert:
                        self._convert_radionuclide_units(name, 'mol mol-1')
            else:
                self.logger.warning(
                    "QV file was not specified. Setting QV=0.0")
                self.specific_hum = 0.0  # assume dry air conditions

    def _convert_radionuclide_units(self, species_name, target_units):
        """ CCM-specific conversion function for radionuclides """
        ds_index = self.config.data_source.get_ds_index()
        if not self.config.use_sphum_field:
            return
        if self.config.data_source.data_unit_is_mol_per_mol(self.config.data_source.datasets[ds_index]['vars'][species_name]):
            return
        self.logger.debug(f"Converting {species_name} units to {target_units}")

        # Get species molecular weight information
        if "MW_g" in self.config.db_data[species_name].keys():
            mw_g = self.config.db_data[species_name].get("MW_g")
        else:
            msg = "Cannot find molecular weight MW_g for species {}".format(
                species_name)
            msg += "!\nPlease add the MW_g field for {}".format(species_name)
            msg += " to the species_database.yaml file."
            raise ValueError(msg)

        mw_air = constants.MW_AIR_g  # g/mole

        rn_arr = self.config.data_source.datasets[ds_index]['vars'][species_name]

        # TODO: regrid if different resolutions
        data = (rn_arr / (1. - self.specific_hum)) * (mw_air / mw_g)

        rn_new = xr.DataArray(
            data, name=rn_arr.name, coords=rn_arr.coords, dims=rn_arr.dims, attrs=rn_arr.attrs
        )
        rn_new.attrs["units"] = target_units

        self.config.data_source.datasets[ds_index]['ptr'][rn_arr.name] = rn_new

    def get_processed_data(self, field: str) -> Any | None:
        for processed_field, data_array in self.data:
            if processed_field == field:
                return data_array
        return None

    @staticmethod
    def process_difference(data1: np.ndarray, data2: np.ndarray) -> np.ndarray:
        return data1 - data2

    @staticmethod
    def process_xy(data: Any, field: str) -> np.ndarray:
        data_variable = data[field]
        data_array = data_variable.values

        if data_array.ndim == 3:
            data_array = data_array[0]

        return data_array

    @staticmethod
    def process_yz(data: Any, field: str) -> np.ndarray:
        data_variable = data[field]
        data_array = data_variable.values

        if data_array.ndim == 3:
            data_array = data_array[0]

        data_array = np.mean(data_array, axis=0)

        return data_array

    @staticmethod
    def process_scat(data: Any, field: str) -> np.ndarray:
        data_variable = data[field]
        data_array = data_variable.values

        return data_array

    def get_field(self, name, ds_index=0):
        """ Extract field from xarray Dataset

        Parameters:
            name (str) : name of field to extract from dataset
            ds_index (int) : fid index associated with dataset containing field name

        Returns:
            DataArray containing field data
        """
        try:
            self.logger.debug(f" -> getting field {name}")
            return self.config.readers[ds_index].datasets[ds_index]['vars'][name]
        except Exception as e:
            self.logger.error('key error: %s, not found' % str(e))
        return None

    def get_meta_attrs(self, data, key):
        """ Get attributes associated with a key"""
        if self.config.source_names[key] in self.config.meta_attrs[key]:
            return self.config.meta_attrs[key][self.config.source_names[key]]
        return None

    @staticmethod
    def get_attrs(data, key):
        """ Get attributes associated with a key"""
        for attr in data.attrs:
            if key == attr:
                return data.attrs[key]
            else:
                continue
        return None


@dataclass
class Interp:
    config: Config
    data: Tuple[Any]

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    def regrid(self, field_names, ax, level, pid):
        """ Wrapper for regrid method

        This function takes in two fields and, if necessary, regrids them to a common resolution.

        Parameters:
            field_names (tuple) : Names of fields
            ax (Axes) : Axes object
            level (int) : index of vertical level to interpolate (level=0 for 2D fields)
            pid (str) : a plot identifier

        Returns:
            Regridded fields
        """
        # TODO: get rid of ax/ax_opts dependency
        return self._regrid_check(field_names, ax, level, pid)

    # Interpolation (AKA regrid) methods
    def _regrid_check(self, field_names, ax, level, pid):
        """ Main regrid method """
        ax_opts = self.config.ax_opts
        name1, name2 = field_names
        xc = self.config.get_model_dim_name('xc')
        yc = self.config.get_model_dim_name('yc')
        zc = self.config.get_model_dim_name('zc')
        dim1, dim2 = xc, yc
        if 'yz' in pid:
            dim1, dim2 = yc, zc
        d1 = self.data[0]  # self.config.readers[0].get_field(name1, ds_index=0)
        d2 = self.data[1]  # self.config.readers[0].get_field(name2, ds_index=1)
        if 'yz' in pid:
            d1 = eval(f"d1['ptr'][name1].isel({self.config.get_model_dim_name('tc')}=ax_opts['time_lev']).mean(dim=xc)")
            d2 = eval(f"d2['ptr'][name2].isel({self.config.get_model_dim_name('tc')}=ax_opts['time_lev']).mean(dim=xc)")
            d1 = self._select_yrange(d1, name1)
            d2 = self._select_yrange(d2, name2)
        elif 'xy' in pid:
            if zc in d1['dims'] and len(d1['ptr'][name1].coords[zc]) == 1:
                d1 = d1['ptr'][name1].squeeze()
            if zc in d2['dims'] and len(d2['ptr'][name1].coords[zc]) == 1:
                d2 = d2['ptr'][name2].squeeze()

            if zc not in d1['ptr'][name1].coords:
                d1 = eval(f"d1['ptr'][name1].isel({self.config.get_model_dim_name('tc')}=ax_opts['time_lev'])")
            else:
                lev_to_plot = np.where(d1['ptr'][name1].coords[zc].values == level)[0]
                d1 = eval(f"d1['ptr'][name1].isel({self.config.get_model_dim_name('tc')}=ax_opts['time_lev'], lev=lev_to_plot)")

            if zc not in d2['ptr'][name2].coords:
                d2 = eval(f"d2['ptr'][name2].isel({self.config.get_model_dim_name('tc')}=ax_opts['time_lev'])")
            else:
                lev_to_plot = np.where(d2['ptr'][name2].coords[zc].values == level)[0]
                d2 = eval(f"d2['ptr'][name2].isel({self.config.get_model_dim_name('tc')}=ax_opts['time_lev'], lev=lev_to_plot)")

        d1 = self._apply_conversion(d1, name1)
        d2 = self._apply_conversion(d2, name2)

        da1_size = d1.size
        da2_size = d2.size
        if da1_size < da2_size:
            d2 = self._regrid(d2, d1, dim1, dim2, regrid_dims=(1, 0))
            d2 = self._regrid(d2, d1, dim1, dim2, regrid_dims=(0, 1))
        elif da1_size > da2_size:
            d1 = self._regrid(d1, d2, dim1, dim2, regrid_dims=(1, 0))
            d1 = self._regrid(d1, d2, dim1, dim2, regrid_dims=(0, 1))
        elif da1_size == da2_size:
            d1 = self._regrid(d1, d2, dim1, dim2, regrid_dims=(1, 0))
            d1 = self._regrid(d1, d2, dim1, dim2, regrid_dims=(0, 1))
            d2 = self._regrid(d2, d1, dim1, dim2, regrid_dims=(1, 0))
            d2 = self._regrid(d2, d1, dim1, dim2, regrid_dims=(0, 1))

        if self.config.ax_opts['add_extra_field_type']:
            data_diff = self._compute_diff_type(d1, d2).squeeze()
        else:
            data_diff = (d1 - d2).squeeze()
        coords = data_diff.coords
        return data_diff, coords[dim1].values, coords[dim2].values

    def _apply_conversion(self, data2d, name):
        """ Apply conversion factor to data

        The conversion factor is specified in the ``specs`` file.

        Parameters:
            data2d (ndarray) : A 2D array of an ESM field
            name (str) : field name
        Returns:
            Pre-processed data array
        """
        if 'unitconversion' in self.config.spec_data[name]:
            if "AOA" in name.upper():
                data2d = data2d / np.timedelta64(1, 'ns') / 1000000000 / 86400
            else:
                data2d = data2d * float(self.config.spec_data[name]['unitconversion'])
        return data2d

    def _select_yrange(self, data2d, name):
        """ For 3D fields, select vertical level range to use

        Parameters:
            data2d (ndarray) : A 2D array of an ESM field
            name (str) : field name

        Returns:
            sliced data array
        """
        if 'zrange' in self.config.spec_data[name]['yzplot']:
            if self.config.spec_data[name]['yzplot']['zrange']:
                lo_z = self.config.spec_data[name]['yzplot']['zrange'][0]
                hi_z = self.config.spec_data[name]['yzplot']['zrange'][1]
                if hi_z >= lo_z:
                    self.logger.error(f"Upper level value ({hi_z}) must be less than low level value ({lo_z})")
                    return
                lev = self.config.get_model_dim_name('zc')
                min_index, max_index = 0, len(data2d.coords[lev].values) - 1
                for k, v in enumerate(data2d.coords[lev]):
                    if data2d.coords[lev].values[k] == lo_z:
                        min_index = k
                for k, v in enumerate(data2d.coords[lev]):
                    if data2d.coords[lev].values[k] == hi_z:
                        max_index = k
                return data2d[min_index:max_index + 1, :]
            else:
                return data2d
        else:
            return data2d

    def _compute_diff_type(self, d1, d2):
        """ Compute difference between two fields based on specified type

        Difference is specified in ``app`` file. It can be a percent difference, a percent change
        or a ratio difference.

        Parameters:
            d1 (ndarray) : A 2D array of an ESM field
            d2 (ndarray) : A 2D array of an ESM field

        Returns:
            Difference of the two fields
        """
        field_diff = None
        if self.config.extra_diff_plot == "percd":  # percent diff
            num = abs(d1 - d2)
            den = (d1 + d2) / 2.0
            field_diff = (num / den) * 100.
        elif self.config.extra_diff_plot == "percc":  # percent change
            field_diff = d1 - d2
            field_diff = field_diff / d2
            field_diff = field_diff * 100
        elif self.config.extra_diff_plot == "ratio":
            field_diff = d1 / d2

        return field_diff

    @staticmethod
    def _interp(y_src, x_src, x_dest, **kwargs):
        """ Wrapper for SciPy's interp1d """
        return interp1d(x_src, y_src, **kwargs)(x_dest)

    def _regrid(self, ref_arr, in_arr, dim1_name, dim2_name, regrid_dims=(0, 0)):
        """ Main regrid function used in eviz

        The regridding uses SciPy's interp1d function and interpolates
        a 2D field one row at a time.

        Parameters:
           ref_arr (ndarray) : the reference array
            in_arr (ndarray) : the input array
            dim1_name (str) : name of the input dimension
            dim2_name (str) : name of the output dimension
        """
        new_arr = ref_arr

        if regrid_dims[0]:
            new_arr = xr.apply_ufunc(self._interp, new_arr,
                                     input_core_dims=[[dim2_name]],
                                     output_core_dims=[[dim2_name]],
                                     exclude_dims={dim2_name},
                                     kwargs={'x_src': ref_arr[dim2_name],
                                             'x_dest': in_arr.coords[dim2_name].values,
                                             'fill_value': "extrapolate"},
                                     dask='allowed', vectorize=True)
            new_arr.coords[dim2_name] = in_arr.coords[dim2_name]
        elif regrid_dims[1]:
            new_arr = xr.apply_ufunc(self._interp, new_arr,
                                     input_core_dims=[[dim1_name]],
                                     output_core_dims=[[dim1_name]],
                                     exclude_dims={dim1_name},
                                     kwargs={'x_src': ref_arr[dim1_name],
                                             'x_dest': in_arr.coords[dim1_name].values,
                                             'fill_value': "extrapolate",},
                                     dask='allowed', vectorize=True)
            new_arr.coords[dim1_name] = in_arr.coords[dim1_name]

        return new_arr
