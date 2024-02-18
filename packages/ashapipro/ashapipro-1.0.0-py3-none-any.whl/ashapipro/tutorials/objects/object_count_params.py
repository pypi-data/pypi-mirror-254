
from ashapi import Config, SimcomplexTask, local_server


class ObjectCountParamsTask(SimcomplexTask):

    def init(self, path, code):
        self.scene_path = path
        self.code = code
        self.count = 0

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

        print(f"Opened scene contains {ship.code} object, which has following params:")
        print(f"Object parameters:")
        print(f"  Name: {ship.name}") # +1
        print(f"  Position: {ship.pos}") # +3
        print(f"  Rotation: {ship.rot}") # +4
        print(f"  Linear Speed: {ship.linear}") # +3
        print(f"  Angular Speed: {ship.angular}") # +3
        self.count += 14
        for pname, pvalue in ship.values.items():
            print(f'   {pname}: {pvalue}')
            self.count += 1
        print(f"Equipment parameters:")
        for tag, device in ship.devices:
            print(f'    {tag}')
            for pname, pvalue in device.values.items():
                print(f'       {pname}: {pvalue}')
                self.count += 1
        print(f"Total parameters count: {self.count}")
        self.complete()

    def result(self):
        return self.count




if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = ObjectCountParamsTask(config, "api/objects/cargo01_full_speed_ahead_01.stexc", "cargo01")

        result = task.run()


