from conftest import get_data_path

import geopandas as gpd
import pickle

from ashapipro.routes.areautil import area_xmltree, extract_area_multipoligons

from ashapipro.routes import graph



def test_build_a_star_path(capsys):

    with capsys.disabled():

        print(f"Extract polygons from area map data...")

        map_file = get_data_path("routes\\RU6MELN0.xml")

        axmltree = area_xmltree(filepath=map_file)
        lndare = extract_area_multipoligons(axmltree,'LNDARE')

        print(f"Extracted {len(lndare.geoms)} polygons from area map data.")

        assert len(lndare.geoms) == 8

        print(f"Built area polygon pandas data frame...")

        gdf = gpd.GeoDataFrame({'area': 'LNDARE' ,'geometry' : [lndare]}, crs='epsg:4326')

        # Uncomment this to generate html area polygon over map picture:

        # m = gdf.explore()
        # m.save(get_data_path("routes\\_area_polygon_map.html"))

        print(f"Build 8-Neigbhours-based-graph on area polygon... (may take a while)")

        neighbors_graph = graph.build_area_tiles_graph_by_neighbors(gdf, 25.0)

        print(f"8-Neigbhours-based-graph: {len(neighbors_graph.nodes)}  nodes, {len(neighbors_graph.edges)} edges.")

        start = (37.815158, 44.720084)
        target = (37.785410, 44.730714)

        print(f"Build path from {start} to {target} based on graph...")

        start_node = graph.find_node_by_coord(neighbors_graph, *start)
        target_node = graph.find_node_by_coord(neighbors_graph, *target)

        # path with A*
        path = graph.build_astar_path(neighbors_graph, start_node, target_node)
        A_star_path_df = graph.build_path_gdf(path, neighbors_graph)

        # Uncomment this to generate html containing path over area picture:

        # m = A_star_path_df.explore()
        # m.save(get_data_path("routes\\_a_star_path_map.html"))

        coords = A_star_path_df.geometry[0].coords

        print(f"Path of {len(coords)} wayponts has been built!")

        assert len(coords) == 95


def test_build_dijkstra_path(capsys):

    with capsys.disabled():

        print(f"Extract polygons from area map data...")

        map_file = get_data_path("routes\\RU6MELN0.xml")

        axmltree = area_xmltree(filepath=map_file)
        lndare = extract_area_multipoligons(axmltree,'LNDARE')

        print(f"Extracted {len(lndare.geoms)} polygons from area map data.")

        assert len(lndare.geoms) == 8

        print(f"Built area polygon pandas data frame...")

        gdf = gpd.GeoDataFrame({'area': 'LNDARE' ,'geometry' : [lndare]}, crs='epsg:4326')

        use_cached_graph = True # Set False to build graph during test. # WARNING! may take a lot of time (> 2h)
        all_to_all_graph = None

        if use_cached_graph:
            print(f"Load precalculated all-to-all graph with tile size 25 meters...")
            graph_cache_file = get_data_path("routes\\Graph25meters.pickle")
            all_to_all_graph = pickle.load(open(graph_cache_file, 'rb'))
        else:
            print(f"Build all-to-all graph on area polygon... (WARNING! may take a lot of time > 2h)")
            all_to_all_graph = graph.build_area_tiles_graph_all_to_all(gdf, 150)

        print(f"All-to-all graph: {len(all_to_all_graph.nodes)}  nodes, {len(all_to_all_graph.edges)} edges.")

        start = (37.815158, 44.720084)
        target = (37.785410, 44.730714)

        print(f"Build dijkstra path from {start} to {target} based on graph...")

        start_node = graph.find_node_by_coord(all_to_all_graph, *start) #  37.815158, 44.720084)
        target_node = graph.find_node_by_coord(all_to_all_graph, *target) # 37.785410, 44.730714)

        path = graph.build_dijkstra_path(all_to_all_graph, start_node, target_node)
        dijkstra_path_df = graph.build_path_gdf(path, all_to_all_graph)

        # Uncomment this to generate html containing path over area picture:

        # m = dijkstra_path_df.explore()
        # m.save(get_data_path("routes\\_dijkstra_path_map.html"))

        coords = dijkstra_path_df.geometry[0].coords

        print(f"Path of {len(coords)} wayponts has been built!")

        assert len(coords) == 4


def test_build_bellman_ford_path(capsys):

    with capsys.disabled():

        print(f"Extract polygons from area map data...")

        map_file = get_data_path("routes\\RU6MELN0.xml")

        axmltree = area_xmltree(filepath=map_file)
        lndare = extract_area_multipoligons(axmltree,'LNDARE')

        print(f"Extracted {len(lndare.geoms)} polygons from area map data.")

        assert len(lndare.geoms) == 8

        print(f"Built area polygon pandas data frame...")

        gdf = gpd.GeoDataFrame({'area': 'LNDARE' ,'geometry' : [lndare]}, crs='epsg:4326')

        print(f"Build polygon-based-graph on area polygon... (may take a while)")

        polygon_graph = graph.build_area_graph_by_polygon(gdf, 25.0)

        print(f"Polygon-based-graph: {len(polygon_graph.nodes)}  nodes, {len(polygon_graph.edges)} edges.")

        start = (37.815158,44.720084)
        target = (37.785410,44.730714)

        print(f"Build path from {start} to {target} based on graph...")

        path = graph.build_bellman_ford_path_on_polygon_graph(gdf, 25.0, polygon_graph, start, target)
        bellman_ford_path_df = graph.build_path_gdf(path, polygon_graph)

        # Uncomment this to generate html containing path over area picture:

        # m = bellman_ford_path_df.explore()
        # m.save(get_data_path("routes\\_bellman_ford_path_map.html"))

        coords = bellman_ford_path_df.geometry[0].coords

        print(f"Path of {len(coords)} wayponts has been built!")

        assert len(coords) == 4
