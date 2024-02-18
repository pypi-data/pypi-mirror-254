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


from . regulator import Regulator, shortest_arc

'''
See example of using CourseKeeper with Simcomplex in `tutorials/objects/cargo_keep_course.py`
'''


class CourseKeeper(Regulator):

    def __init__(self,
                 wn,
                 zeta,
                 m,
                 d,
                 k,
                 max_r,
                 wn_d,
                 zeta_d,
                 rudder_limit):

        super().__init__(wn, zeta, m, d, k, max_r, wn_d, zeta_d, rudder_limit)


    def calc_diff(self, tracked_value, _arc=shortest_arc):
        return _arc(tracked_value, self.order)
