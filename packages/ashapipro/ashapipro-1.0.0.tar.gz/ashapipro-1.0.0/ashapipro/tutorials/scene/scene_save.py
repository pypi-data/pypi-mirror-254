
from ashapi import Config, SimcomplexTask, local_server


class SaveSceneTask(SimcomplexTask):

    scene_path = "api/saved_scene"

    def setup(self):
        self.done = False
        print(f"Saving scene to '{self.scene_path}'")
        self.scene.save(
            self.scene_path,
            self.on_scene_saved
        )

    def on_scene_saved(self, response):
        print(f"Saved scene to: '{self.scene_path}'")
        self.content.request_scenes(
            self.check_content_scenes
        )

    def check_content_scenes(self, response):
        if f"{self.scene_path}.stexc" in self.content.scenes:
            print("Scene has been successfully saved and now available in simcomplex content")
            self.done = True
        self.complete()

    def result(self):
        return self.done



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = SaveSceneTask(config)

        result = task.run()

