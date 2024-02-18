import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
from adjustText import adjust_text
from shapely.geometry import shape
from tbthematic.commun_funcs import add_north, add_scalebar, get_feature_by_geojson, ReadGeoInfo


def tb_thematic_map(tiff_path,
                    geojson_path,
                    vector_properties_list,
                    out_png,
                    tile_name,
                    all_colors,
                    all_colors_name,
                    pyramid_number=3000,
                    is_texts=True):
    # 栅格与矢量信息读取
    img_info = ReadGeoInfo()
    img_info.read_info_from_tiff(tiff_path)
    pyramid_level = round(max(img_info.xsize / pyramid_number, img_info.ysize / pyramid_number, 1))
    img_info.read_overview_from_tiff(tiff_path, pyramid_level)
    img_info.read_info_from_shp(geojson_path)
    # 计算dpi并设置幕布的宽度固定值为8
    fig_size_y = 8
    x_cols = img_info.overview_xsize
    y_rows = img_info.overview_ysize
    dpi = round(max(y_rows * 2 / fig_size_y, 100), -1)
    # 根据矢量四至确定矢量扩展范围与幕布的长度值
    shp_extent = img_info.shp_extent
    lon_extent = shp_extent[1] - shp_extent[0]
    lat_extent = shp_extent[3] - shp_extent[2]
    lon_lat_ratio = lon_extent / lat_extent
    shp_extend_extent = [shp_extent[0] - 0.1 / lon_lat_ratio * img_info.shp_x,
                         shp_extent[1] + 0.22 / lon_lat_ratio * img_info.shp_x,
                         shp_extent[2] - 0.22 * max(lon_lat_ratio, 1) * img_info.shp_y,
                         shp_extent[3] + 0.1 * max(lon_lat_ratio, 1) * img_info.shp_y]
    fig_size_x = round(
        8 * ((shp_extend_extent[1] - shp_extend_extent[0]) / (shp_extend_extent[3] - shp_extend_extent[2])), 1)
    # 调节幕布大小与图中字体大小
    if fig_size_x >= 8:
        tile_fontsize = 18 + (fig_size_x - 8)
        legend_tile_fontsize = 13 + (fig_size_x - 8)
        legend_color_fontsize = 11 + (fig_size_x - 8)
        shp_fontsize = 13 + (fig_size_x - 8)
        north_fontsize = 15 + round((fig_size_x - 8) / 3, 1)
        scalebar_fontsize = 15 + round((fig_size_x - 8) / 5, 1)
    else:
        tile_fontsize = 18 + round((fig_size_x - 8) / 3, 1)
        legend_tile_fontsize = 13 + round((fig_size_x - 8) / 3, 1)
        legend_color_fontsize = 11 + round((fig_size_x - 8) / 3, 1)
        shp_fontsize = 13 + round((fig_size_x - 8) / 3, 1)
        north_fontsize = 15 + round((fig_size_x - 8) / 3, 1)
        scalebar_fontsize = 15 + round((fig_size_x - 8) / 3, 1)
    # 设置指北针参数
    north_height = 0.056
    north_width = round((north_height * (shp_extend_extent[3] - shp_extend_extent[2])) / 1.6 / (
            shp_extend_extent[1] - shp_extend_extent[0]), 2)
    # 设置比例尺参数
    scalebar_distance = 0
    scalebar_distance_unit = 0
    while scalebar_distance <= 0:
        scalebar_distance = round(((shp_extend_extent[1] - shp_extend_extent[0]) * 111 * 0.3) / 2,
                                  scalebar_distance_unit)
        scalebar_distance_unit += 1
        original_scalebar_distance = ((shp_extend_extent[1] - shp_extend_extent[0]) * 111 * 0.3) / 2
        if scalebar_distance / original_scalebar_distance >= 1.5:
            scalebar_distance = round(((shp_extend_extent[1] - shp_extend_extent[0]) * 111 * 0.3) / 2,
                                      scalebar_distance_unit)
        if scalebar_distance_unit > 4:
            break
    # 获取颜色表
    tiff_unique_list = img_info.unique_value_list
    plot_colors = all_colors[min(tiff_unique_list) - 1: max(tiff_unique_list)]
    # 栅格图加载
    arr_mask_nodata = img_info.overview_ds_array
    tiff_extent = [img_info.overview_ulx, img_info.overview_lrx, img_info.overview_lry, img_info.overview_uly]
    proj = ccrs.PlateCarree()
    fig = plt.figure(figsize=[fig_size_x, fig_size_y],
                     dpi=dpi)
    colors = plot_colors
    cmap = mpl.colors.ListedColormap(colors)
    ax = fig.add_subplot(111, projection=proj)
    plt.subplots_adjust(top=0.92,
                        bottom=0.05,
                        right=0.94,
                        left=0.06,
                        hspace=0,
                        wspace=0)

    ax.imshow(arr_mask_nodata, extent=tiff_extent, cmap=cmap)

    ax.set_extent(shp_extend_extent, crs=proj)
    ax.add_geometries(Reader(geojson_path).geometries(), proj,
                      facecolor="none",
                      edgecolor="black",
                      linewidth=0.8)
    if is_texts:
        # 在矢量图层添加区县名字
        texts = list()
        feature_list = get_feature_by_geojson(geojson_path, vector_properties_list)
        for feature in feature_list:
            name = feature[vector_properties_list[0]]
            geo = shape(feature['geo'])
            geo_bounds = tuple(geo.bounds)
            labelx, labely = ((geo_bounds[0] + geo_bounds[2]) / 2,
                              (geo_bounds[1] + geo_bounds[3]) / 2 + (geo_bounds[3] - geo_bounds[1]) * 0)
            texts.append(plt.text(labelx, labely,
                                  name, fontsize=shp_fontsize,
                                  horizontalalignment="left",
                                  fontproperties="SimHei",
                                  fontweight="bold",
                                  va="bottom",
                                  color="#000000"))
        # 避免图片上的文字重叠
        adjust_text(texts, )
    # 标题设置
    plt.title(tile_name, fontsize=tile_fontsize,
              loc="center", weight="bold",
              y=1.012)
    # 图例设置
    texts = all_colors_name
    patches = [mpatches.Patch(color=all_colors[i],
                              label="{:s}".format(texts[i])) for i in range(len(texts))]
    plt.legend(title="图例", handles=patches,
               loc="lower right", ncol=1,
               fontsize=legend_color_fontsize,
               title_fontsize=legend_tile_fontsize,
               frameon=False)
    # 指北针
    add_north(ax, label_size=north_fontsize,
              loc_x=0.93,
              loc_y=0.98,
              width=north_width,
              height=north_height,
              pad=0.1)
    # 比例尺
    add_scalebar(ax,
                 metric_distance=scalebar_distance * 1000,
                 at_x=[0.04, 0.1],
                 at_y=[0.04, 0.06],
                 max_stripes=2,
                 xtick_label_margins=0.02,
                 ytick_label_margins=0.20,
                 rotation=0,
                 fontsize=scalebar_fontsize,
                 font_weight="bold")
    # 图片保存
    os.makedirs(os.path.split(out_png)[0], exist_ok=True)
    plt.savefig(out_png, dpi=dpi, pad_inches=0)
    plt.close()
