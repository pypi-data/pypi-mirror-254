from ashapipro.autopilot.routekeeper import RouteKeeper

from ashapi import Config, SimcomplexTask, local_server
from ashapi.math2 import rad2deg

class RouteKeeperTask(SimcomplexTask):

    def init(self, path, object_uid, route_uid, controller, freq):
        self.scene_path = path
        self.uid = object_uid
        self.route_uid = route_uid
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

        route = self.scene.routes[self.route_uid]

        if ship is None or route is None:
            if ship is None:
                print(f"Couldn't find object with uid={self.uid} in opened scene '{self.scene_name}'")
            if route is None:
                print(f"Couldn't find route with name={self.route_uid} in opened scene '{self.scene_name}'")
            print(f"Finishing task...")
            self.complete()

        ship.route_id_order = route.uid

        self.controller.set_route(route) # , ship.geo, ship.hdg)

        self.ship = ship
        self.prev_time = self.simulation.time

        self.simulation.run()
        self.simulation.call_each_step()(self.keep_on_route)


    def keep_on_route(self):

        ship = self.ship

        if ship.route_id_order != self.route_uid:
            self.route_uid = ship.route_id_order
            route = self.scene.routes[self.route_uid]
            print(f"Ship has been assigned to another route: {route.uid}, '{route.name}'")
            self.controller.set_route(route) #, ship.geo, ship.hdg)
            order = self.controller.get_control_order((ship.geo, ship.hdg), rad2deg(ship.rot), self.dt)
            ship.devices["propeller.aft"].steering_order = order
            self.prev_time = self.simulation.time

        ship.route_id_order = self.route_uid # to update other clients

        t = self.simulation.time
        dt = t - self.prev_time

        if (dt >= self.dt):
            self.prev_time = t
            order = self.controller.get_control_order((ship.geo, ship.hdg), rad2deg(ship.rot), dt)
            ship.devices["propeller.aft"].steering_order = order

        if t > 6000.0:
            self.complete()


if __name__ == "__main__":

    config = Config.localhost()

    with local_server(config):

        scene_name = "api/routes/tuga_on_route_01.stexc"
        object_id = 1
        route_id = 7
        frequency = 2 # Hz

        routekeeper = RouteKeeper(
            wn = 0.35,
            zeta = 0.9,
            m = 1,
            d = 0.0,
            k = 0.0,
            max_r = 4.0,
            wn_d = 0.15,
            zeta_d = 1.0,
            wp_accept_distance = 100.0,
            rudder_limit = 15
        )

        task = RouteKeeperTask(config,
                               scene_name,
                               object_id,
                               route_id,
                               routekeeper,
                               frequency)

        result = task.run()

