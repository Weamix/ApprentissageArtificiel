import island


class Pirate:
    def __init__(self, island):
        self.position = island.choose_random_point_in_map()

    def move_to(self, position):
        self.position = position
        print("move to :", position)

    def move_to_random_action(self, island):
        neighbours = island.neighbours_for_position(self.position[0], self.position[1])
        print("\nneighbors :", neighbours)
        n = island.sort_neighbours_exclude_elements_out_map(neighbours)
        print("sorted neighbors :", n)
        random_value = island.choose_random_action_in_neighbours(n)
        print("random_value :", random_value)
        self.move_to(n[random_value])

    def move_to_best_action(self, island):
        neighbours = island.neighbours_for_position(self.position[0], self.position[1])
        print("\nneighbors :", neighbours)
        values = island.values_for_neighbours_with_negative_elements_out_map(island.matrix, neighbours)
        print("values :", values)
        best_action = max(values)
        print("best_action :", best_action)
        value_best_action = values.index(best_action)
        print("value_best_action", value_best_action)
        self.move_to(neighbours[value_best_action])

    def found_tresor(self, island):
        return self.position == island.tresor
