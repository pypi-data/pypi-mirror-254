
from ashapi import Config, SimcomplexTask, local_server


class ObjectDevicesOrdersTask(SimcomplexTask):

    def init(self, path, code):
        self.scene_path = path
        self.code = code

    def setup(self):
        print(f"Opening scene '{self.scene_path}'")
        self.scene.clear()
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )

    def on_scene_opened(self, response):
        print(f"Opened scene: '{self.scene_path}'")
        ship = self.scene.objects[self.code]
        print(f"Opened scene contains {ship.code} object, with following orders in propulsion-steering system:")
        for tag in ("propeller.port", "propeller.stbd", "engine.port", "engine.stbd", "rudder.port", "rudder.stbd"):
            device = ship.devices[tag]
            print(f'{tag}')
            for pname, pvalue in device.orders.items():
                print(f'   {pname}: {pvalue}')
        self.complete()



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = ObjectDevicesOrdersTask(config, "api/objects/cargo01_full_speed_ahead_01.stexc", "cargo01")

        result = task.run()
