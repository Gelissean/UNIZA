import sys


class network():
    class node():
        def __init__(self, id, name):
            self.id = id
            self.name = name
            self.edges = []
            self.antecendent = None
            self.distance = None

    class edge():
        def __init__(self, point_a, point_b, distance):
            self.points = [point_a, point_b]
            self.distance = distance

    def __init__(self):
        self.defined = False
        self.nodes = []
        self.edges = []

    def read_network(self, nodes, edges):
        #create nodes
        file = open(nodes, 'r', encoding="utf-8")
        file.readline()
        file.readline()
        self.node_count = int(file.readline())
        for i in range(self.node_count):
            line = file.readline()
            line = line.split(',')
            line[1] = line[1].split("\"")
            self.nodes.append(self.node(int(line[0]), line[1][1]))
        #create edges
        file = open(edges, 'r', encoding="utf-8")
        file.readline()
        file.readline()
        self.edge_count = int(file.readline())
        for i in range(self.edge_count):
            line = file.readline().split(",")
            for i in range(3):
                line[i] = int(line[i])
            #find first point
            start_id = self.find_node_pos_by_id(line[0])
            if start_id is None:
                exit(-1)
            #find second point
            end_id = self.find_node_pos_by_id(line[1])
            if end_id is None:
                exit(-1)
            self.edges.append(self.edge(self.nodes[start_id], self.nodes[end_id], line[2]))
            #add edges to nodes
            self.nodes[start_id].edges.append(self.edges[-1])
            self.nodes[end_id].edges.append(self.edges[-1])

    def find_node_pos_by_id(self, id):
        for i in range(self.node_count):
            if id == self.nodes[i].id:
                return i
        return None

    def get_closest_edge(self, edges):
        minimum = sys.maxsize
        closest_edge = None
        for edge in edges:
            if edge.points[0].distance is not None:
                new_dist = edge.points[0].distance + edge.distance
            elif edge.points[1].distance is not None:
                new_dist = edge.points[1].distance + edge.distance
            else:
                exit(-1)
            if new_dist < minimum:
                minimum = new_dist
                closest_edge = edge
        return closest_edge

    def get_not_found_node(self, edge):
        for node in self.found:
            if node.id == edge.points[0].id:
                return edge.points[1]
        for node in self.found:
            if node.id == edge.points[1].id:
                return edge.points[0]
        return None

    def cull_edges(self, node, edges):
        found_edges = []
        for edge in edges:
            not_found = 2
            if node.id == edge.points[0].id:
                not_found = 1
            elif node.id == edge.points[1].id:
                not_found = 0
            if not_found < 2:
                if edge.points[not_found] in self.found:
                    found_edges.append(edge)
        for edge in found_edges:
            edges.remove(edge)
        return edges

    def find_all_paths(self, start_id):
        start_node = self.nodes[self.find_node_pos_by_id(start_id)]
        start_node.distance = 0

        self.found = [start_node]
        possible_edges = start_node.edges.copy()
        while possible_edges:
            best_edge = self.get_closest_edge(possible_edges)
            new_node = self.get_not_found_node(best_edge)
            if new_node.id == best_edge.points[0].id:
                new_node.distance = best_edge.points[1].distance + best_edge.distance
                new_node.antecendent = best_edge.points[1]
            else:
                new_node.distance = best_edge.points[0].distance + best_edge.distance
                new_node.antecendent = best_edge.points[0]
            possible_edges = possible_edges + new_node.edges
            possible_edges = self.cull_edges(new_node, possible_edges)
            self.found.append(new_node)

    def print_paths(self):
        final_string = ""
        for node in self.nodes:
            first = True
            distance = node.distance
            while node is not None:
                if first:
                    first = False
                else:
                    final_string = final_string + "-"
                    #print("-", end="")
                final_string = final_string + node.name
                #print(node.name, end="")
                node = node.antecendent
            #print("\t dist: ", distance)
            final_string = final_string + "\t dist: " + str(distance) + '\n'
        return final_string

def help():
    print("program vyzaduje nasledovne argumenty:")
    print("id: int, identifikator pociatocneho uzlu")
    print("uzly: cesta k suboru s uzlami vo formate:")
    print("\t\\n")
    print("\t\\n")
    print("\tpocet_uzlov")
    print("\tid,nazov")
    print("\t...")
    print("hrany: cesta k suboru s uzlami vo formate:")
    print("\t\\n")
    print("\t\\n")
    print("\tpocet_hran")
    print("\tid_prveho_uzla,id_druheho_uzla,dlzka_cesty")
    print("\t...")
    print("vystupny_subor: volitelny argument, cesta k suboru s vysledkami skriptu")

if __name__ == '__main__':
    if (len(sys.argv) > 5) or (len(sys.argv) < 4):
        help()
        exit(0)
    dijkstra = network()
    #dijkstra.read_network("nodes.txt", "edges.txt")
    dijkstra.read_network(sys.argv[2], sys.argv[3])
    dijkstra.find_all_paths(int(sys.argv[1]))
    if(len(sys.argv)>4):
        file = open(sys.argv[4], 'w+')
        file.write(dijkstra.print_paths())
        file.close()
    else:
        print(dijkstra.print_paths())
