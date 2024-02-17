import logging
import warnings
from typing import Any
import pandas as pd
from dataclasses import dataclass, field

from eviz.lib.eviz.figure import Figure
from eviz.lib.eviz.plot_utils import print_map
from eviz.models.root import Root

warnings.filterwarnings("ignore")


@dataclass
class Airnow(Root):
    """ Define Airnow inventory data and functions.
    """
    source_data: Any = None
    _ds_attrs: dict = field(default_factory=dict)
    _maps_params: dict = field(default_factory=dict)
    frame_params: Any = None

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(__name__)

    def __post_init__(self):
        self.logger.info("Start init")
        super().__post_init__()
        self._map_params = self.config.map_params
        self.source_name = 'airnow'

    def process_data(self, filename) -> pd.DataFrame:
        """ Prepare data for plotting """
        # Get the model data
        model_data = self.config.readers[self.source_name].read_data(filename)
        # create time column
        model_data['time'] = pd.to_datetime(
            (model_data.ValidDate + ' ' + model_data.ValidTime),
            format='%m/%d/%y %H:%M')

        # set index
        seldata = model_data.sort_values(by=['AQSID', 'time'])
        seldata = seldata.set_index(['time', 'AQSID'])

        # conversion to xarray dataset to calculate averages
        chem_fields = ['PM25_Unit', 'OZONE_Unit', 'NO2_Unit', 'CO_Unit', 'SO2_Unit', 'PM10_Unit']
        selds = seldata.to_xarray()
        selds = selds.drop(chem_fields)
        return selds.to_dataframe().reset_index()

    def _single_plots(self, plotter):
        map_params = self.config.map_params
        field_num = 0
        for i in map_params.keys():
            field_name = map_params[i]['field']
            source_name = map_params[i]['source_name']
            filename = map_params[i]['filename']
            file_index = self.config.get_file_index(filename)
            model_data = self.process_data(filename)
            self.config.ds_index = self.config.source_names.index(source_name)
            self.config.findex = file_index
            self.config.pindex = field_num
            for pt in map_params[i]['to_plot']:
                self.logger.info(f"Plotting {field_name}, {pt} plot")
                figure = Figure(self.config, pt)
                data_to_plot = self._get_field_to_plot(model_data, field_name, file_index, pt, figure)
                plotter.single_plots(self.config, field_to_plot=data_to_plot)
                print_map(self.config, pt, self.config.findex, figure)

            field_num += 1

    def _get_field_to_plot(self, model_data, field_name, file_index, plot_type, figure):
        _, ax = figure.get_fig_ax()
        self.config.ax_opts = figure.init_ax_opts(field_name)
        dim1, dim2 = self.config.get_dim_names(plot_type)
        # TODO: consider diff fields
        data2d = model_data
        if 'xt' in plot_type:
            return data2d, None, None, field_name, plot_type, file_index, figure, ax
        return data2d, model_data[dim1], model_data[dim2], field_name, plot_type, file_index, figure, ax
