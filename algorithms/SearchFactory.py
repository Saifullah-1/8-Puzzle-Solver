from algorithms.BFS import BFS
from algorithms.DFS import DFS


class SearchFactory:
    @staticmethod
    def create_search_algorithm(search_algorithm, initial_state):
        if search_algorithm.upper() == "DFS":
            return DFS().execute(initial_state)
        elif search_algorithm.upper() == "BFS":
            return BFS().execute(initial_state)