import csv

from cityRoadMap import CityRoadMap
from road import Road
from city import City
"""
 Project 4
 Filename: NCCitiesRoads.py
 Programmer: Alex Lopez Torres Riega
 Date: December 04, 2018

 Description:
    Object-oriented program that maps out 52 NC cities with roads
    that connect them and the distances between the cities along
    the road.

    Uses four graph traversal algorithms, depth-first search,
    breadth-first search, minimum spanning tree and shortest path.
"""

"""
This is the mainline logic for running commands
for a Graph of City and Road objects
"""


def main():
    # Constants for file names and records
    COMMAND_FILE = "Commands.txt"
    OUTPUT_FILE = "NCRoutesOut.txt"

    # Create an output File writer for writing the processing results
    writer = open(OUTPUT_FILE, 'w')

    # Open and Read file containing the commands to be processed
    cmd_file = open(COMMAND_FILE, 'r')
    file_lines = csv.reader(cmd_file, delimiter=':')
    commands = list(file_lines)
    cmd_file.close()

    print("Begin NC Routes Program ")

    # Use build_map function to create empty CityRoadMap object, and 
    # return the graph and the output message etring
    # You need to pass this pass to process_cmd
    city_road_map, msg = build_map()

    msg = msg + '\n'

    # Loop for each line in the Command File and process it
    # The command output is placed in the result String
    for cmd_line in commands:
        msg += process_cmd(cmd_line, city_road_map)
    writer.write(msg)

    print("End NC Routes Program ")

    writer.close()


def process_cmd(cmd_list, city_road_map):

    cmd = cmd_list[0].strip().lower()

    # Echo the command
    result = "Command: " + cmd.upper() + "\n"

    if cmd == "PrintMap".lower():
        result += city_road_map.get_roads_str()

    elif cmd == "PrintCities".lower():
        result += city_road_map.get_cities_str() + "\n"

    elif cmd == "DFSMap".lower():
        root = cmd_list[1].strip()
        dest = cmd_list[2].strip()

        result += dfs(city_road_map, root, dest) + "\n"

    elif cmd == "BFSMap".lower():
        root = cmd_list[1].strip()

        result += bfs(city_road_map, root) + "\n"

    elif cmd == "MSTMap".lower():
        root = cmd_list[1].strip()

        result += mst(city_road_map, root) + "\n"
        
    elif cmd == "ShortPathMap".lower():
    
        if city_road_map is not None:
            num_args = len(cmd_list)
            root = cmd_list[1].strip()
            dest = None
            if num_args == 3:
                dest = cmd_list[2].strip()
                
            result += shortest_path(city_road_map, root, dest)

    elif cmd == "SortCities".lower():
        result += sort_cities(city_road_map) + "\n"
    else:
        result += "Unknown command."

    return result

"""
Build CityRoadMap graph object
from the CITY and ROAD records in a file

Note: Do NOT round any values (especially GPS) here, 
      we want them to have their max precision.
      Only do rounding when displaying values
"""


def build_map():

    print("Entering build map")

    CITY_REC = "CITY"
    ROAD_REC = "ROAD"
    NCMAP_FILE = "NCRoadMap.csv"

    # Start message about City and Roads processed
    msg = ""

    # Create lists for holding Graph information and
    # a dictionary that maps the City name to its index in cities
    cities = []
    roads = []
    city_dict = {}
    city_index = 0
    road_index = 0

    road = []

    # Read in Road Map information from NCMAP_FILE using CSV reader
    ncmap_file = open(NCMAP_FILE, 'r')
    file_lines = csv.reader(ncmap_file, delimiter=',')
    ncmap = list(file_lines)

    ncmap_file.close()
    
    # Loop: Read each line in NCMAP_FILE:
    # The first field has either CITY or ROAD to distinguish the record type
    # The remaining fields are used to create the City or Road objects
    # Append each city to the cities list and each road to the roads list
    for info in ncmap:
        identifier = info[0]
        fields = info[1:]
        if identifier == CITY_REC:
            city = info[1]
            x = info[2]
            y = info[3]
            pop = info[4]

            cities.append(City(city, x, y, pop))
            city_dict[city] = city_index
            city_index += 1

        elif identifier == ROAD_REC:
            from_city = info[1]
            to_city = info[2]
            roads.append(Road(cities[city_dict.get(from_city)], cities[city_dict.get(to_city)]))
            road.append(fields)
            road_index += 1

    # Add the processing message to the String result to return
    
    msg += "Processed {} Cities and {} Roads \n".format(city_index, road_index)

    # Build a road_map CityRoadMap graph object of the cities and roads
    
    city_road_map = CityRoadMap(cities, roads)

    return city_road_map, msg


"""
Depth first search:
Starting Node : root_name
Destination Node: dest_name
"""


def dfs(city_road_map, root_name, dest_name):
    # Retrieve the starting vertex from the root city name
    root = city_road_map.get_vertex(root_name)

    # Call the DFS graph method, which returns a DFS tree 
    # containing the DFS order of the vertices, starting with root
    dfs_tree = city_road_map.df_search(root)

    # Retrieve the City search order and Number of Cities
    search_order = dfs_tree.get_search_order()
    num_cities = dfs_tree.get_num_verts_found()

    # Output the number of Cities found and root name
    msg = str(num_cities) + " cities are searched in this DFS order"
    msg += " starting from " + root_name + "\n"

    # Loop through the search order list
    # Output each city name: only display 5 cities per line
    city_count = 0
    for city in search_order:
        if city_count % 5 == 0:
            msg += "\n" + city.get_name()
        else:
            msg += ", " + city.get_name()

        city_count += 1


    # Print the DFS Path of Roads From Root
    # msg += "\n\nDFS Path of Roads" + "\n"
    msg += "\n\nRoot is " + str(root.get_name()) + "\n"
    msg += dfs_tree.get_edge_str()

    # Retrieve the starting vertex from the root city name
    dest = city_road_map.get_vertex(dest_name)

    # Print the DFS Path of Cities From Root to Dest
    msg += dfs_tree.get_path_str(dest) + "\n"

    return msg


"""
Breadth first search:
Starting Node : root_name
"""


def bfs(city_road_map, root_name):
    # Retrieve the starting vertex from the root city name
    root = city_road_map.get_vertex(root_name)

    # Call the BFS method, which returns a BFS tree containing
    # the BFS order of the vertices, starting with root
    bfs_tree = city_road_map.bf_search(root)

    # Retrieve the City search order and Number of Cities
    search_orders = bfs_tree.get_search_order()
    num_cities = bfs_tree.get_num_verts_found()

    # Output the number of Cities found and root name

    msg = str(num_cities) + " cities are searched in this BFS order"
    msg += " starting from " + root_name + "\n"

    # Loop through the search order list
    # Output each city name: only display 5 cities per line
    city_count = 0
    for city in search_orders:
        if city_count % 5 == 0:
            msg += "\n" + city.get_name()
        else:
            msg += " : " + city.get_name()

        city_count += 1
    
    # Print the parents of the vertices found using BFS order
    # of cities starting with root
    msg += "\n\nThe parents of cities searched in BFS order:" + "\n"
    for city in search_orders:
        if city.get_name() != root.get_name():
            parent_name = bfs_tree.get_parent(city).get_name()
            msg += city.get_name() + " has parent " + parent_name + "\n"

    return msg


"""
Minimum Spanning Tree:
Starting Node : root_name
"""


def mst(city_road_map, root_name):
    # Retrieve the starting vertex from the root city name
    root = city_road_map.get_vertex(root_name)

    # Call the MST method, which returns an MST containing
    # the MST order of the vertices, starting with root
    mst_tree = city_road_map.get_min_spanning_tree(root)

    # Output root, total weight and mst edge str
    msg = ""
    msg += "Root is " + root_name + "\n"
    msg += ("Total Weight of MST: " + str(round(mst_tree.get_total_weight(), 2)))
    msg += "\n" + mst_tree.get_mst_edge_str()
    
    return msg


"""
ShortestPath Tree:
Starting Node : root_name
"""


def shortest_path(city_road_map, root_name, dest_name):
    # Retrieve the starting vertex from the root city name
    root = city_road_map.get_vertex(root_name)
    dest = city_road_map.get_vertex(dest_name)

    # Call the get_shortest_path method, which returns a short path tree
    # containing all the shortest paths from root to each other city
    short_tree = city_road_map.get_shortest_path(root)

    # If destination is None,
    # Print the Shortest Path from root to all Cities
    if dest is None:
        msg = "Root is " + root.get_name() + "\n"
        msg += short_tree.get_all_paths_str() + "\n\n"

    # Else Print the Shortest Path from root to destination city
    else:
        msg = "Root is " + root.get_name() + "\n"
        msg += "Destination is " + dest.get_name() + "\n"
        msg += short_tree.get_path_str(dest) + "\n\n"

    return msg


"""
Sort the cities by population and display them
"""


def get_key(city):
    return city.get_pop()


def sort_cities(city_road_map):

    cities = city_road_map.get_vertices()

    # Message to return
    msg = ""

    cities.sort(key = get_key)

    # Output each City object information
    for city in cities:
        msg += str(city) + "\n"
        if city == cities[-1]:
            return msg + str(city)


main() 
