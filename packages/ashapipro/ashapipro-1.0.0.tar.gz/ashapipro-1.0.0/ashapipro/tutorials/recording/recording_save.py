from ashapi import Config, SimcomplexTask, Events, local_server


import math


class OpenSceneRunThenSaveRecordingTask(SimcomplexTask):

    def init(self, scene: str, duration: float, saveto: str):
        self.scene_path = scene
        self.duration = duration
        self.recording_path = saveto
        self.done = False


    def setup(self):
        print(f"Opening scene '{self.scene_path}'")
        self.scene.clear()
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )


    def on_scene_opened(self, response):
        print(f"Opened scene: '{self.recording_path}'")
        print(f"Run simulation for {self.duration} seconds at max speed:")
        self.simulation.maxaccel() # maxaccel is request
        # self.simulation.setaccel(5)
        # self.simulation.run_for(self.duration, end_action=self.save_recording)
        self.on_event(Events.SIMULATION_STATE, self.await_duration, lambda: not self.done)
        self.simulation.run()


    def await_duration(self, message,
                       _close = math.isclose,
                       _round = round):
        time = self.simulation.time
        if time >= self.duration:
            self.done = True
            self.save_recording()
        elif _close(time, _round(time)):
            print(f"Time: {self.simulation.time:.1f}")


    def save_recording(self):
        print(f"Saving recording to: {self.recording_path}")
        self.simulation.setaccel(1)
        self.simulation.pause()
        self.scene.save_recording(
            self.recording_path,
            self.on_recording_saved
        )


    def on_recording_saved(self, response):
        print(f"Recording saved response: {response}")
        print(f"Saved recording to: '{self.recording_path}'")
        self.content.request_recordings(
            self.check_content_recordings
        )


    def check_content_recordings(self, response):
        if f"{self.recording_path}.strec" in self.content.recordings:
            print("Recording has been successfully saved and now available in simcomplex content. Happy ashcoding!")
        self.complete()



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = OpenSceneRunThenSaveRecordingTask(config,
                                             scene = "api/objects/misv01_full_throttle_01.stexc",
                                             duration = 20,
                                             saveto = "api/recordings/saved_recording")

        result = task.run()
