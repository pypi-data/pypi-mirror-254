
from ashapi import Config, SimcomplexTask, local_server


class ObjectSetOrdersTask(SimcomplexTask):

    def init(self, path, code):
        self.scene_path = path
        self.code = code
        self.ship = None

    def setup(self):
        print(f"Opening scene '{self.scene_path}'")
        self.scene.clear()
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )

    def on_scene_opened(self, response):
        print(f"Opened scene: '{self.scene_path}'")
        self.ship = self.scene.objects[self.code]
        print(f"Opened scene contains {self.ship.code} object, with following propellers values:")
        pport, pstbd = self.ship.devices["propeller.port"], self.ship.devices["propeller.stbd"]
        print(pport.values)
        # {'gear_ratio': 1.0, 'revolutions': 1e-05, 'throttle_order': 0.0, 'throttle_reply': 0.0, 'torque': 0.0}
        print(f"{pport.tag}: torque: {pport.torque:.3f}, revolutions: {pport.revolutions:.2f}")
        print(f"{pstbd.tag}: torque: {pstbd.torque:.3f}, revolutions: {pstbd.revolutions:.2f}")
        print(f"Now let's see what will happen if to set propellers throttle...")
        eport, estbd = self.ship.devices["engine.port"], self.ship.devices["engine.stbd"]
        eport.start_order = 1
        estbd.start_order = 1
        pport.throttle_order = 1
        pstbd.throttle_order = 1
        self.simulation.run()
        self.simulation.call_each_step(25)(self.report_engines)

    def report_engines(self):

        t = self.simulation.time

        pport, pstbd = self.ship.devices["propeller.port"], self.ship.devices["propeller.stbd"]
        print(f"{pport.tag}: torque: {pport.torque:.3f}, revolutions: {pport.revolutions:.2f}")
        print(f"{pstbd.tag}: torque: {pstbd.torque:.3f}, revolutions: {pstbd.revolutions:.2f}")

        if t > 5.0:
            self.complete()




if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = ObjectSetOrdersTask(config, "api/all_models_nv.stexc", "cargo01")

        result = task.run()

