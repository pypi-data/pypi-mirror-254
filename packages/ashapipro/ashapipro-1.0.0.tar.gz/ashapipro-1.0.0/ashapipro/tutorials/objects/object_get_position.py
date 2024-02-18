
from ashapi import Config, SimcomplexTask, local_server


class ObjectGetPositionTask(SimcomplexTask):

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
        print(f"Opened scene contains {len(self.scene.objects)} object(s).")
        for o in self.scene.objects:
            geo, eul = o.geo, o.euler
            print(f'{o.uid}: "{o.code}", "{o.name}"')
            print(f'    Position in local tangent plane: ({o.pos.x:.2f}, {o.pos.y:.2f}, {o.pos.z:.2f}), (m)')
            print(f'    Orientation in local tangent plane:')
            print(f'        Heading: {eul.heading:.2f}\u00B0')
            print(f'        Pitch: {eul.pitch:.2f}\u00B0')
            print(f'        Roll: {eul.roll:.2f}\u00B0')
            print(f'    Geolocation (lat, lon): ({geo.lat:.5f}\u00B0, {geo.lon:.5f}\u00B0)')
        self.complete()



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = ObjectGetPositionTask(config, "api/all_models_nv.stexc")

        result = task.run()

