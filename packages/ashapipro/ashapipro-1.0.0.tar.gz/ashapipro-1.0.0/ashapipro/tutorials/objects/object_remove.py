
from ashapi import Config, SimcomplexTask, Events, local_server



class RemoveObjectTask(SimcomplexTask):

    def init(self, path):
        self.scene_path = path
        self.done = False

    def setup(self):
        print(f"Opening scene '{self.scene_path}'")
        self.scene.clear()
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )

    def on_scene_opened(self, response):

        print(f"Opened scene: '{self.scene_path}'")

        print(f"Opened scene contains {len(self.scene.objects)} object(s):")

        for o in self.scene.objects:
            print(f'{o.uid}: "{o.code}", "{o.name}"')

        code = 'misv01'

        print(f"Now let's remove first {code} from the scene:")

        o = self.scene.objects[code]
        self.scene.objects.remove(o)

        self.on_event(Events.OBJECT_REMOVED, self.on_object_removed, lambda: not self.done)


    def on_object_removed(self, msg):
        print(f"Now scene contains {len(self.scene.objects)} object(s):")
        for o in self.scene.objects:
            print(f'{o.uid}: "{o.code}", "{o.name}"')
        self.done = True
        self.complete()

    def result(self):
        return self.done



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = RemoveObjectTask(config, "api/all_models_nv.stexc")

        result = task.run()

