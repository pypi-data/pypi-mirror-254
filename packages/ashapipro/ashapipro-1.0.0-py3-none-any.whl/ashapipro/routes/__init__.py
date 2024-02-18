'''
This module provides useful functions to build graphs based upon navigational area data.
Also it gives functions to build paths based on area graphs, in order to create navigational routes in the given area.

For usage, see (run):

    1. `tutorials/routes/build_astar_path_on_area_neighbours_graph.py`

        Builds A-Star path over 8-neigbours square cells graph.
        Graph is built upon area data provided by Simcomplex.

    2. `tutorials/routes/build_bellman_ford_path_on_area_polygon_graph.py`

        Builds Bellman-Ford path based upon 'polygon' graph.
        Graph is built upon area polygons data provided by Simcomplex.

    3. `tutorials/routes/build_dijkstra_path_on_area_all_to_all_graph.py`

        Builds Dijkstra path over all-to-all square cells graph.
        Graph is built upon area data provided by Simcomplex.
'''


from . import areautil
from . import graph