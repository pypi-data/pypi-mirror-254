'''
Copyright (c) 2024 SimTech LLC.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


import pyproj

from . regulator import Regulator, shortest_arc, clamp

'''
See example of using RouteKeeper with Simcomplex in `tutorials/routes/tuga_follow_route.py`
'''

class RouteKeeper(Regulator):

    def __init__(self,
                 wn,
                 zeta,
                 m,
                 d,
                 k,
                 max_r,
                 wn_d,
                 zeta_d,
                 wp_accept_distance,
                 rudder_limit):

        super().__init__(wn, zeta, m, d, k, max_r, wn_d, zeta_d, rudder_limit)

        self.route = []
        self.wp_accept_distance = wp_accept_distance
        self.wp_index = -1

        self.G = pyproj.Geod(ellps='WGS84',sphere=True)


    def set_route(self, route):
        self.route = route
        self.wp_index = -1
        self.next_waypoint()


    def next_waypoint(self):
        if self.wp_index < len(self.route)-1:
            self.wp_index += 1
            wp = self.route[self.wp_index]
            self.order = 0
            return wp


    def calc_diff(self, current_geo_and_heading: tuple): #  (current_geo, current_heading)

        current_geo, current_heading = current_geo_and_heading

        wp = self.route[self.wp_index]

        azimuth_to, _, distance =  self.G.inv(current_geo.lon, current_geo.lat, wp.lon, wp.lat)

        if distance <= self.wp_accept_distance:

            print(f"wp #{self.wp_index} passed")

            wp = self.next_waypoint()

            if wp:

                azimuth_to, _, distance =  self.G.inv(current_geo.lon, current_geo.lat, wp.lon, wp.lat)

                print(f"next wp {self.wp_index} lat {wp.lat} lon {wp.lon} course {azimuth_to}")

        course_order = azimuth_to if azimuth_to >= 0 else (azimuth_to + 360)

        return shortest_arc(current_heading, course_order)


    def get_control_order(self,
                          current_geo_and_heading: tuple, # (current_geo, current_heading)
                          current_rot: float,
                          dt: float):

        if len(self.route) > 0:

            diff = self.calc_diff(current_geo_and_heading)

            if self._ref_order is None:
                self._ref_order = diff

            self.calc_ref_model(dt) # desired jerk

            psi = self._ref_order - diff

            u = self.calc_pid_order(psi, current_rot, dt)

            self.control_order = clamp(-u, -self.control_limit, self.control_limit)

        return self.control_order
