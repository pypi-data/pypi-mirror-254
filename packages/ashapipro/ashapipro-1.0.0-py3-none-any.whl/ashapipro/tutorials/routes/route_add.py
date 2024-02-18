
from ashapi import Config, SimcomplexTask, Events, local_server


class AddRouteTask(SimcomplexTask):

    def init(self, path):
        self.scene_path = path
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
        print(f"Now let's add some new route to the scene:")

        points = [
            [0.78059841735038,   0.6595292708678948],
            [0.7806435609656948, 0.6596289412962438],
            [0.7806108099163716, 0.6597198905621122],
            [0.7805305506012377, 0.6596962188353793],
            [0.7805034026243378, 0.6597311034853016],
            [0.7805034026243378, 0.6597311034853016]
        ]

        self.scene.routes.add("Test route", points)

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

    with local_server(config):

        task = AddRouteTask(config, "api/empty_nv.stexc")

        result = task.run()

