

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


class SimulationStepTask(SimcomplexTask):

    def init(self, steps_to_do):
        self.steps_to_do = steps_to_do
        self.num_steps_made = 0

    def setup(self):
        if self.simulation.is_running:
            self.on_event(Events.SIMULATION_STATE, self.paused, lambda: self.simulation.is_running)
            self.simulation.pause()
        else:
            self.step_simulation()

    def paused(self, message):
        if self.simulation.is_paused:
            self.step_simulation()

    def step_simulation(self):
        sim = self.simulation
        report_simstate(sim, f"Current simulation state:")
        print(f"Let's make {self.steps_to_do} simulation steps:")
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
            if self.num_steps_made >= self.steps_to_do:
                self.done = True
                self.complete()
                return
            sim.step()

    def result(self):
        return self.num_steps_made


if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = SimulationStepTask(config, 10)

        result = task.run()
