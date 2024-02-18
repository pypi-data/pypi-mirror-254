from ashapipro.autopilot.coursekeeper import CourseKeeper

from ashapi import Config, SimcomplexTask, local_server

from ashapi.math2 import rad2deg


class CourseKeeperTask(SimcomplexTask):

    def init(self, path, object_uid, course_order, controller, freq):
        self.scene_path = path
        self.uid = object_uid
        self.course_order = course_order # deg
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

        ship.course_order = self.course_order
        self.controller.order = self.course_order

        self.ship = ship
        self.prev_time = self.simulation.time

        self.simulation.run()
        self.simulation.setaccel(5.0)
        self.simulation.call_each_step()(self.keep_on_course)


    def keep_on_course(self):

        ship = self.ship

        if ship.course_order != self.course_order:
            self.course_order = ship.course_order
            print(f"Ship has got another course order: {ship.course_order}\u00B0")
            self.controller.order = self.course_order
    
            order = self.controller.get_control_order(ship.hdg, rad2deg(ship.rot), self.dt)
            ship.devices["rudder.port"].steering_order = order
            ship.devices["rudder.stbd"].steering_order = order
            self.prev_time = self.simulation.time

        ship.course_order = self.course_order # to update other clients

        t = self.simulation.time
        dt = t - self.prev_time

        if (dt >= self.dt):
            self.prev_time = t
            order = self.controller.get_control_order(ship.hdg, rad2deg(ship.rot), dt)
            ship.devices["rudder.port"].steering_order = order
            ship.devices["rudder.stbd"].steering_order = order

        if t > 6000.0:
            self.complete()


if __name__ == "__main__":

    config = Config.localhost()

    with local_server(config):

        scene_name = "api/objects/cargo01_full_speed_ahead_01.stexc"
        object_id = 1
        course_order = 40 # deg
        frequency = 1 # Hz

        coursekeeper = CourseKeeper(
            wn = 0.15,
            zeta = 0.8,
            m = 100,
            d = 0.0,
            k = 0.0,
            max_r = 1.2,
            wn_d = 0.03,
            zeta_d = 1.0,
            rudder_limit=35
        )

        task = CourseKeeperTask(config,
                                scene_name,
                                object_id,
                                course_order,
                                coursekeeper,
                                frequency)

        result = task.run()

