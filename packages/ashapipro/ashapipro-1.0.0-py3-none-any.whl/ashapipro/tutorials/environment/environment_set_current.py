from ashapi import Config, SimcomplexTask, Events, local_server

from ashapi.math2 import deg2rad, rad2deg, knots2msec, msec2knots, isclose


class EnvironmentSetCurrentTask(SimcomplexTask):

    def init(self, direction, speed):
        self.current_direction = direction # deg
        self.current_speed = speed # knots

    def setup(self):
        current = self.environment.current
        print(f"Scene environment current:")
        print(f"  Direction to: {rad2deg(current.direction_to):.1f}\u00B0")
        print(f"  Speed: {msec2knots(current.speed):.1f} knots")
        print(f"Setting scene environment current to:")
        print(f"  Direction to: {self.current_direction:.1f}\u00B0")
        print(f"  Speed: {self.current_speed:.1f} knots")
        self.on_event(Events.ENVIRONMENT_CURRENT, self.on_current_changed)
        current.set(deg2rad(self.current_direction), knots2msec(self.current_speed))


    def on_current_changed(self, message):
        current = self.environment.current
        print(f"Simcomplex responded with scene environment current:")
        print(f"  Direction to: {rad2deg(current.direction_to):.1f}\u00B0")
        print(f"  Speed: {msec2knots(current.speed):.1f} knots")
        self.complete()

    def result(self):
        current = self.environment.current
        return isclose(rad2deg(current.direction_to), self.current_direction) and isclose(msec2knots(current.speed), self.current_speed)



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = EnvironmentSetCurrentTask(config, 30.0, 5.0)

        result = task.run()
