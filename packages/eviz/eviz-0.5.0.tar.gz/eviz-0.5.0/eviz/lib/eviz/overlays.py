import logging
import xarray as xr
import eviz.lib.const as constants
from eviz.lib.xarray_utils import get_dst_attribute


class Overlays:
    """ Class that define overlays

    Example of overlays include:
        - specialized contours
        - specialized line plots

    Parameters:
        figure (Frame) : Frame object to contain plot(s)
        config (Config) : Config object
    """
    logger = logging.getLogger(__name__)
    _sphum = None

    def __init__(self, figure, config):
        self.logger.info("Start init")
        self.figure = figure
        self.config = config
        self.tropp = None
        self.tropp_conversion = None
        self.trop_ok = False

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

    def space_average(self):
        pass

    def time_average(self):
        pass

