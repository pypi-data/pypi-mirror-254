
from ashapi import Config, SimcomplexTask, Events, local_server

from ashapi import GeoPoint, Euler


class AddObjectTask(SimcomplexTask):

    def init(self, path):
        self.scene_path = path
        self.num_objects = 0

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

        print(f"Opened scene contains {self.num_objects} object(s):")

        for o in self.scene.objects:
            geo, eul = o.geo, o.euler
            print(f'{o.uid}: "{o.code}", "{o.name}"')
            print(f'    Position in local tangent plane: ({o.pos.x:.2f}, {o.pos.y:.2f}, {o.pos.z:.2f}), (m)')
            print(f'    Orientation in local tangent plane:')
            print(f'        Heading: {eul.heading:.2f}\u00B0')
            print(f'        Pitch: {eul.pitch:.2f}\u00B0')
            print(f'        Roll: {eul.roll:.2f}\u00B0')
            print(f'    Geolocation (lat, lon): ({geo.lat:.5f}\u00B0, {geo.lon:.5f}\u00B0)')

        code = "cargo01"
        geo = GeoPoint(44.71155, 37.81662)
        eul = Euler(60)

        print(f"Now let's add {code} at geolocation {geo} with heading={360-eul.heading}\u00B0:")

        self.scene.objects.add(code, name="Warrior", geo = geo, eul = eul)

        self.on_event(Events.OBJECT_DATA, self.on_object, lambda: not self.done)


    def on_object(self, msg):

        print(f"Now scene contains {len(self.scene.objects)} object(s):")

        o = self.scene.objects[-1]

        print(f"And the last one: ")
        geo, eul = o.geo, o.euler
        print(f'And the last one: {o.uid}: "{o.code}", "{o.name}"')
        print(f'    Position in local tangent plane: ({o.pos.x:.2f}, {o.pos.y:.2f}, {o.pos.z:.2f}), (m)')
        print(f'    Orientation in local tangent plane:')
        print(f'        Heading: {eul.heading:.2f}\u00B0')
        print(f'        Pitch: {eul.pitch:.2f}\u00B0')
        print(f'        Roll: {eul.roll:.2f}\u00B0')
        print(f'    Geolocation (lat, lon): ({geo.lat:.5f}\u00B0, {geo.lon:.5f}\u00B0)')

        if len(self.scene.objects) - self.num_objects > 0:
            self.done = True
            self.complete()

    def result(self):
        return self.done



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = AddObjectTask(config, "api/all_models_nv.stexc")

        result = task.run()

