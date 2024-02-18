from ashapi import Config, SimcomplexTask, Events, local_server

from ashapi.math2 import deg2rad, rad2deg, knots2msec, msec2knots, isclose



class EnvironmentSetWindTask(SimcomplexTask):

    def init(self, direction, speed):
        self.wind_direction = direction # deg
        self.wind_speed = speed # knots

    def setup(self):
        wind = self.environment.wind
        print(f"Scene environment wind:")
        print(f"  Direction from: {rad2deg(wind.direction_from):.1f}\u00B0")
        print(f"  Wind speed: {msec2knots(wind.speed):.1f} knots")
        print(f"Setting scene environment wind to:")
        print(f"  Direction from: {self.wind_direction:.1f}\u00B0")
        print(f"  Wind speed: {self.wind_speed:.1f} knots")
        self.on_event(Events.ENVIRONMENT_WIND, self.on_wind_changed)
        wind.set(deg2rad(self.wind_direction), knots2msec(self.wind_speed))


    def on_wind_changed(self, message):
        wind = self.environment.wind
        print(f"Simcomplex responded with scene environment wind:")
        print(f"  Direction from: {rad2deg(wind.direction_from):.1f}\u00B0")
        print(f"  Speed: {msec2knots(wind.speed):.1f} knots")
        self.complete()

    def result(self):
        wind = self.environment.wind
        return isclose(rad2deg(wind.direction_from), self.wind_direction) and isclose(msec2knots(wind.speed), self.wind_speed)



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = EnvironmentSetWindTask(config, 60.0, 10.0)

        result = task.run()

