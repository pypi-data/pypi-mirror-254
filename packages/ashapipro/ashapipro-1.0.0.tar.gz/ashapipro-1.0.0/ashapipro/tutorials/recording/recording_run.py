
from ashapi import Config, SimcomplexTask, Events, local_server


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


class RecordingRunTask(SimcomplexTask):

    def init(self, path):
        self.recording_path = path

    def setup(self):
        self.done = False
        print(f"Opening recording '{self.recording_path}'")
        self.scene.clear()
        self.scene.open(
            self.recording_path,
            self.run_recording
        )

    def run_recording(self, message):
        sim = self.simulation
        report_simstate(sim, f"Current playback state:")
        print(f"Run recording:")
        self.ticks = sim.ticks
        self.target_time = sim.time + 1.0 # will run for 1 second
        self.done = False
        self.on_event(Events.SIMULATION_STATE, self.on_sim_state, lambda: not self.done)
        sim.run()

    def on_sim_state(self, message):
        sim = self.simulation
        if sim.ticks > self.ticks:
            self.ticks = sim.ticks
            report_simstate(sim)
            if sim.time > self.target_time:
                self.done = True
                self.complete()

    def result(self):
        return self.done



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = RecordingRunTask(config, 'api/recordings/misv01_accelerating_01.strec')

        result = task.run()
