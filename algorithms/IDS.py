import time
from service.Service import Service

class IDS:
    @staticmethod
    def execute(initial_state):
        
        # check if the state is solvable or not
        if not Service.is_solvable(initial_state):
            return False
        
        """
        Current depth limit
        Number of overall expanded nodes
        Flag to Indicate if the search is successful
        Starting the timer 
        """
        limit = 0
        expanded_nodes = 0
        succeed = False
        start = time.time()
        
        while not succeed:
            
            # Try to solve with the current limit
            result = IDS.iterate(initial_state, limit)
            
            # if a number is returned, it means that the limit is not enough,
            # and this number is the expanded nodes with this limit
            if type(result) == int: 
                expanded_nodes += result
            else : 
                expanded_nodes += result["expanded_nodes"]
                succeed = True
                break
            
            # increase the depth limit  
            limit += 1
        
        # End of the timer 
        end = time.time()
        running_time = (end - start) * 1000
        # print(f"IDS took {running_time} ms with {expanded_nodes} expanded nodes and path {result['path']} with limit {limit}")
        return Service.info(running_time, expanded_nodes, result["path"], result["states"], limit, limit) 
        
    
    @staticmethod
    def iterate(initial_state, limit):
        
        """
        number of expanded nodes
        search frontier
        parent dictionary to trace the path, direction and cost
        """
        expanded_nodes = 0
        frontier = [(initial_state, 0)]
        parent = {initial_state: [None, None, 0]}

        while len(frontier) > 0:
            
            # get next state to be expanded with its cost
            state_with_cost = frontier.pop()
            state = state_with_cost[0]
            cost = state_with_cost[1]
            # mark node as expanded
            expanded_nodes += 1

            # check if the state is the goal state
            if state == 12345678:
                path, states = Service.get_path(parent)
                return Service.info(0, expanded_nodes, path, states, limit, limit)

            # get next states
            children = Service.get_children(state)
            # get the cost of next level
            cost += 1

            if (cost <= limit):
                for child, move in children.items():
                    # append the child state to the frontier
                    frontier.append((child, cost))
                    if child not in parent.keys() or parent[child][2] > cost:
                        parent[child] = [state, move, cost]
                    """
                    if the child state is not in the parent dictionary or it exists but with higher cost,
                    add this new entry or override it with the new cost,
                    that means that there is a shorter path to this state than the one already exists
                    and hence, this guarantees optimlaity of the solution 
                    as parent dictionary is used to trace the optimal path to the goal state
                    while the frontier keeps the actual depth of the state not the optimal to compare with our limit
                    """
        
        return expanded_nodes

