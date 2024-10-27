import time
from heapdict import heapdict
from service.Service import Service

class Informed:
    
    @staticmethod
    def execute(initial_state, heuristic_function):
        
        # check if the state is solvable or not
        if not Service.is_solvable(initial_state):
            return False
        
        """
        initialize the frontier with the initial state, contains: cost and state
        max search depth
        visited states
        parent dictionary to trace the path, cost and direction of move
        starts the timer
        """
        frontier = heapdict()
        frontier.put(Service.heuristic_function(initial_state), initial_state)
        search_depth = 0
        visited = set()
        parent = {initial_state: (None, None, 0)}
        start = time.time()
        
        while len(frontier) > 0:
            
            # state to be expanded
            current = frontier.peekitem()
            state = current[0]
            # add the state to the visited set
            visited.add(state)
            # check if the state is the goal state
            if state == 12345678:
                break
            
            # getting the children of the state
            children = Service.get_children(state)
            # depth of next states (children of the current state)
            depth = parent[state][2] + 1 
            # updating the search depth
            search_depth = max(search_depth, depth)
            
            for child, move in children.items():
                # if the child is visited, skip it
                if child in visited:
                    continue
                # getting the total estimated cost for this child (heuristic + depth)
                total_cost = depth + heuristic_function(child)
                # if it's in the frontier, check if the new cost is less than the old cost
                if child in frontier:
                    if total_cost < frontier[child]:
                        frontier[child] = total_cost
                    else:
                        continue
                # if neither visited nor in the frontier, add it to the frontier
                frontier[child] = total_cost
                parent[child] = [state, move, depth]
        
        end = time.time()
        path = Service.get_path(parent)
        expanded_nodes = len(visited)
        running_time = (end - start) * 1000
        cost = parent[12345678][2]
        
        return Service.info(running_time, expanded_nodes, path, search_depth, cost)
