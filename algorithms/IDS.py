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
            # print(f"limit: {limit}")
            result = IDS.iterate(initial_state, limit)
            
            # add the new number of expanded nodes and check if it was a successfull search
            expanded_nodes += result["expanded_nodes"]
            if result["path"] != "failed":
                succeed = True
                break
            
            # increase the depth limit  
            limit += 1
        
        # End of the timer 
        end = time.time()
        running_time = (end - start) * 1000
        print(f"IDS took {running_time} ms with {expanded_nodes} expanded nodes and path {result['path']} with limit {limit}")
        return Service.info(running_time, expanded_nodes, result["path"], limit, limit) 
        
    
    @staticmethod
    def iterate(initial_state, limit):
        
        """
        number of expanded nodes
        search frontier
        parent dictionary to trace the path, cost and direction of move
        """
        expanded_nodes = 0
        frontier = [initial_state]
        parent = {initial_state: [None, None, 0]}

        while len(frontier) > 0:
            
            # get next level state
            state = frontier.pop()
            # mark node as expanded
            expanded_nodes += 1

            # check if the state is the goal state
            if state == 12345678:
                # print("Found it!!!!!")
                return Service.info(0, expanded_nodes, Service.get_path(parent), limit, limit)

            # get next states
            children = Service.get_children(state)
            # get the cost of next level
            cost = parent[state][2] + 1

            if (cost <= limit):
                for child, move in children.items():
                    # append the child state to the frontier
                    frontier.append(child)
                    if limit == 22 :
                        print(f"child: {child}")
                    # print(f"child: {child}")
                    # append the child states to the parent dictionary if it's new
                    # if child not in parent:
                    parent[child] = [state, move, cost]
                    # parent[child][2] = cost
                    # if the child state is already in the parent dictionary, only the cost is updated not to stuck in a loop,
                    # the cost won't affect as the steps will be the limit depth,
                    # while the parent of the state not changed guarantees that the path is the shortest 
        
        return Service.info("failed", expanded_nodes, "failed", "failed", "failed")
