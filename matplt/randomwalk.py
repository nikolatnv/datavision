from random import choice

class RandomWalk():
    def __init__(self, num_points=50):
        self.num_pints = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_pints:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_steps = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_steps = y_direction * y_distance

            if x_steps == 0 and y_steps == 0:
                continue

            x = self.x_values[-1] + x_steps
            y = self.y_values[-1] + y_steps

            self.x_values.append(x)
            self.y_values.append(y)

