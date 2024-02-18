import geopandas as gpd


from ashapi import Config, SimcomplexTask, Events, local_server
from ashapi.math2 import deg2rad

from ashapipro.routes.areautil import area_xmltree, extract_area_multipoligons

from ashapipro.routes.graph import build_area_graph_by_polygon, build_bellman_ford_path_on_polygon_graph, build_path_gdf



class BuildBellmanFordPathOnAreaPolygonGraphTask(SimcomplexTask):

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

        print(f"Build polygon-based-graph on area polygon... (may take a while)")

        gdf = gpd.GeoDataFrame({'area': 'LNDARE' ,'geometry' : [lndare]}, crs='epsg:4326')
        polygon_graph = build_area_graph_by_polygon(gdf, 25.0)

        print(f"Polygon-based-graph: {len(polygon_graph.nodes)}  nodes, {len(polygon_graph.edges)} edges.")

        print(f"Build path from {self.start} to {self.target} based on graph...")

        path = build_bellman_ford_path_on_polygon_graph(gdf, 25.0, polygon_graph, self.start, self.target)
        bellman_ford_path_df = build_path_gdf(path, polygon_graph)
        coords = bellman_ford_path_df.geometry[0].coords

        print(f"Path of {len(coords)} points has been built...")

        print(f"Add route to simcomplex:")

        points = [[deg2rad(c[1]), deg2rad(c[0])] for c in coords]
        self.scene.routes.add("Bellman-Ford Path", points)
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

        task = BuildBellmanFordPathOnAreaPolygonGraphTask(config, "api/empty_nv.stexc", start, target)

        result = task.run()

