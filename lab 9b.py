# Cecilia (yixian) Zhang
# Agent-Based Simulation


class Agent:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.world.grid[new_y][new_x] = self

    def location(self):
        return (self.x, self.y)

class World:
    def __init__(self, width, height, num_agents):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.agents = []
        self.init_agents(num_agents)

    def init_agents(self, num_agents):
        from random import randint

        for _ in range(num_agents):
            while True:
                x, y = randint(0, self.width - 1), randint(0, self.height - 1)
                if self.grid[y][x] is None:
                    agent = Agent(self, x, y)
                    self.grid[y][x] = agent
                    self.agents.append(agent)
                    break

    def find_empty_patch(self, x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.width and 0 <= new_y < self.height and self.grid[new_y][new_x] is None:
                return (new_x, new_y)
        return None

    def update(self):
        from random import shuffle

        shuffle(self.agents)
        for agent in self.agents:
            empty_patch = self.find_empty_patch(agent.x, agent.y)
            if empty_patch:
                old_x, old_y = agent.x, agent.y
                self.grid[old_y][old_x] = None
                agent.move(*empty_patch)
def main():
    world = World(width=10, height=10, num_agents=5)

    for step in range(10):
        world.update()
        print(f"After step {step + 1}:")
        for agent in world.agents:
            print(f"Agent at {agent.location()}")

if __name__ == "__main__":
    main()
