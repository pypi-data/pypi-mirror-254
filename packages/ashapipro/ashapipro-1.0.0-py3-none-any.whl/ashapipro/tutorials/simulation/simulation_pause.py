
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


class SimulationPauseTask(SimcomplexTask):

    def setup(self):
        if self.simulation.is_paused:
            self.on_event(Events.SIMULATION_STATE, self.running, lambda: not self.simulation.is_running)
            self.simulation.run()
        else:
            self.pause_simulation()

    def running(self, message):
        if self.simulation.is_running:
            self.pause_simulation()

    def pause_simulation(self):
        sim = self.simulation
        report_simstate(sim, f"Current simulation state:")
        print(f"Pause simulation:")
        self.done = False
        self.on_event(Events.SIMULATION_STATE, self.on_sim_state, lambda: not self.done)
        sim.pause()

    def on_sim_state(self, message):
        sim = self.simulation
        if sim.is_paused:
            report_simstate(sim)
            self.done = True
            self.complete()


if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = SimulationPauseTask(config)

        result = task.run()

