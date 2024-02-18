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


import xml.etree.ElementTree as ET

from shapely.geometry import Polygon, MultiPolygon


def area_xmltree(xml: str = "", filepath: str = "") -> ET.ElementTree:
    if xml:
        return ET.ElementTree(ET.fromstring(xml))
    if filepath:
        return ET.parse(filepath)


def extract_area_multipoligons(axmltree: ET.ElementTree, s_57_acronym: str ='LNDARE'):
    area = None
    for child in axmltree.getroot():
        if child.tag == s_57_acronym:
            area = child
            break
    polygons = []
    _split_value = ' 0.0000 '
    for item in area.iter():
        if ('type' in item.attrib) and (item.attrib['type']=='polygon'):
            polylines = []
            for line in item.iter('line'): 
                line = line.attrib['points'].split(_split_value)[:-1]
                polylines += line
            tup_list = []
            for i in polylines:
                tup_list.append(tuple(map(float, reversed(i.split(' ')))))
            polygons.append(Polygon(tup_list))
            polylines = []
    return MultiPolygon(polygons)

