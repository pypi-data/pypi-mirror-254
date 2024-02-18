
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



class SimulationRunTask(SimcomplexTask):

    def setup(self):
        if self.simulation.is_running:
            self.on_event(Events.SIMULATION_STATE, self.paused, lambda: not self.simulation.is_paused)
            self.simulation.pause()
        else:
            self.run_simulation()

    def paused(self, message):
        if self.simulation.is_paused:
            self.run_simulation()

    def run_simulation(self):
        sim = self.simulation
        report_simstate(sim, f"Current simulation state:")
        print(f"Run simulation:")
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


if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = SimulationRunTask(config)

        result = task.run()

