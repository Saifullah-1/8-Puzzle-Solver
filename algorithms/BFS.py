import queue
import time
from service.Service import Service


class BFS:
    @staticmethod
    def execute(initial_state: int):
        # check if the state is solvable or not
        if not Service.is_solvable(initial_state):
            return False

        # visited nodes
        visited = set()

        # search frontier
        frontier = queue.Queue()

        # parent dictionary to trace the path and direction of move
        parent = {initial_state: (None, None)}

        start = time.time()
        frontier.put((initial_state, 0))

        # cost of goal
        cost = 0

        while not frontier.empty():
            # get next level state
            state, cost = frontier.get()

            # mark node as visited
            visited.add(state)

            # check if the state is the goal state
            if state == 12345678:
                break

            # get next states
            children = Service.get_children(state)

            for child, move in children.items():
                # check if the state is not visited
                if child not in visited and child not in parent:
                    # append the child state to the frontier
                    frontier.put((child, cost + 1))
                    # append the child states to the parent dictionary
                    parent[child] = [state, move]

        end = time.time()
        path, states = Service.get_path(parent)
        expanded_nodes = len(visited)
        running_time = (end - start) * 1000

        return Service.info(running_time, expanded_nodes, path, states, cost, cost)