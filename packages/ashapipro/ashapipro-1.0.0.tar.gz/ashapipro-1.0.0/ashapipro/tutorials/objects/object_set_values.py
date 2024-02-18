
from ashapi import Config, SimcomplexTask, local_server



class ObjectSetValuesTask(SimcomplexTask):

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
        print(f"Opened scene contains {self.ship.code} object, with following engines states:")
        eport, estbd = self.ship.devices["engine.port"], self.ship.devices["engine.stbd"]
        print(f"{eport.tag}: torque: {eport.torque:.3f}, revolutions: {eport.revolutions:.2f}")
        print(f"{estbd.tag}: torque: {estbd.torque:.3f}, revolutions: {estbd.revolutions:.2f}")
        print(f"Now let's see what will happen if to start engines...")
        eport.start_order = 1
        estbd.start_order = 1
        self.simulation.run()
        self.simulation.call_each_step(1)(self.report_engines)

    def report_engines(self):

        t = self.simulation.time

        eport, estbd = self.ship.devices["engine.port"], self.ship.devices["engine.stbd"]
        print(f"{t:.2f}:{eport.tag}: torque: {eport.torque:.3f}, revolutions: {eport.revolutions:.2f}")
        print(f"{t:.2f}:{estbd.tag}: torque: {estbd.torque:.3f}, revolutions: {estbd.revolutions:.2f}")

        if t > 1.0:
            self.complete()




if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = ObjectSetValuesTask(config, "api/all_models_nv.stexc", "cargo01")

        result = task.run()

