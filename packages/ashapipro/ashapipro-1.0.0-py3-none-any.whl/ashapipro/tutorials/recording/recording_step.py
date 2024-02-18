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



class RecordingStepTask(SimcomplexTask):

    def init(self, path, num_steps_to_do):
        self.recording_path = path
        self.num_steps_to_do = num_steps_to_do
        self.num_steps_made = 0

    def setup(self):
        self.done = False
        print(f"Opening recording '{self.recording_path}'")
        self.scene.clear()
        self.scene.open(
            self.recording_path,
            self.step_recording
        )

    def step_recording(self, message):
        sim = self.simulation
        report_simstate(sim, f"Current playback state:")
        print(f"Let's make {self.num_steps_to_do} playback steps:")
        self.ticks = sim.ticks
        self.done = False
        self.on_event(Events.SIMULATION_STATE, self.on_sim_state, lambda: not self.done)
        sim.step()


    def on_sim_state(self, message):
        sim = self.simulation
        if sim.ticks > self.ticks:
            self.ticks = sim.ticks
            report_simstate(sim)
            self.num_steps_made += 1
            if self.num_steps_made >= self.num_steps_to_do:
                self.done = True
                self.complete()
                return
        sim.step()

    def result(self):
        return self.num_steps_made


if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = RecordingStepTask(config, 'api/recordings/misv01_accelerating_01.strec', 10)

        result = task.run()
