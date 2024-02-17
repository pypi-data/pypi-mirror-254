from .base_dashboard import BaseDash


class CfDash(BaseDash):

    def __init__(self, config, params):
        super().__init__(config=config, params=params)


    def get_comparison_types(self):
        if (self.params.model == 'cf') and (self.params.comparison_source in ['omi',
                                                                              'mopitt-toco']):
            if self.params.zc is not None:
                if 'yz' in self.params.plot_type.value:
                    newt = []
                    for p in self.params.plot_type.value:
                        if p != 'yz':
                            newt.append(p)
                    self.params.plot_type.value = newt
                return True
            else:
                return False
        else:
            return False


    def set_f1_xy(self, data2d):
        """
        Set tc plot for file 1. 

        Sets:
                tc (list): list containing xy plots.
        """
        do_tc = self.get_comparison_types()
        if do_tc:
            xy = []
            if 'xy' in self.params.plot_type.value:
                xy_data = self.data3d.sum(dim=self.params.zc)
                xy_data.attrs = self.data3d.attrs

                img_opts = self.get_xy_opts(xy_data)
                title = xy_data.name + ' Total Column'
                img_opts['title'] = title

                self.clim = self.get_clim(xy_data, self.data_2)

                img_opts['clim'] = self.clim #rewrite get clim function in this class because the get clim function is only using the xy slice data to do it not the total column data to do it and its different. 

                for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                    plot = self._plot(self.get_converter(xy_data, 'xy', self.params.field, 
                                    self.params.xc, self.params.yc, self.params.tc, self.params.zc), 
                                    plot_kind,
                                    img_opts
                                    )
                    if plot_kind == 'contourf' or plot_kind == 'contour':
                        ticker2 = self.colorbar_ticks(plot, xy_data)
                        plot.opts(colorbar_opts={'ticker': ticker2})
                    if self.params.zonal_cnorm == 'log':
                        plot = plot.opts(clim=(float(xy_data.min().values), None))
                    if self.config.trop_filename is not None:
                        plot = self.overlay_trop(plot)
                    plot = self.create_overlay(plot)
                    plot = plot.hist() if self.params.add_histo else plot
                    xy.append(plot)
        else:
            xy = []
            if 'xy' in self.params.plot_type.value:
                img_opts = self.get_xy_opts(data2d)
                title = self.title_function(data2d, self.config.exp_name, self.params.zc, self.params.tc)
                img_opts['title'] = title
                for plot_kind in self.get_2d_plot_types(self.params.plot_kind.value):
                    plot = self._plot(self.get_converter(data2d, 'xy', self.params.field, 
                                    self.params.xc, self.params.yc, self.params.tc, self.params.zc), 
                                    plot_kind,
                                    img_opts
                                    )
                    if plot_kind == 'contourf' or plot_kind == 'contour':
                        ticker1 = self.colorbar_ticks(plot, data2d, self.clim[0], self.clim[1])
                        plot.opts(colorbar_opts={'ticker': ticker1})
                    plot = self.create_overlay(plot)
                    plot = plot.hist() if self.params.add_histo else plot
                    xy.append(plot)
        self.xy = xy
