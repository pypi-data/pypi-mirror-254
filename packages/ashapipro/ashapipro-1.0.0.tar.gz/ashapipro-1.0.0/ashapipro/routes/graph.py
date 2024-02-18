'''
Copyright (c) 2024 SimTech LLC.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


import geopandas as gpd
import numpy as np

from networkx import Graph, astar_path, dijkstra_path, bellman_ford_path

from shapely import intersection as shape_intersection

from shapely.geometry import LineString, Polygon, MultiPolygon

from pyproj import Geod


import os.path

data_folder = os.path.join(os.path.dirname(__file__), "data")


def save_tiles_map(tofile: str, cells, crs='epsg:4326'):
    ''' Save graph tiles/cells to html file to see later visualization of cells over area '''
    df = gpd.GeoDataFrame({ 'area': 'grid', 'geometry' : [MultiPolygon(cells)] }, crs = crs)
    m = df.explore()
    m.save(tofile)


def save_polygon_map(tofile: str, polygon, crs='epsg:4326'):
    ''' Save polygons to html file to see later visualization of polygons over area '''
    df = gpd.GeoDataFrame({ 'area': 'path', 'geometry' : [polygon] }, crs = crs)
    m = df.explore()
    m.save(tofile)


def build_area_tiles_graph_by_neighbors(gdf, tileSize, geod = Geod(ellps="WGS84")):
    xmin,ymin,xmax,ymax =  gdf.total_bounds
    width_m = geod.line_length([xmin,xmax], [ymin,ymin])
    height_m = geod.line_length([xmin,xmin], [ymin,ymax])
    cell_w_m = tileSize # meters
    cols=np.round(width_m/cell_w_m)
    cell_w_deg = (xmax-xmin)/cols
    cell_h_m = tileSize # meters
    rows=np.round(height_m/cell_h_m)
    cell_h_deg = (ymax-ymin)/rows
    XleftOrigin = xmin
    XrightOrigin = xmin + cell_w_deg
    YtopOrigin = ymax
    YbottomOrigin = ymax - cell_h_deg
    cells = []
    intersections = []
    center_points = []
    for i in range(int(cols)):
        Ytop = YtopOrigin
        Ybottom =YbottomOrigin
        for j in range(int(rows)):
            cell_polygon = Polygon([(XleftOrigin, Ytop), (XrightOrigin, Ytop), (XrightOrigin, Ybottom), (XleftOrigin, Ybottom)])
            if shape_intersection(cell_polygon,gdf['geometry'][0]).is_empty:#TO DO make universal. THis will not work with general geo dataframe
                cells.append(cell_polygon) 
            intersections.append(int(shape_intersection(cell_polygon,gdf['geometry'][0]).is_empty))#TO DO make universal. THis will not work with general geo dataframe
            center_points.append(cell_polygon.centroid)
            Ytop = Ytop - cell_h_deg
            Ybottom = Ybottom - cell_h_deg
            
        XleftOrigin = XleftOrigin + cell_w_deg
        XrightOrigin = XrightOrigin + cell_w_deg
    maze = np.asarray(intersections).reshape(int(cols),int(rows)).T
    center_points=np.asarray(center_points).reshape(int(cols),int(rows)).T
    G = Graph()
    #building the graph
    for i in range(int(rows)):
        for j in range(int(cols)):
            if maze[i,j]>0:
                if (i-1>0) and (maze[i-1,j]>0):#north
                    cp1=center_points[i,j]
                    cp2=center_points[i-1,j]
                    edge_len = geod.line_length([cp1.coords[0][0],cp2.coords[0][0]],[cp1.coords[0][1],cp2.coords[0][1]])
                    G.add_node(i*cols+j, center = cp1)
                    G.add_node((i-1)*cols+j, center = cp2)
                    G.add_edge(i*cols+j,(i-1)*cols+j,weight=edge_len)
                if (i+1<rows) and (maze[i+1,j]>0):#south
                    cp1=center_points[i,j]
                    cp2=center_points[i+1,j]
                    edge_len = geod.line_length([cp1.coords[0][0],cp2.coords[0][0]],[cp1.coords[0][1],cp2.coords[0][1]])
                    G.add_node(i*cols+j, center = cp1)
                    G.add_node((i+1)*cols+j, center = cp2)
                    G.add_edge(i*cols+j,(i+1)*cols+j,weight=edge_len)
                if (j-1>0) and (maze[i,j-1]>0):#west
                    cp1=center_points[i,j]
                    cp2=center_points[i,j-1]
                    edge_len = geod.line_length([cp1.coords[0][0],cp2.coords[0][0]],[cp1.coords[0][1],cp2.coords[0][1]])
                    G.add_node(i*cols+j, center = cp1)
                    G.add_node(i*cols+j-1, center = cp2)
                    G.add_edge(i*cols+j,i*cols+j-1,weight=edge_len)
                if (j+1<cols) and (maze[i,j+1]>0):#east
                    cp1=center_points[i,j]
                    cp2=center_points[i,j+1]
                    edge_len = geod.line_length([cp1.coords[0][0],cp2.coords[0][0]],[cp1.coords[0][1],cp2.coords[0][1]])
                    G.add_node(i*cols+j, center = cp1)
                    G.add_node(i*cols+j+1, center = cp2)
                    G.add_edge(i*cols+j,i*cols+j+1,weight=edge_len)
                if (j-1>0) and (i-1>0) and (maze[i-1,j-1]>0):#north-west
                    cp1=center_points[i,j]
                    cp2=center_points[i-1,j-1]
                    edge_len = geod.line_length([cp1.coords[0][0],cp2.coords[0][0]],[cp1.coords[0][1],cp2.coords[0][1]])
                    G.add_node(i*cols+j, center = cp1)
                    G.add_node((i-1)*cols+j-1, center = cp2)
                    G.add_edge(i*cols+j,(i-1)*cols+j-1,weight=edge_len)
                if (j+1<cols) and (i-1>0) and (maze[i-1,j+1]>0):#north-east
                    cp1=center_points[i,j]
                    cp2=center_points[i-1,j+1]
                    edge_len = geod.line_length([cp1.coords[0][0],cp2.coords[0][0]],[cp1.coords[0][1],cp2.coords[0][1]])
                    G.add_node(i*cols+j, center = cp1)
                    G.add_node((i-1)*cols+j+1, center = cp2)
                    G.add_edge(i*cols+j,(i-1)*cols+j+1,weight=edge_len)
                if (i+1<rows) and (j-1>0) and (maze[i+1,j-1]>0):#south-west
                    cp1=center_points[i,j]
                    cp2=center_points[i+1,j-1]
                    edge_len = geod.line_length([cp1.coords[0][0],cp2.coords[0][0]],[cp1.coords[0][1],cp2.coords[0][1]])
                    G.add_node(i*cols+j, center = cp1)
                    G.add_node((i+1)*cols+j-1, center = cp2)
                    G.add_edge(i*cols+j,(i+1)*cols+j-1,weight=edge_len)
                if (i+1<rows) and (j+1<cols) and (maze[i+1,j+1]>0):#south-east
                    cp1=center_points[i,j]
                    cp2=center_points[i+1,j+1]
                    edge_len = geod.line_length([cp1.coords[0][0],cp2.coords[0][0]],[cp1.coords[0][1],cp2.coords[0][1]])
                    G.add_node(i*cols+j, center = cp1)
                    G.add_node((i+1)*cols+j+1, center = cp2)
                    G.add_edge(i*cols+j,(i+1)*cols+j+1,weight=edge_len)
    return G


def build_area_tiles_graph_all_to_all(gdf, tileSize, geod = Geod(ellps="WGS84")):

    xmin,ymin,xmax,ymax =  gdf.total_bounds
    width_m = geod.line_length([xmin,xmax], [ymin,ymin])
    height_m = geod.line_length([xmin,xmin], [ymin,ymax])
    cell_w_m = tileSize # meters
    cols=np.round(width_m/cell_w_m)
    cell_w_deg = (xmax-xmin)/cols
    cell_h_m = tileSize # meters
    rows=np.round(height_m/cell_h_m)
    cell_h_deg = (ymax-ymin)/rows
    XleftOrigin = xmin
    XrightOrigin = xmin + cell_w_deg
    YtopOrigin = ymax
    YbottomOrigin = ymax - cell_h_deg
    cells = []
    intersections = []
    center_points = []
    for i in range(int(cols)):
        Ytop = YtopOrigin
        Ybottom =YbottomOrigin
        for j in range(int(rows)):
            cell_polygon = Polygon([(XleftOrigin, Ytop), (XrightOrigin, Ytop), (XrightOrigin, Ybottom), (XleftOrigin, Ybottom)])
            if shape_intersection(cell_polygon,gdf['geometry'][0]).is_empty:
                cells.append(cell_polygon) 
            intersections.append(int(shape_intersection(cell_polygon,gdf['geometry'][0]).is_empty))
            center_points.append(cell_polygon.centroid)
            Ytop = Ytop - cell_h_deg
            Ybottom = Ybottom - cell_h_deg
            
        XleftOrigin = XleftOrigin + cell_w_deg
        XrightOrigin = XrightOrigin + cell_w_deg

    G = Graph()
    for i in range(len(intersections)):
        if intersections[i]>0:
            for j in range(i+1,len(intersections)):
                if intersections[j]>0:
                    cells_link = LineString([center_points[i],center_points[j]])
                    if shape_intersection(cells_link,gdf['geometry'][0]).is_empty:
                        edge_len = geod.line_length([center_points[i].coords[0][0],center_points[j].coords[0][0]],
                                                    [center_points[i].coords[0][1],center_points[j].coords[0][1]])
                        G.add_node(i, center = center_points[i])
                        G.add_node(j, center = center_points[j])
                        G.add_edge(i,j,weight=edge_len)
    return G


def build_area_graph_by_polygon(gdf, buffer_m, geod = Geod(ellps="WGS84")):

    polygon_points=[]
    xmin,ymin,xmax,ymax =  gdf.total_bounds
    width_m = geod.line_length([xmin,xmax], [ymin,ymin])
    buffer_deg = (xmax-xmin)/(width_m/buffer_m)
    G = Graph()
    buffer_polygon = gdf['geometry'][0].buffer(buffer_deg, cap_style='square', quad_segs=1, mitre_limit=0.000001)

    polygon_points=buffer_polygon.exterior.coords[:-1] # list of coords from buffer to multiPolygon

    for i in range(len(polygon_points)):
        for j in range(i+1,len(polygon_points)):
            link = LineString([polygon_points[i],polygon_points[j]])
            if shape_intersection(link,gdf['geometry'][0]).is_empty:
                edge_len = geod.line_length([polygon_points[i][0],polygon_points[j][0]],
                                            [polygon_points[i][1],polygon_points[j][1]])
                G.add_node(i, center = polygon_points[i])
                G.add_node(j, center = polygon_points[j])
                G.add_edge(i, j, weight = edge_len)
    return G


def find_node_by_coord(G,lat,lon):
    geod = Geod(ellps="WGS84")
    minDist = 999999999999.9
    nodeId = 0
    for i in G.nodes:
        vec = geod.inv(lon,lat,G.nodes[i]['center'].y,G.nodes[i]['center'].x)
        if vec[2] < minDist:
            minDist = vec[2]
            nodeId=i
    return nodeId


def build_astar_path(G, start_node, target_node):
    return astar_path(G, start_node, target_node)

def build_dijkstra_path(G, start_node, target_node):
    return dijkstra_path(G, start_node, target_node)


def build_bellman_ford_path_on_polygon_graph(gdf, buffer_m, G, start, target):
    polygon_points=[]
    geod = Geod(ellps="WGS84")
    xmin,ymin,xmax,ymax =  gdf.total_bounds
    width_m = geod.line_length([xmin,xmax], [ymin,ymin])
    buffer_deg = (xmax-xmin)/(width_m/buffer_m)
    buffer_polygon = gdf['geometry'][0].buffer(buffer_deg,cap_style='square',quad_segs=1,mitre_limit=0.000001)
    polygon_points=buffer_polygon.exterior.coords[:-1] # list of coords from buffer to multiPolygon

    start_id = G.number_of_nodes()+1
    target_id = G.number_of_nodes()+2
    G.add_node(start_id, center = start)
    G.add_node(target_id, center = target)

    for i in range(len(polygon_points)):
        link = LineString([polygon_points[i], start])
        if shape_intersection(link,gdf['geometry'][0]).is_empty:
            edge_len = geod.line_length([polygon_points[i][0],start[0]],
                                        [polygon_points[i][1],start[1]])
            G.add_edge(i, start_id, weight = edge_len)

    for i in range(len(polygon_points)):
        link = LineString([polygon_points[i], target])
        if shape_intersection(link,gdf['geometry'][0]).is_empty:
            edge_len = geod.line_length([polygon_points[i][0],target[0]],
                                        [polygon_points[i][1],target[1]])
            G.add_edge(i, target_id, weight = edge_len)

    path = bellman_ford_path(G, start_id, target_id)
    return path




def build_path_gdf(path, G: Graph):
    line_points = [G.nodes[p]['center'] for p in path]
    line = LineString(line_points)
    path_df = gpd.GeoDataFrame({'area': 'path' ,'geometry' : [line]}, crs='epsg:4326')
    return path_df
