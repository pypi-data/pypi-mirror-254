
from ashapi import Config, SimcomplexTask, Events, local_server



class RemoveRouteTask(SimcomplexTask):

    def init(self, path, route_idx):
        self.scene_path = path
        self.route_idx = route_idx
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
        for r in self.scene.routes:
            print(f"    {r.uid}: {r.name}, '{len(r)}' points")

        print(f"Now let's remove route # {self.route_idx+1}:")

        route = self.scene.routes[self.route_idx]

        self.scene.routes.remove(route)

        self.on_event(Events.ROUTE_REMOVED, self.on_route_removed, lambda: not self.done)


    def on_route_removed(self, message):
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

    with local_server(config):

        route_to_remove = 1

        task = RemoveRouteTask(config, "api/all_models_nv.stexc", route_to_remove)

        result = task.run()

