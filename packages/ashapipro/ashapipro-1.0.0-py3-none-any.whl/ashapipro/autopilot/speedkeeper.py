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


from . regulator import Regulator, clamp

'''
See example of using SpeedKeeper with Simcomplex in `tutorials/objects/cargo_keep_speed.py`
'''

class SpeedKeeper(Regulator):

    def __init__(self,
                 wn,
                 zeta,
                 m,
                 d,
                 k,
                 max_r,
                 wn_d,
                 zeta_d,
                 max_prop_order = 1.0):

        super().__init__(wn, zeta, m, d, k, max_r, wn_d, zeta_d, max_prop_order)

        self.prev_v = 0.0
        self.a = 0.0


    def get_control_order(self, current_speed: float, dt: float):

        self.a = (current_speed - self.prev_v) / dt
        self.prev_v = current_speed

        self.calc_ref_model(dt)

        u = self.calc_pid_order(current_speed, self.a, dt)

        self.control_order = clamp(u, -self.control_limit, self.control_limit)

        return self.control_order


    def calc_ref_model(self, dt):
        j_d = self.damping * self.wn_d**2 * (self.order - self.psi_d) - self.damping * self.wn_d * self.r_d
        self.psi_d = self.psi_d + dt * self.r_d
        self.r_d   = self.r_d   + dt * j_d
        self.r_d = clamp(self.r_d, -self.max_r, self.max_r)
