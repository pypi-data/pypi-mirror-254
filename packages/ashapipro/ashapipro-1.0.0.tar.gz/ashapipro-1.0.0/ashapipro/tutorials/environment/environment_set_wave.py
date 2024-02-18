from ashapi import Config, SimcomplexTask, Events, local_server

from ashapi.math2 import deg2rad, rad2deg, knots2msec, msec2knots


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


class EnvironmentSetWaveTask(SimcomplexTask):


    def init(self):
        self.direction = 90 # deg
        self.wind_speed = 10 # knots
        self.height = 2 # m
        self.length = 50 # m
        self.spread = 30 # deg
        self.nf = 13
        self.nd = 15
        self.curr_wind = None
        self.curr_height = None
        self.curr_length = None
        self.done = False


    def set_wave_by_wind_speed(self):

        wave = self.environment.wave

        print(f"Setting scene environment wave to:")
        print(f"  Direction to: {self.direction:.1f}\u00B0")
        print(f"  Wind speed: {self.wind_speed:.1f} knots")
        print(f"  Direction spread: {self.spread:.1f}\u00B0")
        print(f"  Num frequencies: {self.nf}")
        print(f"  Num direction components: {self.nd}")

        self.on_event(Events.ENVIRONMENT_WAVE, self.on_wave_changed, persist=lambda: not self.done)

        self.curr_wind = knots2msec(self.wind_speed)
        self.curr_height = wave.typical_height
        self.curr_length = wave.typical_length

        wave.set(direction_to = deg2rad(self.direction),
                 wind_speed = knots2msec(self.wind_speed),
                 direction_spread = deg2rad(self.spread),
                 number_of_frequencies = self.nf,
                 number_of_directions = self.nd)


    def set_wave_by_height(self):

        wave = self.environment.wave

        print(f"Setting scene environment wave to:")
        print(f"  Direction to: {self.direction:.1f}\u00B0")
        print(f"  Typical height: {self.height:.1f} m")
        print(f"  Direction spread: {self.spread:.1f}\u00B0")
        print(f"  Num frequencies: {self.nf}")
        print(f"  Num direction components: {self.nd}")

        self.on_event(Events.ENVIRONMENT_WAVE, self.on_wave_changed, persist=lambda: not self.done)

        self.curr_wind = wave.wind_speed
        self.curr_height = self.height
        self.curr_length = wave.typical_length

        wave.set(direction_to = deg2rad(self.direction),
                 typical_height = self.height,
                 direction_spread = deg2rad(self.spread),
                 number_of_frequencies = self.nf,
                 number_of_directions = self.nd)


    def set_wave_by_length(self):

        wave = self.environment.wave

        print(f"Setting scene environment wave to:")
        print(f"  Direction to: {self.direction:.1f}\u00B0")
        print(f"  Typical length: {self.length:.1f} m")
        print(f"  Direction spread: {self.spread:.1f}\u00B0")
        print(f"  Num frequencies: {self.nf}")
        print(f"  Num direction components: {self.nd}")

        self.on_event(Events.ENVIRONMENT_WAVE, self.on_wave_changed, persist=lambda: not self.done)

        self.curr_wind = wave.wind_speed
        self.curr_height = wave.typical_height
        self.curr_length = self.length

        wave.set(direction_to = deg2rad(self.direction),
                 typical_length = self.length,
                 direction_spread = deg2rad(self.spread),
                 number_of_frequencies = self.nf,
                 number_of_directions = self.nd)



    def on_wave_changed(self, message):
        wave = self.environment.wave
        # print(f"wind: {wave.wind_speed} <-> {self.curr_wind} | height: {wave.typical_height} <-> {self.curr_height} | length: {wave.typical_length} <-> {self.curr_length}")
        if wave.wind_speed != self.curr_wind or wave.typical_height != self.curr_height or wave.typical_length != self.curr_length:
            self.done = True
            report_wave(wave, "Simcomplex responded with scene environment wave:")
            self.complete()


class EnvironmentSetWaveWindTask(EnvironmentSetWaveTask):

    def setup(self):
        report_wave(self.environment.wave, "Current scene environment wave parameters:")
        self.set_wave_by_wind_speed()


class EnvironmentSetWaveHeightTask(EnvironmentSetWaveTask):

    def setup(self):
        report_wave(self.environment.wave, "Current scene environment wave parameters:")
        self.set_wave_by_height()


class EnvironmentSetWaveLengthTask(EnvironmentSetWaveTask):

    def setup(self):
        report_wave(self.environment.wave, "Current scene environment wave parameters:")
        self.set_wave_by_length()



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = EnvironmentSetWaveWindTask(config)

        result = task.run()

        task = EnvironmentSetWaveHeightTask(config)

        result = task.run()

        task = EnvironmentSetWaveLengthTask(config)

        result = task.run()


