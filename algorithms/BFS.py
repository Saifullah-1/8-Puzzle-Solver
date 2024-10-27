import queue
import time
from service.Service import Service


class BFS:
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
        frontier = queue.Queue()

        # parent dictionary to trace the path, cost and direction of move
        parent = {initial_state: (None, None, 0)}

        start = time.time()
        frontier.put(initial_state)

        while not frontier.empty():
            # get next level state
            state = frontier.get()

            # mark node as visited
            visited.add(state)

            # check if the state is the goal state
            if state == 12345678:
                break

            # get next states
            children = Service.get_children(state)

            # get the cost of next level
            cost = parent[state][2] + 1

            # evaluate the max depth
            search_depth = max(search_depth, cost)

            for child, move in children.items():
                # check if the state is not visited
                if child not in visited and child not in parent:
                    # append the child state to the frontier
                    frontier.put(child)
                    # append the child states to the parent dictionary
                    parent[child] = [state, move, cost]

        end = time.time()
        path, states = Service.get_path(parent)
        expanded_nodes = len(visited)
        running_time = (end - start) * 1000
        cost = parent[12345678][2]

        return Service.info(running_time, expanded_nodes, path, states, search_depth, cost)