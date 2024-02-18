from ashapi import Config, SimcomplexTask, local_server

from ashapi.math2 import rad2deg, msec2knots


class EnvironmentGetCurrentTask(SimcomplexTask):

    def init(self, path):
        self.scene_path = path

    def setup(self):
        current = self.environment.current
        print(f"Scene environment current:")
        print(f"  Direction to: {rad2deg(current.direction_to):.1f}\u00B0")
        print(f"  Speed: {msec2knots(current.speed):.1f} knots")
        print(f"Load another scene with different environment conditions:")
        print(f"Opening scene '{self.scene_path}'")
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )

    def on_scene_opened(self, response):
        print(f"Opened scene: '{self.scene_path}'")
        current = self.environment.current
        print(f"Opened scene has following environment current:")
        print(f"  Direction to: {rad2deg(current.direction_to):.1f}\u00B0")
        print(f"  Speed: {msec2knots(current.speed):.1f} knots")
        self.complete()


if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = EnvironmentGetCurrentTask(config, 'api/environment/environment_conditions.stexc')

        result = task.run()

