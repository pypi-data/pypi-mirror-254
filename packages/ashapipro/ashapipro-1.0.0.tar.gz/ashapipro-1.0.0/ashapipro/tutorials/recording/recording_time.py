from ashapi import Config, SimcomplexTask, local_server


def report_simstate(sim, caption="", perf=False):
    if caption:
        print(caption)
    state = 'Running' if sim.is_running else 'Paused'
    recording = ' (Recording)' if sim.is_recording else ''
    playback = ' (Playback)' if sim.is_playback else ''
    timings = f"{sim.time:.2f} seconds, {sim.ticks} ticks, {sim.time_total:.2f} seconds (total)"
    print(f"  {state}{recording}{playback}: {timings}")
    if perf:
        print(f"  Speed/Performance: {sim.time_ratio:.3f} time sim/real ratio, x{sim.accel:.2f}{' (max)' if sim.is_maxaccel else ''}")


class RecordingJumpTimeTask(SimcomplexTask):

    def init(self, path, time):
        self.recording_path = path
        self.time = time

    def setup(self):
        self.done = False
        print(f"Opening recording '{self.recording_path}'")
        self.scene.clear()
        self.scene.open(
            self.recording_path,
            self.set_recording_time
        )

    def set_recording_time(self, message):
        sim = self.simulation
        report_simstate(sim, f"Current playback state:")
        print(f"Jump playback to timestamp {self.time:.1f} (sec):")
        sim.seek(self.time, self.on_time)

    def on_time(self, message):
        # print(message)
        sim = self.simulation
        report_simstate(sim, f"Current playback state:")
        self.complete()



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = RecordingJumpTimeTask(config, 'api/recordings/misv01_accelerating_01.strec', 20.0)

        result = task.run()


