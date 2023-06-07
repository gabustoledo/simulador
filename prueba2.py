import random
from datetime import datetime, timedelta
from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer


class Autobus(Agent):
    def __init__(self, unique_id, model,x,y):
        super().__init__(unique_id, model)
        self.velocidad_actual = 1
        self.ocupacion_actual = 0
        self.ocupacion_maxima = 152
        self.posicion = (x, y)

    def step(self):
        if self.velocidad_actual > 0:
            self.move()
            # self.unload_passengers()

    def move(self):
        posibles_destinos = self.model.get_neighborhood(self.posicion, moore=True, include_center=False)
        nuevo_destino = self.model.closest_paradero_destino(self.posicion, posibles_destinos)
        self.posicion = (nuevo_destino[0], nuevo_destino[1])
        self.model.grid.move_agent(self, nuevo_destino)

    def unload_passengers(self):
        peatones_bajar = []
        for peaton in self.model.peatones_en_bus(self):
            if peaton.destino == self.posicion:
                peatones_bajar.append(peaton)

        for peaton in peatones_bajar:
            self.ocupacion_actual -= 1
            self.model.grid.move_agent(peaton, self.posicion)


class Paradero(Agent):
    def __init__(self, unique_id, model, x, y):
        super().__init__(unique_id, model)
        self.posicion = (x, y)

    def step(self):
        pass


class Semaforo(Agent):
    def __init__(self, unique_id, model, x, y):
        super().__init__(unique_id, model)
        self.posicion = (x, y)

    def step(self):
        pass


class Ciudad(Model):
    def __init__(self, N, M):
        self.num_paraderos = N
        self.num_semaforos = M
        self.grid = MultiGrid(400, 400, torus=True)
        self.schedule = RandomActivation(self)
        self.hora_actual = datetime(2023, 6, 6, 6, 0)  # Hora de inicio de la simulación

        self.paraderos = []
        self.semaforos = []
        self.autobuses = []

        # Crear paraderos con posiciones estáticas
        paradero_positions = [(62, 368), (58, 382), (50, 390), (22, 386), (22, 370), (24, 360), (24, 346), (24, 312), (38, 290), (42, 288), (46, 286), (72, 278), (80, 272), (92, 266), (96, 260), (100, 254), (104, 248), (110, 244), (112, 240), (118, 238), (122, 234), (128, 230), (132, 228), (138, 228), (148, 226), (158, 226), (170, 222), (174, 222), (180, 222), (190, 222), (198, 222), (206, 222), (214, 222), (230, 220), (244, 220), (252, 220), (258, 218), (266, 216), (274, 214), (282, 212), (286, 202), (288, 188), (290, 180), (290, 174), (294, 166), (296, 160), (298, 154), (298, 148), (300, 142), (304, 138), (310, 130), (314, 124), (316, 122), (320, 118), (326, 108), (330, 104), (334, 100), (338, 94), (338, 88), (338, 82), (336, 70), (340, 50), (344, 44), (346, 40), (350, 36), (368, 18), (366, 10), (356, 14)]
        for i, pos in enumerate(paradero_positions):
            paradero = Paradero(self.schedule.get_agent_count(), self, pos[0], pos[1])
            self.paraderos.append(paradero)
            self.grid.place_agent(paradero, pos)
            self.schedule.add(paradero)

        # Crear semáforos con posiciones estáticas
        semaforo_positions = [(55, 385), (48, 390), (43, 390), (40, 389), (31, 388), (22, 387), (22, 378), (22, 369), (24, 351), (24, 342), (24, 333), (24, 324), (24, 315), (27, 307), (32, 300), (36, 292), (44, 287), (52, 284), (61, 282), (69, 279), (77, 274), (85, 270), (92, 265), (97, 258), (102, 250), (109, 245), (115, 239), (124, 233), (130, 229), (136, 228), (139, 228), (147, 227), (150, 226), (156, 226), (162, 226), (165, 224), (172, 222), (176, 222), (178, 222), (183, 222), (185, 222), (192, 222), (201, 222), (210, 222), (219, 222), (227, 221), (236, 220), (245, 220), (254, 220), (263, 217), (272, 215), (280, 213), (284, 205), (286, 197), (290, 179), (291, 171), (295, 162), (299, 145), (309, 131), (315, 123), (321, 117), (325, 109), (331, 103), (337, 96), (338, 87), (337, 78), (336, 69), (338, 60), (339, 51), (349, 37), (356, 30), (362, 24), (367, 17), (360, 9)]
        for i, pos in enumerate(semaforo_positions):
            semaforo = Semaforo(self.schedule.get_agent_count(), self, pos[0], pos[1])
            self.semaforos.append(semaforo)
            self.grid.place_agent(semaforo, pos)
            self.schedule.add(semaforo)

        # Crear autobus con posiciones estáticas
        autobus_positions = [(356, 15)]
        for i, pos in enumerate(autobus_positions):
            autobus = Autobus(self.schedule.get_agent_count(), self, pos[0], pos[1])
            self.autobuses.append(autobus)
            self.grid.place_agent(autobus, pos)
            self.schedule.add(autobus)

        self.datacollector = DataCollector(
            model_reporters={"Autobuses en movimiento": lambda m: self.count_moving_buses()},
            agent_reporters={})

        self.running = True

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
        
        autobus = Autobus(self.schedule.get_agent_count(), self, 356, 15)
        self.autobuses.append(autobus)
        self.grid.place_agent(autobus, (356, 15))
        self.schedule.add(autobus)
        
        # Actualizar la hora actual
        self.hora_actual += timedelta(minutes=1)

    def count_moving_buses(self):
        return sum(1 for agent in self.schedule.agents if isinstance(agent, Autobus) and agent.velocidad_actual > 0)

    def get_neighborhood(self, posicion, moore=True, include_center=True):
        return self.grid.get_neighborhood(posicion, moore, include_center)

    def closest_paradero_destino(self, posicion, posibles_destinos):
        # Implementar lógica para obtener el paradero destino más cercano
        # return random.choice(posibles_destinos)
        if posicion[0] == 399:
          x = 0
        else:
          x = posicion[0] + 1
             
        if posicion[1] == 399:
          y = 0
        else:
          y = posicion[1] + 1
        return (x,y)


def agent_portrayal(agent):
    if agent is None:
        return

    if isinstance(agent, Autobus):
        return {"Shape": "rect",
                "Filled": "true",
                "Layer": 0,
                "Color": "red",
                "w": 0.5,
                "h": 0.5}
    elif isinstance(agent, Paradero):
        return {"Shape": "rect",
                "Filled": "true",
                "Layer": 0,
                "Color": "blue",
                "w": 0.5,
                "h": 0.5}
    elif isinstance(agent, Semaforo):
        return {"Shape": "rect",
                "Filled": "true",
                "Layer": 0,
                "Color": "green",
                "w": 0.5,
                "h": 0.5}

def add_autobus(model):
    if model.schedule.steps % 10 == 0:  # Agregar un nuevo autobús cada 10 pasos
        autobus = Autobus(model.current_id, model)
        model.current_id += 1
        x = random.randrange(model.grid.width)
        y = random.randrange(model.grid.height)
        model.grid.place_agent(autobus, (x, y))
        model.schedule.add(autobus)
        
# Configuración de la simulación
num_paraderos = 68
num_semaforos = 5
ciudad = Ciudad(num_paraderos, num_semaforos)

# Definir visualización
# canvas_element = CanvasGrid(lambda x: x.estado, 100, 100, 800, 800)
# chart_element = ChartModule([{"Label": "Autobuses en movimiento", "Color": "#AA0000"}])

# Definir visualización
grid = CanvasGrid(agent_portrayal, 400, 400, 2500, 2500)

# Definir servidor de visualización
server = ModularServer(Ciudad, [grid], "Simulación de Transporte Urbano", {"N": num_paraderos, "M": num_semaforos})

# Iniciar servidor de visualización
server.port = 8521
# server.add_model_behavior(add_autobus)
server.launch()












