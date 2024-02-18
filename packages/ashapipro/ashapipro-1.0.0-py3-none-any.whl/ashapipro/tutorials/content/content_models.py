from ashapi import Config, SimcomplexTask, local_server


class ContentModelsTask(SimcomplexTask):

    def init(self, code):
        self.code = code

    def setup(self):
        self.content.request_models(
            self.report_model_info
        )

    def report_model_info(self, response):
        # print("Your simcomplex setup contains following available models:")
        # for code, _ in self.content.models.items():
        #     print(f"  {code}")
        model = self.content.models[self.code]
        print(f"{self.code} has following characteristics:")
        print(f'Code: "{model.code}"')
        print(f'Name: "{model.name}"')
        if model.tags:
            print(f'Tags: ' + ",".join([f'"{t}"' for t in model.tags]))
        if model.length is not None:
            print(f'Length: {model.length:.2f} m')
        if model.beam is not None:
            print(f'Width: {model.beam:.2f} m')
        if model.height is not None:
            print(f'Height: {model.height:.2f} m')
        if model.draught is not None:
            print(f'Draught: {model.draught:.2f} m')
        print(f'Mass: {model.mass} m')
        print(f'Inertial Ixx/Iyy/Izz: {model.inertia[0]} / {model.inertia[1]} / {model.inertia[2]} kg*m2')
        print(f'Center of mass: x={model.cms[0]:.3f}, y={model.cms[1]:.3f}, z={model.cms[2]:.3f} m')
        self.complete()



if __name__ == '__main__':

    config = Config.localhost()

    with local_server(config):

        task = ContentModelsTask(config, 'misv01')

        task.run()

        task = ContentModelsTask(config, 'cargo01')

        task.run()

        task = ContentModelsTask(config, 'osv01')

        task.run()

        task = ContentModelsTask(config, 'tuga01')

        task.run()


