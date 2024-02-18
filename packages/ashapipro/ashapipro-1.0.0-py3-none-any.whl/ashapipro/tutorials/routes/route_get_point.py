
from ashapi import Config, SimcomplexTask, local_server


class RouteGetPointTask(SimcomplexTask):

    def init(self, path):
        self.scene_path = path

    def setup(self):
        self.done = False
        print(f"Opening scene '{self.scene_path}'")
        self.scene.clear()
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )

    def on_scene_opened(self, response):
        print(f"Opened scene: '{self.scene_path}'")
        print(f"Opened scene contains {len(self.scene.routes)} route(s)")
        route = self.scene.routes[0]
        print(f'First route "{route.name}" has {len(route)} points')
        n = 2
        p = route[n-1]
        deg = "\u00B0"
        print(f'Point №{n} has following properties:')
        print(f'    Name: "{p.name}":')
        print(f'    Geolocation (lat, lon): ({p.geo.lat:.5f}\u00B0, {p.geo.lat:.5f}\u00B0)')
        print(f'    Target speed: {p.velocity} (m/s)')
        print(f'    Radius: {p.radius} (m)')
        print(f'    Heading: {p.hdg if p.hdg is not None else "Not defined"}{deg if p.hdg is not None else ""}')
        print(f'    Type: {"NON-STOP" if p.type == 1 else "STOP"}')
        n = 12
        p = route[n-1]
        print(f'Point №{n} has following properties:')
        print(f'    Name: "{p.name}":')
        print(f'    Geolocation (lat, lon): ({p.geo.lat:.5f}\u00B0, {p.geo.lat:.5f}\u00B0)')
        print(f'    Target speed: {p.velocity} (m/s)')
        print(f'    Radius: {p.radius} (m)')
        print(f'    Heading: {p.hdg if p.hdg is not None else "Not defined"}{deg if p.hdg is not None else ""}')
        print(f'    Type: {"NON-STOP" if p.type == 1 else "STOP"}')
        self.done = self.scene.path == self.scene_path
        self.complete()

    def result(self):
        return self.done


if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = RouteGetPointTask(config, "api/all_models_nv.stexc")

        result = task.run()
