
from ashapi import Config, SimcomplexTask, local_server


from ashapi import SimcomplexTask



class ObjectSetSpeedTask(SimcomplexTask):

    def init(self, path):
        self.scene_path = path
        self.object = None

    def setup(self):
        self.done = False
        print(f"Opening scene '{self.scene_path}'")
        self.scene.clear()
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )

    def on_scene_opened(self, response):

        print(f"Opened scene: '{self.scene_path}'")

        self.num_objects = len(self.scene.objects)

        print(f"Opened scene contains {self.num_objects} object(s).")
        print(f"Found first osv01 object among them:")

        o = self.scene.objects["osv01"]

        print(f'{o.uid}: "{o.code}", "{o.name}"')
        print(f"  Speed over ground: {o.sog:.3f} knots")
        v = o.linear
        w = o.angular
        print(f'  Linear speed in local tangent plane: ({v.x:.4f}, {v.y:.4f}, {v.z:.4f}), (m/s)')
        print(f'  Angular speed in local tangent plane: ({w.x:.4f}, {w.y:.4f}, {w.z:.4f}), (rad/s)')

        self.object = o

        print(f"Now let's set 10 m/s speed ahead:")

        o.sog = 10

        self.simulation.run()
        self.simulation.call_each_step(25)(self.report_speed)


    def report_speed(self):

        t = self.simulation.time
        v = self.object.linear

        print(f"{t:.2f}: Now osv01 speed is: {self.object.sog:.3f} m/s, vector: ({v.x:.4f}, {v.y:.4f}, {v.z:.4f}), (m/s)")

        if t > 5.0:
            self.complete()



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = ObjectSetSpeedTask(config, "api/all_models_nv.stexc")

        result = task.run()

