from ashapi import Config, SimcomplexTask, local_server

from ashapi.math2 import rad2deg, msec2knots


class EnvironmentGetWindTask(SimcomplexTask):

    def init(self, path):
        self.scene_path = path

    def setup(self):
        wind = self.environment.wind
        print(f"Scene environment wind:")
        print(f"  Direction from: {rad2deg(wind.direction_from):.1f}\u00B0")
        print(f"  Wind speed: {msec2knots(wind.speed):.1f} knots")
        print(f"Load another scene with different environment conditions:")
        print(f"Opening scene '{self.scene_path}'")
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )

    def on_scene_opened(self, response):
        print(f"Opened scene: '{self.scene_path}'")
        wind = self.environment.wind
        print(f"Opened scene has following environment wind:")
        print(f"  Direction from: {rad2deg(wind.direction_from):.1f}\u00B0")
        print(f"  Wind speed: {msec2knots(wind.speed):.1f} knots")
        self.complete()



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = EnvironmentGetWindTask(config, 'api/environment/environment_conditions.stexc')

        result = task.run()

