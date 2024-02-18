
from ashapi import Config, SimcomplexTask, local_server

from ashapi.math2 import rad2deg, msec2knots



class ObjectGetSpeedsTask(SimcomplexTask):

    def init(self, path):
        self.scene_path = path

    def setup(self):
        print(f"Opening scene '{self.scene_path}'")
        self.scene.clear()
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )

    def on_scene_opened(self, response):

        print(f"Opened scene: '{self.scene_path}'")

        ship = self.scene.objects['cargo01']

        print(f"Opened scene contains {ship.code} object, which has following speed characteristics:")
        print(f"  Speed over ground: {msec2knots(ship.sog):.3f} knots")
        print(f"  Course over ground: {ship.cog:.2f}\u00B0")
        print(f"  Rotation speed: {(rad2deg(ship.rot) * 60.0):.3f} \u00B0/min")
        v = ship.linear
        w = ship.angular
        print(f'  Linear speed in local tangent plane: ({v.x:.4f}, {v.y:.4f}, {v.z:.4f}), (m/s)')
        print(f'  Angular speed in local tangent plane: ({w.x:.4f}, {w.y:.4f}, {w.z:.4f}), (rad/s)')

        self.complete()



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = ObjectGetSpeedsTask(config, "api/objects/cargo01_full_speed_ahead_01.stexc")

        result = task.run()


