class Service:
    @staticmethod
    def count_inversions(initial_state: str):
        """
        Counts the number of inversions in a given state.
        :param initial_state: The initial state.
        :return: Number of inversions.
        """
        inversions = 0
        initial_state = initial_state.replace('0', '')

        for i in range(8):
            for j in range(i + 1, 8):
                if int(initial_state[i]) > int(initial_state[j]):
                    inversions += 1

        return inversions

    @staticmethod
    def is_solvable(initial_state: int):
        """
        Checks if the given initial state is solvable.
        :param initial_state: The initial state to be checked.
        :return: True if the given initial state is solvable, False otherwise.
        """
        inversions = Service.count_inversions(str(initial_state))
        if inversions % 2 == 0:
            return True
        return False

    @staticmethod
    def swap_characters(state: str, ind: int, swap_ind: int):
        """
        Swaps two characters in a given string.

        :param state: The string to be swapped.
        :param ind: The index of the first character.
        :param swap_ind: The index of the second character.
        :return: The new string.
        """
        return (state[:ind] + state[swap_ind] + state[ind + 1:swap_ind]
                + state[ind] + state[swap_ind + 1:])

    @staticmethod
    def get_children(state: int):
        """
        Gets the children of a given state.

        :param state: The current state from which to derive child states.
        :return: A list of child states derived from the given state.
        """
        children = {}
        parent = str(state)
        ind = 0

        # Getting the index of blank tile
        try:
            ind = parent.index('0')
        except ValueError:
            # if the blank tile not in the string append it to the start
            parent = '0' + parent

        # move left
        if ind % 3 > 0:
            child = Service.swap_characters(parent, ind - 1, ind)
            children[int(child)] = "Left"

        # move down
        if ind + 3 <= 8:
            child = Service.swap_characters(parent, ind, ind + 3)
            children[int(child)] = "Down"

        # move right
        if ind % 3 < 2:
            child = Service.swap_characters(parent, ind, ind + 1)
            children[int(child)] = "Right"

        # move up
        if ind - 3 >= 0:
            child = Service.swap_characters(parent, ind - 3, ind)
            children[int(child)] = "Up"

        return children

    @staticmethod
    def get_path(parent):
        """
        Gets the path from the initial state to the goal state.
        :param parent: Dictionary contains all children parents and the direction.
        :return: List of directions and states to the goal state.
        """
        path = []
        states = []
        node = 12345678
        while parent[node][1] is not None:
            states.append(str(parent[node][0]))
            path.append(parent[node][1])
            node = parent[node][0]

        path.reverse()
        states.reverse()
        return path, states

    @staticmethod
    def info(running_time, expanded_nodes, path, states, search_depth, cost):
        """
        :param states: States of the path to the goal.
        :param running_time: Searching running time.
        :param expanded_nodes: Number of expanded nodes.
        :param path: Path to the goal.
        :param search_depth: Max depth of the search tree.
        :param cost: Cost of the goal.
        :return: Object contains information about the solution.
        """
        solution = {
            "expanded_nodes": expanded_nodes,
            "path": path,
            "running_time": running_time,
            "cost": cost,
            "search_depth": search_depth,
            "states": states
        }

        return solution