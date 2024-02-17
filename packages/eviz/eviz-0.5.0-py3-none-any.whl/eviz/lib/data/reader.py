from dataclasses import dataclass
from typing import Any
from abc import ABC, abstractmethod

import logging
from eviz.lib import const as constants
import eviz.lib.utils as u


@dataclass
class DataReader(ABC):
    source_name: str

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    def __post_init__(self):
        self.logger.info("Start init")
        self.datasets = []
        self.meta_coords = u.read_meta_coords()
        self.meta_attrs = u.read_meta_attrs()

    @abstractmethod
    def read_data(self, file_path: str) -> Any:
        raise NotImplementedError("Subclasses must implement read_data method.")

    def get_field(self, name: str, ds_index: int):
        """ Extract field from xarray Dataset

        Parameters:
            name (str) : name of field to extract from dataset
            ds_index (int) : index of dataset to extract from

        Returns:
            DataArray containing field data
        """
        try:
            self.logger.debug(f" -> getting field {name}, from index {ds_index}")
            self.logger.debug(f" -> from  filename {self.datasets[ds_index]['filename']}")
            return self.datasets[ds_index]['vars'][name]
        except Exception as e:
            self.logger.error('key error: %s, not found' % str(e))
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

    def get_datasets(self):
        return self.datasets

    def get_dataset(self, i):
        return self.datasets[i]


def get_data_coords(model_name, data2d, generic_attr):
    if generic_attr == 'xc':
        return _get_data_coords(data2d, constants.xc[model_name])
    elif generic_attr == 'yc':
        return _get_data_coords(data2d, constants.yc[model_name])
    elif generic_attr == 'zc':
        return _get_data_coords(data2d, constants.zc[model_name])


def _get_data_coords(data2d, attribute_name):
    if attribute_name is not None:
        return getattr(data2d, attribute_name).values
    else:
        # Handle the case when the generic name is not found in the mapping
        raise ValueError(f"Generic name for {attribute_name} not found in attribute_mapping.")
