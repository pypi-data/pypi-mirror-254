
from ashapi import Config, SimcomplexTask, Events, local_server

from ashapi import PQ, Vec3



class ObjectSetPositionTask(SimcomplexTask):

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
        print(f"Found first cargo01 object among them:")

        o = self.scene.objects["cargo01"]

        geo, eul = o.geo, o.euler
        print(f'{o.uid}: "{o.code}", "{o.name}"')
        print(f'    Position in local tangent plane: ({o.pos.x:.2f}, {o.pos.y:.2f}, {o.pos.z:.2f}), (m)')
        print(f'    Orientation in local tangent plane:')
        print(f'        Heading: {eul.heading:.2f}\u00B0')
        print(f'        Pitch: {eul.pitch:.2f}\u00B0')
        print(f'        Roll: {eul.roll:.2f}\u00B0')
        print(f'    Geolocation (lat, lon): ({geo.lat:.5f}\u00B0, {geo.lon:.5f}\u00B0)')

        self.object = o

        print(f"Now let's move it to the position 100 m ahead:")

        pq = o.pq

        o.pq = pq.abs(PQ(Vec3(100)))

        self.on_event(Events.OBJECT_POSITION, self.on_object_position, lambda: not self.done)


    def on_object_position(self, msg):

        o = self.object

        print(f"Now cargo01 position is:")
        geo, eul = o.geo, o.euler
        print(f'    Position in local tangent plane: ({o.pos.x:.2f}, {o.pos.y:.2f}, {o.pos.z:.2f}), (m)')
        print(f'    Orientation in local tangent plane:')
        print(f'        Heading: {eul.heading:.2f}\u00B0')
        print(f'        Pitch: {eul.pitch:.2f}\u00B0')
        print(f'        Roll: {eul.roll:.2f}\u00B0')
        print(f'    Geolocation (lat, lon): ({geo.lat:.5f}\u00B0, {geo.lon:.5f}\u00B0)')

        self.done = True
        self.complete()

    def result(self):
        return self.done



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = ObjectSetPositionTask(config, "api/all_models_nv.stexc")

        result = task.run()

