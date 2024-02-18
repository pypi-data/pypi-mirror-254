
from ashapi import Config, SimcomplexTask, local_server



class OpenRecordingTask(SimcomplexTask):

    def init(self, path):
        self.recording_path = path

    def setup(self):
        self.done = False
        print(f"Opening recording '{self.recording_path}'")
        self.scene.clear()
        self.scene.open(
            self.recording_path,
            self.on_recording_opened
        )

    def on_recording_opened(self, response):
        print(f"Opened recording: '{self.recording_path}'")
        print(f"Opened recording contains {len(self.scene.objects)} object(s), {len(self.scene.routes)} route(s)")
        if self.scene.objects:
            print("Objects:")
            for o in self.scene.objects:
                print(f'    {o.uid}: {o.code}, "{o.name}"')
        if self.scene.routes:
            print("Routes:")
            for r in self.scene.routes:
                print(f"    {r.uid}: {r.name}, '{len(r)}' points")
        self.done = self.scene.path == self.recording_path
        self.complete()

    def result(self):
        return self.done



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = OpenRecordingTask(config, 'api/recordings/misv01_accelerating_01.strec')

        result = task.run()
