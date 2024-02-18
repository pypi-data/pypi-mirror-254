from ashapi import Config, SimcomplexTask, local_server


class ContentRecordingsTask(SimcomplexTask):

    def setup(self):
        self.content.request_recordings(
            self.report_recordings
        )

    def report_recordings(self, response):
        print("Your simcomplex setup contains following available recordings:")
        for f in self.content.recordings:
            print(f"  {f}")
        self.complete()



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = ContentRecordingsTask(config)

        task.run()

