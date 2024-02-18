from ashapi import Config, SimcomplexTask, Events, local_server


class RouteRemovePointTask(SimcomplexTask):

    def init(self, path, point_idx):
        self.scene_path = path
        self.point_idx = point_idx
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
        print(f"Opened scene contains {len(self.scene.routes)} route(s)")

        for route in self.scene.routes:
            print(f'    "{route.name}", {len(route)} points, uid={route.uid}')
            for p in route:
                nam = f'"{p.name}":'
                geo = f' ({p.geo.lat:.5f}\u00B0, {p.geo.lat:.5f}\u00B0)'
                spd = f' speed={p.velocity:.3f}'
                rad = f' radius={p.radius:.1f}'
                hdg = f' hdg={p.hdg:.1f}\u00B0' if p.hdg is not None else ''
                typ = f' {"NON-STOP" if p.type == 1 else "STOP"}'
                print(f'        {nam:>11}{geo:25s}{spd:15}{rad:15}{hdg:15}{typ}')

        print(f"Now let's remove 4th waypoint on the route:")

        route = self.scene.routes[0]

        route.remove(self.point_idx)

        self.on_event(Events.ROUTE, self.on_route, lambda: not self.done)


    def on_route(self, message):
        print(f"Now scene has {len(self.scene.routes)} route(s):")
        for route in self.scene.routes:
            print(f'    "{route.name}", {len(route)} points, uid={route.uid}')
            for p in route:
                nam = f'"{p.name}":'
                geo = f' ({p.geo.lat:.5f}\u00B0, {p.geo.lat:.5f}\u00B0)'
                spd = f' speed={p.velocity:.3f}'
                rad = f' radius={p.radius:.1f}'
                hdg = f' hdg={p.hdg:.1f}\u00B0' if p.hdg is not None else ''
                typ = f' {"NON-STOP" if p.type == 1 else "STOP"}'
                print(f'        {nam:>11}{geo:25s}{spd:15}{rad:15}{hdg:15}{typ}')
        self.done = True
        self.complete()

    def result(self):
        return self.done



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        point_idx_to_remove = 3

        task = RouteRemovePointTask(config, "api/routes/route_01.stexc", point_idx_to_remove)

        result = task.run()

