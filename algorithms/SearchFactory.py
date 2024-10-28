from algorithms.BFS import BFS
from algorithms.DFS import DFS
from algorithms.IDS import IDS
from algorithms.Informed import Informed
from service.Service import Service


class SearchFactory:
    @staticmethod
    def create_search_algorithm(search_algorithm, initial_state):
        if search_algorithm.upper() == "DFS":
            return DFS().execute(initial_state)
        elif search_algorithm.upper() == "BFS":
            return BFS().execute(initial_state)
        elif search_algorithm.upper() == "IDS":
            return IDS().execute(initial_state)
        elif search_algorithm.upper() == "A*(EUCLIDEAN)":
            return Informed().execute(initial_state, Service.euclidean_distance)
        elif search_algorithm.upper() == "A*(MANHAATTEN)":
            return Informed().execute(initial_state, Service.manhattan_distance)