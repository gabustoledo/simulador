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
            elif self.unique_id == 1:
                self.suma += 5
            else:
                self.suma += 10

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

        model_reporters = {}
        agent2_3_data = [f"Suma agente {i}" for i in range(2, self.num_agents)]

        for i in range(self.num_agents):
            model_reporters[f"Suma agente {i}"] = lambda m, i=i: m.schedule.agents[i].suma

        self.datacollector = DataCollector(model_reporters=model_reporters)
        self.agent2_3_chart = ChartModule([{"Label": label, "Color": "green"} for label in agent2_3_data])

        chart_description = [{"Label": f"Suma agente {i}", "Color": "blue"} for i in range(self.num_agents)]
        self.chart = ChartModule(chart_description)

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)

# Crear el modelo
model = SumModel(num_agents=3)  # Cambiar num_agents a 3 para incluir al agente 0, 1 y 2

# Crear el servidor de visualización
server = ModularServer(SumModel,
                       [model.chart, model.agent2_3_chart],  # Agregar el gráfico del agente 2 y 3 al servidor
                       "SumModel",
                       {"num_agents": 3})  # Cambiar num_agents a 3

# Ejecutar el servidor de visualización
server.port = 8522  # Puerto para acceder al servidor desde el navegador
server.launch()














