import os
import re
import json
import osr
from osgeo import gdal, ogr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager as mfonts
import cartopy.crs as ccrs


# 读取地理数据的信息
class ReadGeoInfo(object):
    def __init__(self):
        self.filename = None
        self.in_ds = None
        self.in_band = None
        self.bands = None
        self.band_type = None
        self.ct = None
        self.geotransform = None
        self.resolution = None
        self.lrx = None
        self.lry = None
        self.projection = None
        self.ulx = None
        self.uly = None
        self.xsize = None
        self.ysize = None
        self.nodata = None
        self.unique_value_list = None
        self.ds_array = None
        self.epsg = None
        self.shp_extent = None
        self.shp_x = None
        self.shp_y = None
        self.shp_spatialref_wkt = None
        self.shp_geogcs = None
        self.shp_proj4 = None
        self.overview_ulx = None
        self.overview_uly = None
        self.overview_lrx = None
        self.overview_lry = None
        self.overview_xsize = None
        self.overview_ysize = None
        self.overview_ds_array = None

    def read_info_from_tiff(self, filename):
        ds = gdal.Open(filename)
        if ds is None:
            return 'Could not open {0}'.format(filename)
        self.in_ds = ds
        self.filename = filename
        self.bands = ds.RasterCount
        self.xsize = ds.RasterXSize  # 列 纬度
        self.ysize = ds.RasterYSize  # 行 经度
        self.band_type = ds.GetRasterBand(1).DataType
        self.projection = ds.GetProjection()
        self.geotransform = ds.GetGeoTransform()
        self.resolution = ds.GetGeoTransform()[1]
        self.ulx = self.geotransform[0]  # u:up,l:left,x:lon
        self.uly = self.geotransform[3]  # u:up,l:left,y:lat
        self.lrx = self.ulx + self.geotransform[1] * self.xsize  # l:low,r:right,x:lon
        self.lry = self.uly + self.geotransform[5] * self.ysize  # l:low,r:right,y:lat
        self.in_band = ds.GetRasterBand(1)

        proj = osr.SpatialReference(wkt=self.projection)
        epsg = proj.GetAttrValue('AUTHORITY', 1)
        self.epsg = epsg

        nodata = ds.GetRasterBand(1).GetNoDataValue()
        self.nodata = nodata

        ct = ds.GetRasterBand(1).GetRasterColorTable()
        if ct is not None:
            self.ct = ct.Clone()
        else:
            self.ct = None

        unique_value_list = list()
        exact_hist = ds.GetRasterBand(1).GetHistogram(approx_ok=False)
        for index, value in enumerate(exact_hist):
            if value != 0:
                unique_value_list.append(index)
        self.unique_value_list = unique_value_list

        return 1

    def read_array_from_tiff(self, filename):

        ds = gdal.Open(filename)
        if ds is None:
            return 'Could not open {0}'.format(filename)

        band = ds.GetRasterBand(1)
        ds_array = band.ReadAsArray()
        ds_array = ds_array.astype(float)
        ds_array[np.where(ds_array == self.nodata)] = np.nan
        self.ds_array = ds_array
        return 1

    def read_overview_from_tiff(self, filename, level):

        ds = gdal.Open(filename)
        if ds is None:
            return 'Could not open {0}'.format(filename)
        band = ds.GetRasterBand(1)
        ds_array = band.ReadAsArray(0, 0, self.xsize, self.ysize,
                                    int(self.xsize / level),
                                    int(self.ysize / level))
        ds_array = ds_array.astype(float)
        ds_array[np.where(ds_array == self.nodata)] = np.nan
        self.overview_ds_array = ds_array
        self.overview_ulx = self.geotransform[0]
        self.overview_uly = self.geotransform[3]
        self.overview_ysize = ds_array.shape[0]
        self.overview_xsize = ds_array.shape[1]
        self.overview_lrx = self.lrx
        self.overview_lry = self.lry
        return 1

    def read_info_from_shp(self, filename):
        shp_ds = ogr.Open(filename)
        if shp_ds is None:
            return 'Could not open {0}'.format(filename)

        Ly = shp_ds.GetLayer(0)
        shp_extent = Ly.GetExtent()
        self.shp_extent = shp_extent
        self.shp_x = shp_extent[1] - shp_extent[0]
        self.shp_y = shp_extent[3] - shp_extent[2]

        spatialref = Ly.GetSpatialRef()
        s = spatialref.ExportToWkt()
        geogcs = re.findall('GEOGCS\["(.*)",DATUM', s)
        proj = osr.SpatialReference(wkt=s)
        proj4 = proj.ExportToProj4()

        self.shp_spatialref_wkt = s
        self.shp_geogcs = geogcs
        self.shp_proj4 = proj4

        return 1


# 根据矢量属性提取矢量边界的列表
def get_feature_by_geojson(geojson, vector_properties_list):
    if isinstance(geojson, str):
        if os.path.exists(geojson):
            with open(geojson, 'r') as f:
                geo_dic = json.loads(f.read())
        else:
            return None
    else:
        geo_dic = geojson

    feature_list = [feature for feature in geo_dic['features']]
    code_list = list()
    for geo in feature_list:
        code_dict = dict()
        for vector_properties in vector_properties_list:
            code_dict[vector_properties] = geo['properties'][vector_properties]
        code_dict['geo'] = geo['geometry']
        code_list.append(code_dict)
    return code_list


# 指北针
def add_north(ax, label_size=15, loc_x=0.92, loc_y=0.96, width=0.03, height=0.054, pad=0.12):
    """
    画一个指北针带'N'文字注释
    :param ax: 要画的坐标区域 Axes实例 plt.gca()获取即可
    :param label_size: 显示'N'文字的大小
    :param loc_x: 以文字下部为中心的占整个ax横向比例
    :param loc_y: 以文字下部为中心的占整个ax纵向比例
    :param width: 指南针占ax比例宽度
    :param height: 指南针占ax比例高度
    :param pad: 文字符号占ax比例间隙
    :return:
    """
    min_x, max_x = ax.get_xlim()
    min_y, max_y = ax.get_ylim()
    y_len = max_y - min_y
    x_len = max_x - min_x
    left = [min_x + x_len * (loc_x - width * .5), min_y + y_len * (loc_y - pad)]
    right = [min_x + x_len * (loc_x + width * .5), min_y + y_len * (loc_y - pad)]
    top = [min_x + x_len * loc_x, min_y + y_len * (loc_y - pad + height)]
    center = [min_x + x_len * loc_x, left[1] + (top[1] - left[1]) * .4]
    triangle = mpatches.Polygon([left, top, right, center], color='k')
    r = {'min_x': min_x,
         'max_x': max_x,
         'min_y': min_y,
         'max_y': max_y,
         'y_len': y_len,
         'x_len': x_len,
         'left': left,
         'right': right,
         'top': top,
         'center': center}
    ax.text(s='N',
            x=min_x + x_len * loc_x,
            y=min_y + y_len * (loc_y - pad + height),
            fontsize=label_size,
            horizontalalignment='center',
            verticalalignment='bottom')
    ax.add_patch(triangle)


# 比例尺
def add_scalebar(ax, metric_distance=100,
                 at_x=(0.1, 0.4),
                 at_y=(0.05, 0.075),
                 max_stripes=5,
                 xtick_label_margins=0.2,
                 ytick_label_margins=0.25,
                 fontsize=8,
                 font_weight='bold',
                 rotation=45,
                 zorder=999):
    old_proj = ax.projection
    ax.projection = ccrs.PlateCarree()

    # Set a planar (metric) projection for the centroid of a given axes projection:

    # First get centroid lon and lat coordinates:
    lon_0, lon_1, lat_0, lat_1 = ax.get_extent(ax.projection.as_geodetic())
    central_lon = np.mean([lon_0, lon_1])
    central_lat = np.mean([lat_0, lat_1])

    # Second: set the planar (metric) projection centered in the centroid of the axes;
    # Centroid coordinates must be in lon/lat.
    proj = ccrs.EquidistantConic(central_longitude=central_lon, central_latitude=central_lat)

    # fetch axes coordinates in meters
    x0, x1, y0, y1 = ax.get_extent(proj)
    ymean = np.mean([y0, y1])

    # set target rectangle in-visible-area (aka 'Axes') coordinates
    axfrac_ini, axfrac_final = at_x
    ayfrac_ini, ayfrac_final = at_y

    # choose exact X points as sensible grid ticks with Axis 'ticker' helper
    xcoords = []
    ycoords = []
    xlabels = []
    for i in range(0, 1 + max_stripes):
        dx = (metric_distance * i) + x0
        xlabels.append(dx - x0)

        xcoords.append(dx)
        ycoords.append(ymean)

    # Convertin to arrays:
    xcoords = np.asanyarray(xcoords)
    ycoords = np.asanyarray(ycoords)

    # Ensuring that the coordinate projection is in degrees:
    x_targets, y_targets, z_targets = ax.projection.transform_points(proj, xcoords, ycoords).T
    x_targets = [x + (axfrac_ini * (lon_1 - lon_0)) for x in x_targets]

    # Setting transform for plotting
    transform = ax.projection

    # grab min+max for limits
    xl0, xl1 = x_targets[0], x_targets[-1]

    # calculate Axes Y coordinates of box top+bottom
    yl0, yl1 = [lat_0 + ay_frac * (lat_1 - lat_0) for ay_frac in [ayfrac_ini, ayfrac_final]]

    # calculate Axes X/Y distance of ticks + label margins
    y_margin = (yl1 - yl0) * ytick_label_margins
    x_margin = (xl1 - xl0) * xtick_label_margins / max_stripes
    # fill black/white 'stripes' and draw their boundaries
    fill_colors = ['black', 'white']
    i_color = 0

    filled_boxs = []
    for xi0, xi1 in zip(x_targets[:-1], x_targets[1:]):
        # fill region
        filled_box = plt.fill(
            (xi0, xi1, xi1, xi0, xi0),
            (yl0, yl0, yl1, yl1, yl0),

            fill_colors[i_color],
            transform=transform,
            clip_on=False,
            zorder=zorder
        )

        filled_boxs.append(filled_box[0])

        # draw boundary
        plt.plot((xi0, xi1, xi1, xi0, xi0),
                 (yl0, yl0, yl1, yl1, yl0),
                 'black',
                 clip_on=False,
                 transform=transform,
                 zorder=zorder)

        i_color = 1 - i_color

    # add short tick lines
    for x in x_targets:
        plt.plot((x, x), (yl0, yl0 - y_margin), 'black',
                 transform=transform,
                 zorder=zorder,
                 clip_on=False)

    # add a scale legend 'Km'
    font_props = mfonts.FontProperties(size=fontsize,
                                       weight=font_weight)
    plt.text(xl1 + x_margin,
             yl0 - y_margin,
             'KM',
             color='k',
             verticalalignment='bottom',
             horizontalalignment='left',
             fontproperties=font_props,
             transform=transform,
             clip_on=False,
             zorder=zorder)

    # add numeric labels
    for x, xlabel in zip(x_targets, xlabels):
        # print('Label set in: ', x, yl0 - 2 * y_margin)
        plt.text(x,
                 yl0 - 2 * y_margin,
                 '{:g}'.format((xlabel) * 0.001),
                 verticalalignment='top',
                 horizontalalignment='center',
                 fontproperties=font_props,
                 transform=transform,
                 rotation=rotation,
                 clip_on=False,
                 zorder=zorder + 1
                 )

    # Adjusting figure borders to ensure that the scalebar is within its limits
    ax.projection = old_proj
    ax.get_figure().canvas.draw()
