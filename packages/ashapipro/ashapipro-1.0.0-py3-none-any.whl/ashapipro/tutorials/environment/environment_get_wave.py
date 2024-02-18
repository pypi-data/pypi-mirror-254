from ashapi import Config, SimcomplexTask, local_server

from ashapi.math2 import rad2deg, msec2knots


def report_wave(wave, caption=""):
    if caption:
        print(caption)
    print(f"  Direction to: {rad2deg(wave.direction_to):.1f}\u00B0")
    print(f"  Wind speed: {msec2knots(wave.wind_speed):.1f} knots")
    print(f"  Typical height: {wave.typical_height:.1f} m")
    print(f"  Typical length: {wave.typical_length:.1f} m")
    print(f"  Direction spread: {rad2deg(wave.direction_spread):.1f}\u00B0")
    print(f"  Num frequencies: {wave.number_of_frequencies}")
    print(f"  Num direction components: {wave.number_of_directions}")



class EnvironmentGetWaveTask(SimcomplexTask):

    def init(self, path):
        self.scene_path = path

    def setup(self):
        report_wave(self.environment.wave, "Scene environment wave parameters:")
        print(f"Load another scene with different environment conditions:")
        print(f"Opening scene '{self.scene_path}'")
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )

    def on_scene_opened(self, response):
        print(f"Opened scene: '{self.scene_path}'")
        report_wave(self.environment.wave, "Opened scene has following environment wave parameters:")
        self.complete()



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = EnvironmentGetWaveTask(config, 'api/environment/environment_conditions.stexc')

        task.run()

