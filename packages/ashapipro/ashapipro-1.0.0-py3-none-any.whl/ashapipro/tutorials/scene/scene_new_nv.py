
from ashapi import Config, SimcomplexTask, Events, local_server



class NewSceneWithAreaTask(SimcomplexTask):

    def init(self, name: str, area: str):
        self.scene_name = name
        self.scene_area = area

    def setup(self):
        self.content.request_areas(
            self.on_got_areas
        )
        self.scene.clear()
        self.scene.new_path(self.scene_name,
                            self.on_scene_created)

    def on_got_areas(self, response):
        print("Your simcomplex contains following avaialble areas:")
        for key, a in self.content.areas.items():
            print(f'{key}: {str(a)}')

    def on_scene_created(self, response):
        print(f"Created new empty scene with name: '{self.scene.path}'")
        if self.scene_area in self.content.areas:
            print(f"Set scene area to: '{self.scene_area}'")
            self.on_event(Events.AREA, self.on_area_changed)
            self.scene.area.set(self.content.areas[self.scene_area])

    def on_area_changed(self, response):
        print(f"Area changed to: '{self.scene.area}'")
        self.complete()

    def result(self):
        area = self.scene.area
        return area.name == self.scene_area



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = NewSceneWithAreaTask(config, "my_new_scene_with_area", 'RU_NVS')

        result = task.run()

