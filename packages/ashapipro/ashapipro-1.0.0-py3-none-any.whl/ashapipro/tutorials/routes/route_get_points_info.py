
from ashapi import Config, SimcomplexTask, local_server


class RoutePointsInfoTask(SimcomplexTask):

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
        if self.scene.routes:
            print("Routes:")
            for route in self.scene.routes:
                print(f'    "{route.name}", {len(route)} points, uid={route.uid}')
                for p in route:
                    nam = f'"{p.name}":'
                    geo = f' ({p.geo.lat:.5f}\u00B0, {p.geo.lat:.5f}\u00B0)'
                    spd = f' speed={p.velocity}'
                    rad = f' radius={p.radius}'
                    hdg = f' hdg={p.hdg}\u00B0' if p.hdg is not None else ''
                    typ = f' {"NON-STOP" if p.type == 1 else "STOP"}'
                    print(f'        {nam:>10}{geo:30s}{spd:15}{rad:15}{hdg:15}{typ}')
        self.done = self.scene.path == self.scene_path
        self.complete()

    def result(self):
        return self.done



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = RoutePointsInfoTask(config, "api/all_models_nv.stexc")

        result = task.run()
