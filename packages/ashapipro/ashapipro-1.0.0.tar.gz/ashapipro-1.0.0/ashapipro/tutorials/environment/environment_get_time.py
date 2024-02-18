
from ashapi import Config, SimcomplexTask, local_server



class EnvironmentGetTimeTask(SimcomplexTask):

    def init(self, path):
        self.scene_path = path

    def setup(self):
        dt = self.environment.datetime
        print(f"Scene environment time: {dt}")
        print(f"Load another scene with different environment time:")
        print(f"Opening scene '{self.scene_path}'")
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )

    def on_scene_opened(self, response):
        print(f"Opened scene: '{self.scene_path}'")
        dt = self.environment.datetime
        print(f"Opened scene has following environment time: {dt}")
        self.complete()



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = EnvironmentGetTimeTask(config, 'api/environment/environment_conditions.stexc')

        result = task.run()

