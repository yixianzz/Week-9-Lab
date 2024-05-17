# Cecilia (yixian) Zhang
# Agent-Based Simulation

import random

class Agent:
    def __init__(self, world):
        self.world = world
        self.x, self.y = self.world.get_random_empty_patch()

    def move(self):
        new_x, new_y = self.world.get_random_empty_patch()
        self.world.grid[self.x][self.y] = None  
        self.x, self.y = new_x, new_y
        self.world.grid[self.x][self.y] = self  

class World:
    def __init__(self, width, height, num_agents):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.agents = [Agent(self) for _ in range(num_agents)]
        for agent in self.agents:
            self.grid[agent.x][agent.y] = agent

    def get_random_empty_patch(self):
        empty_patches = [(x, y) for x in range(self.width) for y in range(self.height) if self.grid[x][y] is None]
        return random.choice(empty_patches)

    def step(self):
        for agent in self.agents:
            agent.move()

def main():
    width, height = 3, 3
    num_agents = 2  
    num_steps = 2  

    world = World(width, height, num_agents)
    for _ in range(num_steps):
        world.step()

if __name__ == "__main__":
    main()
