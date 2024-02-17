import logging
import os
from abc import ABC, abstractmethod
from glob import glob

import pandas as pd
import xarray as xr
import numpy as np
import eviz.lib.const as constants
import eviz.lib.utils as u
from dataclasses import dataclass
from typing import Any

FILE_EXTENSIONS = (
    'nc',
    'nc4',
    'hdf',
    'hdf4',
    'h5',
    'hdf5',
    'csv',
    'dat',
    'grib',
    'grib2',
)


@dataclass
class DataSource(ABC):
    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    @abstractmethod
    def load_data(self, file_path):
        raise NotImplementedError("Subclasses must implement load_data method.")


@dataclass
class CSVDataSource(DataSource):

    def load_data(self, file_path: str):
        self.logger.debug(f"Loading CSV data from {file_path}")
        files = glob(file_path)
        alldata = pd.DataFrame()
        if "*" in file_path:
            for f in files:
                this_data = pd.read_csv(f)
                alldata = pd.concat([alldata, this_data], ignore_index=True)
        else:
            this_data = pd.read_csv(file_path)
            alldata = pd.concat([alldata, this_data], ignore_index=True)

        processed_data = self._process_data(alldata)
        return processed_data

    def _process_data(self, data):
        self.logger.debug(f"Preparing CSV data")
        return data


@dataclass
class HDF4DataSource(DataSource):
    def load_data(self, file_path: str):
        self.logger.debug(f"Loading HDF4 data from {file_path}")
        # Custom logic to load HDF4 data

    def _process_data(self, data):
        self.logger.debug(f"Preparing HDF4 data")
        return data


@dataclass
class HDF5DataSource(DataSource):
    def load_data(self, file_path: str):
        self.logger.debug(f"Loading HDF5 data from {file_path}")
        # Custom logic to load HDF5 data

    def _process_data(self, data):
        self.logger.debug(f"Preparing HDF5 data")
        return data


@dataclass
class NetCDFDataSource(DataSource):
    fid: int = 0

    def load_data(self, file_name: str):

        """ Helper function to open and define a dataset

        Parameters:
            fid (int) : file id (starts at 0)
            file_name (str) : name of file associated with fid

        Returns:
            unzipped_data (xarray.Dataset) : dict with xarray dataset information
        """
        self.logger.debug(f"Loading NetCDF data from {file_name} , fid: {NetCDFDataSource.fid}")
        unzipped_data = {}
        if "*" in file_name:
            with xr.open_mfdataset(file_name, decode_cf=True) as f:
                unzipped_data['id'] = NetCDFDataSource.fid
                unzipped_data['ptr'] = f
                unzipped_data['regrid'] = False
                unzipped_data['vars'] = f.data_vars
                unzipped_data['attrs'] = f.attrs
                unzipped_data['dims'] = f.dims
                unzipped_data['coords'] = f.coords
                unzipped_data['filename'] = "".join(file_name)
                unzipped_data['season'] = get_season_from_file(file_name)
        else:
            with xr.open_dataset(file_name, decode_cf=True) as f:
                unzipped_data['id'] = NetCDFDataSource.fid
                unzipped_data['ptr'] = f
                unzipped_data['regrid'] = False
                unzipped_data['vars'] = f.data_vars
                unzipped_data['attrs'] = f.attrs
                unzipped_data['dims'] = f.dims
                unzipped_data['coords'] = f.coords
                unzipped_data['filename'] = "".join(file_name)
                unzipped_data['season'] = get_season_from_file(file_name)
        NetCDFDataSource.fid += 1
        processed_data = self._process_data(unzipped_data)
        return processed_data

    def _process_data(self, data):
        self.logger.debug(f"Preparing NetCDF data")
        return data


class DataSourceFactory:

    @staticmethod
    def get_data_class(file_extension: str) -> DataSource:
        if file_extension == "csv" or file_extension == "dat":
            return CSVDataSource()
        elif file_extension == "hdf4":
            return HDF4DataSource()
        elif file_extension == "hdf5":
            return HDF5DataSource()
        elif file_extension == "nc" or file_extension == "nc4":
            return NetCDFDataSource()
        else:
            raise ValueError(f"No data source specified for file extension: {file_extension}")


@dataclass
class DataProcessor(DataSource):
    """ This class provides methods to access and process EVIZ data sources.

    An instance of DataProcessor is created for each model and its associated file list.
    To maintain model agnosticism, the names for the model's coordinates are represented
    by generic names as xc, yc, zc, and tc. These names are mapped to the actual model
    coordinate names in the YAML file meta_coordinates.yaml. Likewise, the data attributes
    are stored and mapped in a dictionary defined in meta_attributes.yaml.

    Parameters:
        model_name (str) : The name of the `supported` model.
        file_list (list) : The list of data file names.
        meta_coords (dict) : A dictionary of metadata coordinate names from the file list.
        meta_attrs (dict) : A dictionary of metadata attribute names from the file list.

    """
    model_name: str
    file_list: dict
    meta_coords: dict
    meta_attrs: dict
    season: Any = None

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    def __post_init__(self):
        self.logger.info("Start init")
        self.datasets = []

    def load_data(self, file_path):
        pass

    def process_data(self):
        factory = DataSourceFactory()
        for fid, filename in self.file_list.items():
            file_path = filename['name']
            if 'location' in filename:
                file_path = os.path.join(filename['location'], filename['name'])
            file_extension = file_path.split(".")[-1]
            if file_extension not in FILE_EXTENSIONS:
                self.logger.error(f"File extension '{file_extension}' not found. Will assume NetCDF4.")
                file_extension = 'nc4'
            data_class = factory.get_data_class(file_extension)
            self.datasets.append(data_class.load_data(file_path))

        self.logger.info(f"Processing data for model: {self.model_name}")

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
            return self.datasets[ds_index]['vars'][name]
        except Exception as e:
            self.logger.error('key error: %s, not found' % str(e))
        return None

    def get_meta_attrs(self, data, key):
        """ Get attributes associated with a key"""
        if self.model_name in self.meta_attrs[key]:
            return self.meta_attrs[key][self.model_name]
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

    @staticmethod
    def adjust_units(units):

        # Error check arguments
        if not isinstance(units, str):
            raise TypeError("Units must be of type str!")

        # Strip all spaces in the unit string
        units_squeezed = units.replace(" ", "")

        if units_squeezed in ["kg/m2/s", "kgm-2s-1", "kgm^-2s^-1"]:
            unit_desc = "kg/m2/s"

        elif units_squeezed in [
            "kgC/m2/s",
            "kgCm-2s-1",
            "kgCm^-2s^-1",
            "kgc/m2/s",
            "kgcm-2s-1",
            "kgcm^-2s^-1",
        ]:
            unit_desc = "kgC/m2/s"

        elif units_squeezed in ["molec/cm2/s", "moleccm-2s-1", "moleccm^-2s^-1"]:
            unit_desc = "molec/cm2/s"

        else:
            unit_desc = units_squeezed

        return unit_desc

    @staticmethod
    def convert_kg_to_target_units(data_kg, target_units, kg_to_kgC):

        # Convert to target unit
        if target_units == "Tg":
            data = data_kg * 1e-9

        elif target_units == "Tg C":
            data = data_kg * kg_to_kgC * 1.0e-9

        elif target_units == "Gg":
            data = data_kg * 1e-6

        elif target_units == "Gg C":
            data = data_kg * kg_to_kgC * 1.0e-6

        elif target_units == "Mg":
            data = data_kg * 1e-3

        elif target_units == "Mg C":
            data = data_kg * kg_to_kgC * 1.0e-3

        elif target_units == "kg":
            data = data_kg

        elif target_units == "kg C":
            data = data_kg * kg_to_kgC

        elif target_units == "g":
            data = data_kg * 1e3

        elif target_units == "g C":
            data = data_kg * kg_to_kgC * 1.0e3

        else:
            msg = "Target units {} are not yet supported!".format(target_units)
            raise ValueError(msg)

        # Return converted data
        return data

    @staticmethod
    def convert_units(
            dr,
            species_name,
            species_properties,
            target_units,
            interval=2678400.0,
            area_m2=None,
            delta_p=None,
            box_height=None):

        # Get species molecular weight information
        if "MW_g" in species_properties.keys():
            mw_g = species_properties.get("MW_g")
        else:
            msg = "Cannot find molecular weight MW_g for species {}".format(
                species_name)
            msg += "!\nPlease add the MW_g field for {}".format(species_name)
            msg += " to the species_database.yml file."
            raise ValueError(msg)

        # If the species metadata does not contain EmMW_g, use MW_g instead
        if "EmMW_g" in species_properties.keys():
            emitted_mw_g = species_properties.get("EmMW_g")
        else:
            emitted_mw_g = mw_g

        # If the species metadata does not containe MolecRatio, use 1.0 instead
        if "MolecRatio" in species_properties.keys():
            moles_C_per_mole_species = species_properties.get("MolecRatio")
        else:
            moles_C_per_mole_species = 1.0

        # ==============================
        # Compute conversion factors
        # ==============================

        # Physical constants
        avo = constants.AVOGADRO  # molecules/mole
        mw_air = constants.MW_AIR_g  # g/mole
        g0 = constants.G  # m/s2

        # Get a consistent value for the units string
        # (ignoring minor differences in formatting)
        units = DataSource.adjust_units(dr.units)

        # Error checks
        if units == "molmol-1dry" and area_m2 is None:
            raise ValueError(
                "Conversion from {} to {} for {} requires area_m2 as input".format(
                    units, target_units, species_name
                )
            )
        if units == "molmol-1dry" and delta_p is None:
            raise ValueError(
                "Conversion from {} to {} for {} requires delta_p as input".format(
                    units, target_units, species_name
                )
            )
        if "g" in target_units and mw_g is None:
            raise ValueError(
                "Conversion from {} to {} for {} requires MW_g definition in species_database.yml".format(
                    units, target_units, species_name))

        # Conversion factor for kg species to kg C
        kg_to_kgC = (emitted_mw_g * moles_C_per_mole_species) / mw_g

        # Mass of dry air in kg (required when converting from v/v)
        if 'molmol-1' in units:
            air_mass = delta_p * 100.0 / g0 * area_m2

            # Conversion factor for v/v to kg
            # v/v * kg dry air / g/mol dry air * g/mol species = kg species
            if "g" in target_units:
                vv_to_kg = air_mass / mw_air * mw_g

            # Conversion factor for v/v to molec/cm3
            # v/v * kg dry air * mol/g dry air * molec/mol dry air /
            #  (area_m2 * box_height ) * 1m3/10^6cm3 = molec/cm3
            if "molec" in target_units:
                vv_to_MND = air_mass / mw_air * avo / (area_m2 * box_height) / 1e6

        # ================================================
        # Get number of seconds per time in dataset
        # ================================================

        # Number of seconds is passed via the interval argument
        numsec = interval

        # Special handling is required if multiple times in interval (for
        # broadcast)
        if len([interval]) > 1:
            if 'time' in dr.dims:
                # Need to right pad the interval array with new axes up to the
                # time dim of the dataset to enable broadcasting
                numnewdims = len(dr.dims) - (dr.dims.index('time') + 1)
                for _ in range(numnewdims):
                    numsec = numsec[:, np.newaxis]
            else:
                # Raise an error if no time in dataset but interval has length > 1
                raise ValueError(
                    'Interval passed to convert_units has length greater than one but data array has no time dimension')

        # ==============================
        # Compute target units
        # ==============================

        if units == "kg/m2/s":
            data_kg = dr * area_m2
            data_kg = data_kg.values * numsec
            data = DataSource.convert_kg_to_target_units(data_kg, target_units, kg_to_kgC)

        elif units == "kgC/m2/s":
            data_kg = dr * area_m2 / kg_to_kgC
            data_kg = data_kg.values * numsec
            data = DataSource.convert_kg_to_target_units(data_kg, target_units, kg_to_kgC)

        elif units == "kg":
            data_kg = dr.values
            data = DataSource.convert_kg_to_target_units(data_kg, target_units, kg_to_kgC)

        elif units == "kgC":
            data_kg = dr.values / kg_to_kgC
            data = DataSource.convert_kg_to_target_units(data_kg, target_units, kg_to_kgC)

        #    elif units == 'molec/cm2/s':
        #        # Implement later

        #    elif units == 'atomsC/cm2/s':
        #         implement later

        elif 'molmol-1' in units:

            if "g" in target_units:
                data_kg = dr.values * vv_to_kg
                data = DataSource.convert_kg_to_target_units(data_kg, target_units, kg_to_kgC)

            elif "molec" in target_units:
                data = dr.values * vv_to_MND

        else:
            raise ValueError(
                "Units ({}) in variable {} are not supported".format(
                    units, species_name))

        # ==============================
        # Return result
        # ==============================

        # Create a new DataArray.  This will be exactly the same as the old
        # DataArray, except that the data will have been converted to the
        # target_units, and the units string will have been adjusted accordingly.
        dr_new = xr.DataArray(
            data, name=dr.name, coords=dr.coords, dims=dr.dims, attrs=dr.attrs
        )
        dr_new.attrs["units"] = target_units

        return dr_new

    @staticmethod
    def check_units(ref_da, dev_da, enforce_units=True):
        units_ref = ref_da.units.strip()
        units_dev = dev_da.units.strip()
        if units_ref != units_dev:
            units_match = False
            print("WARNING: ref and dev concentration units do not match!")
            print("Ref units: {}".format(units_ref))
            print("Dev units: {}".format(units_dev))
            if enforce_units:
                # if enforcing units, stop the program if
                # units do not match
                assert units_ref == units_dev, \
                    "Units do not match: ref {} and dev {}!".format(
                        units_ref, units_dev)
        else:
            units_match = True
        return units_match

    @staticmethod
    def data_unit_is_mol_per_mol(da):
        conc_units = ["mol mol-1 dry", "mol/mol", "mol mol-1"]
        is_molmol = False
        if da.units.strip() in conc_units:
            is_molmol = True
        return is_molmol

    def get_ds_index(self):
        return self.ds_index

    def get_datasets(self):
        return self.datasets

    def get_dataset(self, i):
        return self.datasets[i]


def get_season_from_file(file_name):
    if "ANN" in file_name:
        return "ANN"
    elif "JJA" in file_name:
        return "JJA"
    elif "DJF" in file_name:
        return "DJF"
    elif "SON" in file_name:
        return "SON"
    elif "MAM" in file_name:
        return "MAM"
    else:
        return None


def make_fake_timeseries_dataset(path=None):
    np.random.seed(123)
    times = pd.date_range("2000-01-01", "2001-12-31", name="time")
    annual_cycle = np.sin(2 * np.pi * (times.dayofyear.values / 365.25 - 0.28))

    base = 10 + 15 * annual_cycle.reshape(-1, 1)
    tmin_values = base + 3 * np.random.randn(annual_cycle.size, 3)
    tmax_values = base + 10 + 3 * np.random.randn(annual_cycle.size, 3)

    ds = xr.Dataset(
        {
            "tmin": (("time", "location"), tmin_values),
            "tmax": (("time", "location"), tmax_values),
        },
        {"time": times, "location": ["DC", "MD", "VA"]},
    )
    if path is None:
        path = os.path.join(constants.ROOT_FILEPATH, 'test/data')
    u.mkdir_p(path)
    ds.to_netcdf(os.path.join(path, 'timeseries.nc'), format='NETCDF4')
    return ds


def make_fake_4D_dataset(nt=366, path=None):
    nt = nt
    nx = 20
    ny = 15
    nz = 10

    temp = np.zeros((nt, nz, ny, nx))
    rh = np.zeros((nt, nz, ny, nx))
    ps = np.zeros((nt, ny, nx))

    times = pd.date_range("2000-01-01",
                          periods=nt,
                          freq=pd.DateOffset(days=1),
                          name="time")
    t0 = 273.
    q0 = 50.
    p0 = 1e5

    lon = np.zeros((ny, nx))
    lat = np.zeros((ny, nx))
    lev = np.linspace(nz, 1., 10) * 1e4
    for y in range(ny):
        for x in range(nx):
            lon[y, x] = 100 + y * 10 + x / 10
            lat[y, x] = 200 + x * 10 + y / 10

    for t in range(nt):
        tt = (nt - t) * p0 / 100
        for y in range(ny):
            for x in range(nx):
                ps[t, y, x] = np.random.normal(p0, 1000) + \
                              np.sin(x + tt * np.pi / 4) + \
                              np.cos(y + tt * np.pi / 6)
    for t in range(nt):
        tt = (nt - t) * 10
        for z in range(nz):
            zz = nz - z
            for y in range(ny):
                for x in range(nx):
                    temp[t, z, y, x] = np.random.normal(t0, 20) + \
                                       np.sin(x + tt * np.pi / 4) + \
                                       np.cos(y + tt * np.pi / 6) + \
                                       np.exp(zz / 10.)
                    rh[t, z, y, x] = np.random.normal(q0, 20) + \
                                     np.sin(x + tt * np.pi / 4) + \
                                     np.cos(y + tt * np.pi / 6) + \
                                     np.exp(zz / 20.)

    ds = xr.Dataset({
        'sfc_press': xr.DataArray(
            data=ps,
            dims=['time', 'lat', 'lon'],
            coords={'lons': (['lat', 'lon'], lon),
                    'lats': (['lat', 'lon'], lat),
                    'time': times
                    },
            attrs={'long_name': 'Surface Pressure', 'units': 'Pa'}
        ),
        'air_temp': xr.DataArray(
            data=temp,
            dims=['time', 'lev', 'lat', 'lon'],
            coords={'lons': (['lat', 'lon'], lon),
                    'lats': (['lat', 'lon'], lat),
                    'lev': (['lev'], lev),
                    'time': times,
                    },
            attrs={'long_name': 'Air Temperature', 'units': 'K'}
        ),
        'rel_humid': xr.DataArray(
            data=rh,
            dims=['time', 'lev', 'lat', 'lon'],
            coords={'lons': (['lat', 'lon'], lon),
                    'lats': (['lat', 'lon'], lat),
                    'lev': (['lev'], lev),
                    'time': times,
                    },
            attrs={'long_name': 'Relative Humidity', 'units': '%'}
        ),
    },
        attrs={'Title': 'EViz test data',
               'Start_date': '2022-01-01',
               'MAP_PROJECTION': 'Lambert Conformal',
               'SOUTH_WEST_CORNER_LAT': 35.,
               'SOUTH_WEST_CORNER_LON': -105.,
               'TRUELAT1': 40.,
               'TRUELAT2': 35.,
               'STANDARD_LON': -99.,
               }
    )
    if path is None:
        path = os.path.join(constants.ROOT_FILEPATH, 'test/data')
    u.mkdir_p(path)
    ds.to_netcdf(os.path.join(path, 'spacetime.nc'), format='NETCDF4')
    return ds


def make_fake_column_dataset(path=None):
    np.random.seed(123)
    times = pd.date_range(start='2000-01-01',
                          freq=pd.DateOffset(months=1),
                          periods=12)
    ds = xr.Dataset({
        'SWdown': xr.DataArray(
            data=np.random.random(12),  # enter data here
            dims=['time'],
            coords={'time': times},
            attrs={
                '_FillValue': -999.9,
                'units': 'W/m2'
            }
        ),
        'LWdown': xr.DataArray(
            data=np.random.random(12),  # enter data here
            dims=['time'],
            coords={'time': times},
            attrs={
                '_FillValue': -999.9,
                'units': 'W/m2'
            }
        )
    },
        attrs={'example_attr': 'this is a global attribute'}
    )
    if path is None:
        path = os.path.join(constants.ROOT_FILEPATH, 'test/data')
    u.mkdir_p(path)
    ds.to_netcdf(os.path.join(path, 'column.nc'), format='NETCDF4')
    return ds



