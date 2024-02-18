from ashapipro.autopilot.speedkeeper import SpeedKeeper

from ashapi import Config, SimcomplexTask, local_server


class SpeedKeeperTask(SimcomplexTask):

    def init(self, path, object_uid, speed_order, controller, freq):
        self.scene_path = path
        self.uid = object_uid
        self.speed_order = speed_order # deg
        self.controller = controller
        self.dt = 1/freq
        self.ship = None
        self.prev_time = 0

    def setup(self):
        print(f"Opening scene '{self.scene_path}'")
        self.scene.clear()
        self.scene.open(
            self.scene_path,
            self.on_scene_opened
        )

    def on_scene_opened(self, response):

        print(f"Opened scene: '{self.scene_path}'")

        ship = self.scene.objects.find_by(self.uid)

        if ship is None:
            print(f"Couldn't find object with uid={self.uid} in opened scene '{self.scene_name}'")
            self.complete()

        ship.speed_order = self.speed_order
        self.controller.order = self.speed_order

        self.ship = ship
        self.prev_time = self.simulation.time

        self.simulation.run()
        self.simulation.setaccel(5.0)
        self.simulation.call_each_step()(self.keep_speed)


    def keep_speed(self):

        ship = self.ship

        if ship.speed_order != self.speed_order:
            self.speed_order = ship.speed_order
            print(f"Ship has got another speed order: {ship.speed_order} ")
            self.controller.order = self.speed_order
    
            order = self.controller.get_control_order(ship.sog, self.dt)

            ship.devices["propeller.main"].throttle_order = order
            self.prev_time = self.simulation.time

        ship.speed_order = self.speed_order # to update other clients

        t = self.simulation.time
        dt = t - self.prev_time

        if (dt >= self.dt):
            self.prev_time = t
            order = self.controller.get_control_order(ship.sog, dt)
            ship.devices["propeller.main"].throttle_order = order

        if t > 6000.0:
            self.complete()


if __name__ == "__main__":

    config = Config.localhost()

    with local_server(config):

        scene_name = "api/objects/cargo_full_speed_ahead.stexc"
        object_id = 1
        speed_order = 5 # m/s
        frequency = 1 # Hz

        coursekeeper = SpeedKeeper(
            wn = 0.03,
            zeta = 0.9,
            m = 600,
            d = 0.0,
            k = 0.0,
            max_r = 10.0,
            wn_d = 0.008,
            zeta_d = 1.0
        )

        task = SpeedKeeperTask(config,
                                scene_name,
                                object_id,
                                speed_order,
                                coursekeeper,
                                frequency)

        result = task.run()

