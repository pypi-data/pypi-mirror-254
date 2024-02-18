
from ashapi import Config, SimcomplexTask, local_server


class NewSceneTask(SimcomplexTask):

    def init(self, name: str):
        self.scene_name = name

    def setup(self):
        print("Creating new empty scene")
        self.scene.clear()
        self.scene.new_path(self.scene_name,
                            self.on_scene_created)

    def on_scene_created(self, response):
        print(f"Created new empty scene with name: '{self.scene.path}'")
        self.complete()

    def result(self):
        return self.scene.path


if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = NewSceneTask(config, "my_new_scene")

        result = task.run()
