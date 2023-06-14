import random
import pandas as pd
from mesa.visualization.modules import ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector

# Definir el agente
class SumAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.suma = 0

    def step(self):
        if self.model.schedule.steps % 5 == 0:
            if self.unique_id == 0:
                self.suma += 3
            else:
                self.suma += 5

# Definir el modelo
class SumModel(Model):
    def __init__(self, num_agents):
        self.num_agents = num_agents
        self.schedule = RandomActivation(self)
        self.grid = SingleGrid(1, num_agents, torus=False)

        for i in range(self.num_agents):
            agent = SumAgent(i, self)
            self.schedule.add(agent)
            self.grid.place_agent(agent, (0, i))

        self.datacollector = DataCollector(model_reporters={"Suma agente 0": lambda m: m.schedule.agents[0].suma,
                                                            "Suma agente 1": lambda m: m.schedule.agents[1].suma})

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)

# Crear el modelo
model = SumModel(num_agents=2)

# Definir el gráfico de barras
chart = ChartModule([{"Label": "Suma agente 0", "Color": "blue"},
                     {"Label": "Suma agente 1", "Color": "red"}])

# Crear el servidor de visualización
server = ModularServer(SumModel,
                       [chart],
                       "SumModel",
                       {"num_agents": 2})

# Ejecutar el servidor de visualización
server.port = 8522  # Puerto para acceder al servidor desde el navegador
server.launch()




