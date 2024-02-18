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


from ashapi.math2 import clamp


def shortest_arc(from_deg, to_deg):
    diff = (to_deg - from_deg) % 360
    return diff if diff <= 180 else (diff - 360)


class Regulator:

    def __init__(self,
                 wn,
                 zeta,
                 m,
                 d,
                 k,
                 max_r,
                 wn_d,
                 zeta_d,
                 limit
                 ):

        # desired order for tracked value
        self._order = None
        self._ref_order = None

        # control order to keep tracked value
        self.control_order = 0
        self.control_limit = limit

        # PID parameters
        self.wn = wn # natural freq. of control model. Used in PID pole placement
        self.zeta = zeta  # damping factor of control model. Used in PID pole placement
        self.m = m # param in Pole placement
        self.d = d # param in Pole placement
        self.k = k # param in Pole placement

        # ref model data parameters
        self.max_r = max_r           # max tracked value speed from ref model
        self.wn_d = wn_d              # desired natural frequency in tracked value for ref model
        self.damping = 2 * zeta_d + 1 # 'zeta_d' is desired relative damping ratio in tracked value for ref model

        # internal parameters used for calculations
        self.e_int = 0.0 # integral error of PID
        self.psi_d = 0.0 # desired value from ref model
        self.r_d = 0.0   # desired value speed (rate) from ref model
        self.a_d = 0.0   # desired value acceleration from ref model

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value
        self._ref_order = None
        self.e_int = 0.0 # integral error of PID
        self.psi_d = 0.0 # desired angle from ref model
        self.r_d = 0.0 # desired ang. rate from ref model
        self.a_d = 0.0 # desired ang acc. from ref model


    def get_control_order(self,
                          tracked_value: float,
                          tracked_speed: float,
                          dt: float):

        diff = self.calc_diff(tracked_value)

        if self._ref_order is None:
            self._ref_order = diff

        self.calc_ref_model(dt) # desired jerk

        # PID controller

        psi = self._ref_order - diff

        u = self.calc_pid_order(psi, tracked_speed, dt)

        self.control_order = clamp(-u, -self.control_limit, self.control_limit)

        return self.control_order


    def calc_diff(self, tracked_value):
        return self.order - tracked_value


    def calc_ref_model(self, dt):
        # desired "jerk"
        j_d = self.wn_d**3 * (self._ref_order  - self.psi_d) - self.damping * self.wn_d**2 * self.r_d - self.damping * self.wn_d * self.a_d
        self.psi_d = self.psi_d + dt * self.r_d   # desired value
        self.r_d   = self.r_d   + dt * self.a_d   # desired speed (rate)
        self.a_d   = self.a_d   + dt * j_d        # desired acceleration 

        self.r_d = clamp(self.r_d, -self.max_r, self.max_r) # speed (rate) saturation



    def calc_pid_order(self, psi: float, rate: float, dt: float):
        e_psi = psi - self.psi_d
        e_r = rate - self.r_d
        self.e_int = self.e_int + dt * e_psi
        Kp = self.m * self.wn ** 2 - self.k
        Kd = self.m * 2 * self.zeta * self.wn - self.d
        Ki = (self.wn / 10) * Kp
        u = -Kp * e_psi - Kd * e_r - Ki * self.e_int
        return u
