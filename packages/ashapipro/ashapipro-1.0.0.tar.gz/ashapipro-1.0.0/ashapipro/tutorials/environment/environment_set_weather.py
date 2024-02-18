
from ashapi import Config, SimcomplexTask, Events, local_server

from ashapi.environment import WeatherPresets


class EnvironmentSetWeatherTask(SimcomplexTask):

    def init(self, preset):
        self.preset = preset

    def setup(self):
        wp = self.environment.weather_preset
        print(f"Scene environment weather preset: {WeatherPresets(wp).name}")
        print(f"Setting scene environment weather preset to: {WeatherPresets(self.preset).name}")
        self.on_event(Events.ENVIRONMENT_WEATHER_PRESET, self.on_weather_changed)
        self.environment.weather_preset = self.preset

    def on_weather_changed(self, message):
        print(f"Simcomplex responded with scene environment weather preset: {WeatherPresets(self.environment.weather_preset).name}")
        self.complete()

    def result(self):
        return self.environment.weather_preset == self.preset



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = EnvironmentSetWeatherTask(config, WeatherPresets.Rain)

        task.run()
