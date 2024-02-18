
from ashapi import Config, SimcomplexTask, local_server

from ashapi.environment import WeatherPresets


class EnvironmentGetWeatherTask(SimcomplexTask):

    def init(self, path):
        self.scene_path = path

    def setup(self):
        wp = self.environment.weather_preset
        print(f"Scene environment weather preset: {WeatherPresets(wp).name}")
        print(f"Load another scene with different environment conditions:")
        print(f"Opening scene '{self.scene_path}'")
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )

    def on_scene_opened(self, response):
        print(f"Opened scene: '{self.scene_path}'")
        wp = self.environment.weather_preset
        print(f"Opened scene environment weather preset: {WeatherPresets(wp).name}")
        self.complete()



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = EnvironmentGetWeatherTask(config, 'api/environment/environment_conditions.stexc')

        task.run()

