from ashapi import Config, SimcomplexTask, local_server


class SceneAreaInfoTask(SimcomplexTask):

    def init(self, path):
        self.scene_path = path
        self.map = None


    def setup(self):
        print(f"Opening scene '{self.scene_path}'")
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )


    def on_scene_opened(self, response):

        print(f"Opened scene: '{self.scene_path}'")
        print(f"Opened scene origin is within following area:")

        area = self.scene.area

        print(f"Area: '{area.name}'")
        print(f"    Lat/Lon: {area.origo[0]:.4f}/{area.origo[1]:.4f} (degrees)")
        print(f"    Maps: {','.join([m[:-4] for m in area.maps])}")

        print(f"More details on area is available through content request:")

        self.content.request_areas(self.on_got_areas)


    def on_got_areas(self, response):

        info = self.content.areas[self.scene.area.name]

        print(f"Area: '{info.name}'")
        print(f"    Title: '{info.title}'")
        descr = " ".join(info.description)
        print(f"    Description: '{descr}'")
        print(f"    Lat/Lon: {info.origo[0]:.4f}/{info.origo[1]:.4f} (radians)")
        print(f"    Meshes: {', '.join([m[:-5] for m in info.meshes])}")
        print(f"    Maps: {', '.join([m[:-4] for m in info.maps])}")

        print(f"You can actually request downloading of area's map data:")
        self.map = info.maps[-1]
        self.content.request_area_map(info.name, self.map, self.on_got_map)


    def on_got_map(self, response):
        print(f"Downloaded raw {self.map} data, now this xml can be processed or saved to file...")
        self.complete()



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = SceneAreaInfoTask(config, "api/all_models_nv.stexc")

        result = task.run()
