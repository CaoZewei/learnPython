from random import choice

class RandomWalk():
    def __init__(self,num_point = 5000) -> None:
        self.num_point =num_point

        self.x =[0]
        self.y =[0]
        self.get_step()

    def fill_walk(self):
        while len(self.x) < self.num_point:
            x_step = self.get_step()
            y_step = self.get_step()

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction*y_distance

            if x_step ==0 and y_step ==0:
                continue

            next_x = self.x[-1]+x_step
            next_y = self.y[-1]+y_step

            self.x.append(next_x)
            self.y.append(next_y)

    def get_step(self):
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4])
        step = direction*distance
        return step


