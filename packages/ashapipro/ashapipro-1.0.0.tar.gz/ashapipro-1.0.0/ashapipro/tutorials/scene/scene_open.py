
from ashapi import Config, SimcomplexTask, local_server


class OpenSceneTask(SimcomplexTask):

    def init(self, path):
        self.scene_path = path

    def setup(self):
        self.done = False
        print(f"Opening scene '{self.scene_path}'")
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )

    def on_scene_opened(self, response):
        print(f"Opened scene: '{self.scene_path}'")
        print(f"Opened scene contains {len(self.scene.objects)} object(s), {len(self.scene.routes)} route(s)")
        if self.scene.objects:
            print("Objects:")
            for o in self.scene.objects:
                print(f'    {o.uid}: {o.code}, "{o.name}"')
        if self.scene.routes:
            print("Routes:")
            for r in self.scene.routes:
                print(f"    {r.uid}: {r.name}, '{len(r)}' points")
        self.done = self.scene.path == self.scene_path
        self.complete()

    def result(self):
        return self.done



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = OpenSceneTask(config, "api/objects/misv01_01.stexc")

        result = task.run()

