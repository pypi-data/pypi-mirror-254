from ashapi import Config, SimcomplexTask, local_server



class ContentScenesTask(SimcomplexTask):

    def setup(self):
        self.content.request_scenes(
            self.report_scenes
        )

    def report_scenes(self, response):
        print("Your simcomplex setup contains following available scenes:")
        for f in self.content.scenes:
            print(f"  {f}")
        self.complete()



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = ContentScenesTask(config)

        task.run()


