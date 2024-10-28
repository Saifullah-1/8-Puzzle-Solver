import time
from service.Service import Service


class DFS:
    @staticmethod
    def execute(initial_state: int):
        # check if the state is solvable or not
        if not Service.is_solvable(initial_state):
            return False

        # max search depth
        search_depth = 0

        # visited nodes
        visited = set()

        # search frontier
        frontier = [(initial_state, 0)]

        # parent dictionary to trace the path and direction of move
        parent = {initial_state: (None, None)}

        # cost of the goal
        cost = 0

        start = time.time()

        while len(frontier) > 0:
            # get next level state
            state, cost = frontier.pop()

            # mark node as visited
            visited.add(state)

            # check if the state is the goal state
            if state == 12345678:
                break

            # get next states
            children = Service.get_children(state)

            # evaluate the max depth
            search_depth = max(search_depth, cost + 1)

            for child, move in children.items():
                # check if the state is not visited
                if child not in visited and child not in parent:
                    # append the child state to the frontier
                    frontier.append((child, cost + 1))
                    # append the child states to the parent dictionary
                    parent[child] = [state, move]


        end = time.time()
        path, states = Service.get_path(parent)
        expanded_nodes = len(visited)
        running_time = (end - start) * 1000

        return Service.info(running_time, expanded_nodes, path, states, search_depth, cost)