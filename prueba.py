import random
import matplotlib.pyplot as plt
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid

class MyAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.attribute = 0

    def receive_random_amount(self):
        amount = random.randint(1, 10)
        self.attribute += amount

    def step(self):
        self.receive_random_amount()

def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "r": 0.5, "Filled": "true", "Color": "red"}
    return portrayal

class MyModel(Model):
    def __init__(self, num_agents):
        self.num_agents = num_agents
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(1, 1, False)

        for i in range(self.num_agents):
            a = MyAgent(i, self)
            self.schedule.add(a)
            self.grid.place_agent(a, (0, 0))

        self.datacollector = DataCollector(
            model_reporters={"Agent Attribute": lambda m: [agent.attribute for agent in self.schedule.agents]}
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

def agent_attribute_histogram(model):
    agent_attributes = model.datacollector.get_model_vars_dataframe()["Agent Attribute"].values[-1]
    plt.hist(agent_attributes, bins=range(11), align='left', rwidth=0.8, color='blue')
    plt.xlabel('Attribute Value')
    plt.ylabel('Frequency')
    plt.xticks(range(11))
    plt.title('Agent Attribute Histogram')

    # Save the histogram to a file (optional)
    # plt.savefig('agent_attribute_histogram.png')

    plt.show()

# Crear el modelo con 3 agentes
model = MyModel(3)

# Definir el módulo de visualización para el grid
grid = CanvasGrid(agent_portrayal, 1, 1, 300, 200)

# Crear el servidor de visualización
server = ModularServer(MyModel, [grid], "My Model", {"num_agents": 3})

# Agregar el evento del histograma
server.schedule_repeating_event(agent_attribute_histogram, 1)

# Ejecutar el servidor de visualización
server.port = 8522  # Puerto para acceder al servidor (puedes cambiarlo si lo deseas)
server.launch()




