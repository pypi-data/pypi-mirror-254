import xarray as xr
import holoviews as hv
import param
import panel as pn

import geoviews as gv
import cartopy.crs as ccrs

import eviz.lib.iviz.params_util as params_util
from eviz.lib.iviz.notyf import Notyf

pn.extension()
hv.extension('bokeh', logo=False)


class MultiFile(param.Parameterized):
    """ 'mini' control panel for multiple file plotting
    """

    plot = param.Selector(label='Variable')

    xc = param.ObjectSelector(precedence=-1)
    yc = param.ObjectSelector(precedence=-1)
    zc = param.ObjectSelector(precedence=-1)
    tc = param.ObjectSelector(precedence=-1)

    z = param.Integer(label='Vertical level')
    t = param.Integer(label='Time')

    cmap = param.ObjectSelector('rainbow', objects=['rainbow', 'viridis', 'spectral', 'colorwheel', 'bwr'],
                                label="Color theme")

    layout = hv.Layout()

    show_coastlines = param.Boolean(False)
    custom_title = param.Boolean(False)
    show_data = param.Boolean(False)
    text_input = pn.widgets.TextInput(placeholder='Type plot title here')
    show_statistics = param.Boolean(False)
    show_grid = param.Boolean(False, label='Add grid')
    logy = param.Boolean(False, label="Log zonal y axis")
    cnorm = param.ObjectSelector(objects=['linear', 'log', 'eq_hist'], default='linear', label='Colorbar normalization')
    tabs_switch = param.Boolean(True, label="Toggle Tabs")
    invert_zonal_y = param.Boolean(True, label='Invert zonal y-axis')
    invert_zonal_x = param.Boolean(False, label='Invert zonal x-axis')
    radio_group = pn.widgets.RadioButtonGroup(name='Primary Dimension', options=['level', 'time'])
    color_levels = param.Integer(default=16, bounds=(4, 28), label='Contour color levels')
    save_layout_button = pn.widgets.Button(name='Save layout', align='start', width=150)

    keys = None
    coords = None
    ndims = None
    model = None

    def __init__(self, file, model_name, **params):
        self.file = xr.open_dataset(file)
        self.input = file
        self.model_name = model_name

        self.notyf = Notyf(types=[{"type": "error", "background": "red"}, {"type": "success", "background": "green"}])

        self.keys = params_util.get_keys(self.file)
        self.coords = params_util.get_coords(self.file)
        self.meta_coords = params_util.load_model_coords()
        self.ndims = params_util.get_ndims(self.file)
        self.dims = params_util.get_dims(self.file)
        self.model = params_util.get_model_type(self.coords)  # self.model_name)

        self.set_dim_params(self.model)

        self.check_for2d()

        self.set_param_values()

        self.data4d = None
        self.data3d = None
        self.data2d = None

        self.set_selected_data()

        super().__init__(**params)

    def check_for2d(self):
        if self.ndims < 4:
            self.zc = None
            # self.z = None
            self.param.z.precedence = -1

    def set_dim_params(self, model):
        meta_coords = self.meta_coords

        if model == 'ccm':
            self.xc = meta_coords['xc']['ccm']
            self.yc = meta_coords['yc']['ccm']
            self.zc = meta_coords['zc']['ccm']
            self.tc = meta_coords['tc']['ccm']

        elif model == 'cf':
            self.xc = meta_coords['xc']['cf']
            self.yc = meta_coords['yc']['cf']
            self.tc = meta_coords['tc']['cf']
            self.zc = meta_coords['zc']['cf']

        elif model == 'lis':
            self.xc = meta_coords['xc']['lis']
            self.yc = meta_coords['yc']['lis']
            self.zc = meta_coords['zc']['lis']
            self.tc = meta_coords['tc']['lis']

        elif model == 'gmi':
            self.xc = meta_coords['xc']['gmi']
            self.yc = meta_coords['yc']['gmi']
            self.zc = meta_coords['zc']['gmi']
            self.tc = meta_coords['tc']['gmi']

        elif model == 'nuwrf':
            self.xc = meta_coords['xc']['nuwrf']
            self.yc = meta_coords['yc']['nuwrf']
            self.tc = meta_coords['tc']['nuwrf']
            self.zc = meta_coords['zc']['nuwrf']

        elif model is None:
            self.notyf.error("Could not find model type - please check terminal! ")
            print(' Please enter in full, case-sensitive, which coordinate to use for x and y axis ')
            print(' Available coords: ')
            print(self.coords)
            x_user_input = input(" X coordinate: ")
            y_user_input = input(" Y coordinate: ")
            if len(self.coords) > 2:
                time_user_input = input(" Time coorinate: ")
                tc = time_user_input
            else:
                tc = None
            if len(self.coords) > 3:
                z_user_input = input(" Z Coordinate: ")
                zc = z_user_input
            else:
                zc = None

            xc = x_user_input
            yc = y_user_input

            self.xc = xc
            self.yc = yc
            self.zc = zc
            self.tc = tc

    def set_param_values(self):
        gif_dim_opts = []
        if self.zc is not None:
            self.z = 0
            length = len(self.file[self.zc].values)
            if length != 1:
                end_bound = length - 1
                bounds = (0, end_bound)
                self.param['z'].bounds = bounds  # set bounds of z param.Integer
                self.param['z'].precedence = +1
                gif_dim_opts.append(self.zc)
            else:
                self.param['z'].precedence = -1

        self.t = 0
        t_length = len(self.file[self.tc].values)
        if t_length != 1:
            end_t = t_length - 1
            t_bounds = (0, end_t)
            self.param['t'].bounds = t_bounds
            self.param['t'].precedence = +1
            gif_dim_opts.append(self.tc)
        else:
            self.param['t'].precedence = -1

        self.param['plot'].objects = self.keys
        self.param.set_param(plot=self.keys[0])

    @param.depends('z', 't', 'plot')
    def set_selected_data(self):
        self.data4d = self.file[self.plot]

        if self.zc in list(self.data4d.coords):
            self.data2d = self.data4d.isel(lev=self.z, time=self.t)
            self.data3d = self.data4d.isel(time=self.t)
        elif self.zc not in list(self.data4d.coords):
            self.data2d = self.data4d.isel(time=self.t)
        else:   # data is just lat/lon?
            self.data2d = self.data4d
        return self.data2d

    def title_function(self, time_select2):
        if self.plot == "aoa":
            time_select2.aoa.attrs['units'] = 'days'
        if self.zc in list(self.data4d.coords):
            title = self.text_input.value if self.custom_title else (
                        str(time_select2.long_name) + " (" + str(time_select2.units) + ") @ " + str(
                    time_select2['lev'].values) + " " +
                        str(time_select2['lev'].units))  # + " " + str(time_select['lev'].long_name))

        else:
            title = self.text_input.value if self.custom_title else (
                        str(time_select2.long_name) + " (" + str(time_select2.units) + ") ")

        return title

    @param.depends('t', 'plot', 'show_statistics', 'z')
    def statistics_box(self):
        """ 
        get basic statistics and display values in markdown pane  
        """
        data = self.data2d

        # Get rounded statistics
        mean = data.mean().round(3).values
        max_ = data.max().round(3).values
        min_ = data.min().round(3).values
        std = data.std().round(3).values
        med = data.median().round(3).values

        # Sci notation formatting
        if mean == 0.0:
            mean = '{:0.3e}'.format(data.mean().values)
        if max_ == 0.0:
            max_ = '{:0.3e}'.format(data.max().values)
        if min_ == 0.0:
            min_ = '{:0.3e}'.format(data.min().values)
        if std == 0.0:
            std = '{:0.3e}'.format(data.std().values)
        if med == 0.0:
            med = '{:0.3e}'.format(data.median().values)

        if self.show_statistics:
            column = pn.pane.Markdown("""
                 #### <div align="center">  Mean:  {}  <br />  Median: {} <br />  Max:  {}  <br />  Min:  {}  <br />  Std:  {}  </div> </font>
            """.format(
                str(mean), str(med), str(max_), str(min_), str(std)), style={'font-family': "Times New Roman",
                                                                             'color': '#92a8d1'}, align='center',
                width=200, background='#1B345C'
            )
        else:
            column = None
        return column

    @param.depends('plot', 'cmap', 't', 'z', 'radio_group.value')
    def gif(self):
        """ 
        create gif on either time or lev based on user selection  
        """
        data_convert = self.data4d

        if self.radio_group.value == 'level':
            if 'lev' in list(data_convert.coords):
                global images
                images = ({i: hv.Image(data_convert.isel(time=self.time, lev=i)).opts(
                    title=str(data_convert.long_name) + ' ' + str(data_convert.units) + ' ' + str(
                        data_convert.lev.values[i]), colorbar=True, shared_axes=False, cmap='rainbow', width=500,
                    height=300) for i in range(len(data_convert.lev.values))})
                global contours
                contours = {}

                def get_contours():
                    for i in images:
                        contours[i] = hv.operation.contours(images[i], levels=8, filled=True).opts(
                            title=str(data_convert.long_name) + ' ' + str(data_convert.units) + ' ' + str(
                                data_convert.lev.values[i]), padding=0, shared_axes=False,
                            color_levels=self.color_levels, cmap='rainbow', width=500, height=300, colorbar=True)
                        # self.progress.value = i
                    return contours

                contours = get_contours()
                global hmap
                hmap = hv.HoloMap(contours).opts(framewise=True)
            else:
                # print('No lev values for '+ self.plot +' variable')
                # global hmap
                hmap = None

        elif self.radio_group.value == 'time':
            if 'lev' in list(data_convert.coords):
                images = ({i: hv.Image(data_convert.isel(time=i, lev=self.lev)).opts(
                    title=str(data_convert.long_name) + ' ' + str(data_convert.units) + ' ' + str(
                        data_convert.lev.values[i]), colorbar=True, shared_axes=False, cmap='rainbow', width=500,
                    height=300) for i in range(len(data_convert.time.values))})
                contours = {}
                contours = get_contours()
                # global hmap
                hmap = hv.HoloMap(contours).opts(framewise=True)
            else:
                images = ({i: hv.Image(data_convert.isel(time=i)).opts(
                    title=str(data_convert.long_name) + ' ' + str(data_convert.units) + ' ' + str(
                        data_convert.lev.values[i]), colorbar=True, shared_axes=False, cmap='rainbow', width=500,
                    height=300) for i in range(len(data_convert.time.values))})
                contours = {}
                contours = get_contours()
                # global hmap
                hmap = hv.HoloMap(contours).opts(framewise=True)

    @param.depends('z', 'show_data')
    def data_show(self):
        """ 
        add panel Row with file metadata if show data is checked   
        """
        if self.show_data:
            pane = pn.Row(self.file)
        else:
            pane = None
        return pane

    def make_coastlines(self, xy_contours):
        """
        create coastlines from app shapefile using geopandas and spatial pandas, plot with hvplot 
        overlay with xy image and xy contours (if provided) and return overlays
        """
        if self.show_coastlines:
            # borders_ = gpd.read_file('app/geo_features/countries_50m/ne_50m_admin_0_countries.shp')
            # borders_ = spd.GeoDataFrame(borders_)
            # borders = borders_.hvplot.paths(color='black', line_width=0.4, rasterize=True).opts(cmap=['black'], colorbar=False, alpha=0.7) 
            coast = gv.feature.coastline().opts(projection=ccrs.PlateCarree())
            border = gv.feature.borders().opts(projection=ccrs.PlateCarree())
            borders = coast * border

            xy_cont_overlay = xy_contours * borders if xy_contours is not None else None
        else:
            xy_cont_overlay = xy_contours

        return xy_cont_overlay

    @param.depends('plot', 'z', 't', 'cmap', 'text_input.value', 'custom_title', 'text_input.value', 'show_coastlines',
                   'tabs_switch', 'logy', 'color_levels', 'show_grid', 'cnorm',
                   'invert_zonal_x', 'invert_zonal_y')
    def tabs(self):
        data2d = self.set_selected_data()

        img_opts = dict(clabel=str(data2d.long_name) + " " + str(data2d.units), padding=0, cnorm=self.cnorm,
                        show_grid=self.show_grid,
                        height=700, width=700, cmap=self.cmap, tools=["hover"], colorbar=True,
                        colorbar_position='bottom', toolbar='above',
                        title=self.title_function(time_select2=data2d))  # max_height=1100, max_width=1100)

        # create xy contours
        if len(list(self.data4d[self.yc].values)) != 1 and len(list(self.data4d[self.xc].values)) != 1:
            xy_contours = data2d.hvplot.contourf(x=self.xc, y=self.yc, levels=self.color_levels).opts(**img_opts)
        else:
            xy_contours = None

        xy_contours = self.make_coastlines(xy_contours)

        # check for lev in data.coords - if yes, create yz contours
        if self.zc in list(self.data4d.coords):
            if len(list(self.data4d[self.zc].values)) != 1 and len(list(self.data4d[self.yc].values)) != 1:
                data2 = self.data3d
                data_convert = data2.mean(dim=self.xc)

                yz_quadmesh = hv.QuadMesh(data_convert, kdims=[self.yc, self.zc])
                zonal_opts = dict(cmap=self.cmap, colorbar=True, tools=['hover'], padding=0,
                                  title=self.text_input.value + " Zonal Mean" if self.custom_title else str(
                                      data2.long_name) + " " + str(data2.units) + " Zonal Mean",
                                  colorbar_position='bottom',
                                  toolbar='above', clabel=str(data2.long_name) + " " + str(data2.units),
                                  cnorm=self.cnorm, invert_xaxis=self.invert_zonal_x,
                                  height=700, width=700, logy=self.logy, invert_yaxis=self.invert_zonal_y,
                                  show_grid=self.show_grid)

                yz_contours = data_convert.hvplot.contourf(levels=self.color_levels, x=self.yc, y=self.zc).opts(
                    **zonal_opts)

                layout = hv.Layout(xy_contours + yz_contours).opts(shared_axes=False,
                                                                              tabs=self.tabs_switch).cols(1)
            else:
                layout = hv.Layout(xy_contours).opts(shared_axes=True, tabs=self.tabs_switch).cols(1)
        else:  # no lev in data.coords, no yz contours in layout
            layout = hv.Layout(xy_contours).opts(shared_axes=True, tabs=self.tabs_switch).cols(1)

        return layout

    # @pn.depends('save_layout_button.clicks', 'tabs_switch')
    # def save_layout(self):
    #     """ 
    #     save overall layout of the plots when tabs are turned off 
    #     -broken 
    #     """
    #     if self.save_layout_button.clicks:
    #         layout = self.tabs()
    #         layout = pn.Row(layout.cols(2), width=1000, height=1300)
    #         layout.save('layout.png')
