import geopandas as gpd
import os.path

from ashapi import Config, SimcomplexTask, Events, local_server
from ashapi.math2 import deg2rad

from ashapipro.routes.areautil import area_xmltree, extract_area_multipoligons

from ashapipro.routes.graph import build_area_tiles_graph_all_to_all, find_node_by_coord, build_dijkstra_path, build_path_gdf



class BuildDijkstraPathOnAreaAllToAllGraphTask(SimcomplexTask):

    def init(self, path, start, target):
        self.scene_path = path
        self.start = start
        self.target = target
        self.area_name = 'RU_NVS'
        self.map_name = 'RU6MELN0.xml'
        self.map_data = None
        self.done = False

    def setup(self):
        print(f"Opening scene containing Novorossisk area: '{self.scene_path}'")
        self.scene.clear()
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )

    def on_scene_opened(self, response):
        print(f"Opened scene: '{self.scene_path}'")
        print(f"Request area '{self.area_name}' '{self.map_name}' map...")
        self.content.request_area_map(self.area_name, self.map_name, self.on_map_received)


    def on_map_received(self, map_xml):

        print(f"Received '{self.map_name}.xml' data...")

        self.map_data = map_xml

        xtree = area_xmltree(xml=map_xml)

        lndare = extract_area_multipoligons(xtree, 'LNDARE')

        print(f"Extracted {len(lndare.geoms)} polygons from area map data.")

        print(f"Build all-to-all graph on area polygon... (WARNING! may take a lot of time > 2h)")

        gdf = gpd.GeoDataFrame({'area': 'LNDARE' ,'geometry' : [lndare]}, crs='epsg:4326')

        all_to_all_graph = build_area_tiles_graph_all_to_all(gdf, 150)

        ## Load cached all-to-all graph
        # print(f"Load precalculated all-to-all graph with tile size 25 meters...")
        # graph_cache_file = os.path.normpath(os.path.join(os.path.dirname(__file__), "..\\..\\..\\tests\\data\\routes\\Graph25meters.pickle"))
        # import pickle
        # all_to_all_graph = pickle.load(open(graph_cache_file, 'rb'))

        print(f"All-to-all graph: {len(all_to_all_graph.nodes)}  nodes, {len(all_to_all_graph.edges)} edges.")

        print(f"Build dijkstra path from {self.start} to {self.target} based on graph...")

        start_node = find_node_by_coord(all_to_all_graph, *self.start)
        target_node = find_node_by_coord(all_to_all_graph, *self.target)

        path = build_dijkstra_path(all_to_all_graph, start_node, target_node)
        dijkstra_path_df = build_path_gdf(path, all_to_all_graph)

        coords = dijkstra_path_df.geometry[0].coords

        print(f"Path of {len(coords)} points has been built...")

        print(f"Add route to simcomplex:")

        points = [[deg2rad(c[1]), deg2rad(c[0])] for c in coords]
        self.scene.routes.add("Dijkstra Path All-to-All Graph", points)
        self.on_event(Events.ROUTE, self.on_route_added, lambda: not self.done)


    def on_route_added(self, message):
        if self.scene.routes:
            print(f"Now scene has {len(self.scene.routes)} route(s):")
            for r in self.scene.routes:
                print(f"    {r.uid}: {r.name}, '{len(r)}' points")
            self.done = True
            self.complete()

    def result(self):
        return self.done



if __name__ == '__main__':

    config = Config.localhost()

    start = (37.815158, 44.720084)
    target = (37.785410, 44.730714)

    with local_server(config):

        task = BuildDijkstraPathOnAreaAllToAllGraphTask(config, "api/empty_nv.stexc", start, target)

        result = task.run()

