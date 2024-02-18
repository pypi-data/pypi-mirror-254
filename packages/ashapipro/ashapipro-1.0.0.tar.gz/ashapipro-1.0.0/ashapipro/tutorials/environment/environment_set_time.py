
from ashapi import Config, SimcomplexTask, Events, local_server

from datetime import datetime



class EnvironmentSetTimeTask(SimcomplexTask):

    time = datetime(2025, 6, 23, 4, 32, 55)

    def setup(self):
        dt = self.environment.datetime
        print(f"Current scene environment time: {dt}")
        print(f"Setting scene environment time to: {self.time}")
        self.on_event(Events.ENVIRONMENT_TIME, self.on_time_changed)
        self.environment.time = self.time.timestamp()

    def on_time_changed(self, message):
        print(f"Simcomplex responded with scene environment time: {self.environment.datetime}")
        self.complete()

    def result(self):
        return self.environment.datetime == self.time



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = EnvironmentSetTimeTask(config)

        result = task.run()


