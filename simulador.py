import random
from datetime import datetime, timedelta
from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation, RandomActivationByType
from mesa.datacollection import DataCollector
from mesa.visualization.modules import CanvasGrid, ChartModule, BarChartModule, PieChartModule
from mesa.visualization.ModularVisualization import ModularServer

from schedule import RandomActivationByTypeFiltered

SEMAFOROS = [(55, 385), (48, 390), (43, 390), (40, 389), (31, 388), (22, 387), (22, 378), (22, 369), (24, 351), (24, 342), (24, 333), (24, 324), (24, 315), (27, 307), (32, 300), (36, 292), (44, 287), (52, 284), (61, 282), (69, 279), (77, 274), (85, 270), (92, 265), (97, 258), (102, 250), (109, 245), (115, 239), (124, 233), (130, 229), (136, 228), (139, 228), (147, 227), (150, 226), (156, 226), (162, 226), (165, 224), (172, 222), (176, 222), (178, 222), (183, 222), (185, 222), (192, 222), (201, 222), (210, 222), (219, 222), (227, 221), (236, 220), (245, 220), (254, 220), (263, 217), (272, 215), (280, 213), (284, 205), (286, 197), (290, 179), (291, 171), (295, 162), (299, 145), (309, 131), (315, 123), (321, 117), (325, 109), (331, 103), (337, 96), (338, 87), (337, 78), (336, 69), (338, 60), (339, 51), (349, 37), (356, 30), (362, 24), (367, 17), (360, 9)]
PARADEROS = [(62, 368), (58, 382), (50, 390), (22, 386), (22, 370), (24, 360), (24, 346), (24, 312), (38, 290), (42, 288), (46, 286), (72, 278), (80, 272), (92, 266), (96, 260), (100, 254), (104, 248), (110, 244), (112, 240), (118, 238), (122, 234), (128, 230), (132, 228), (138, 228), (148, 226), (158, 226), (170, 222), (174, 222), (180, 222), (190, 222), (198, 222), (206, 222), (214, 222), (230, 220), (244, 220), (252, 220), (258, 218), (266, 216), (274, 214), (282, 212), (286, 202), (288, 188), (290, 180), (290, 174), (294, 166), (296, 160), (298, 154), (298, 148), (300, 142), (304, 138), (310, 130), (314, 124), (316, 122), (320, 118), (326, 108), (330, 104), (334, 100), (338, 94), (338, 88), (338, 82), (336, 70), (340, 50), (344, 44), (346, 40), (350, 36), (368, 18), (366, 10), (356, 14)]
RECORRIDO = [(61, 369) ,(60, 370) ,(59, 371) ,(58, 372) ,(58, 373) ,(58, 374) ,(58, 375) ,(58, 376) ,(58, 377) ,(58, 378) ,(58, 379) ,(58, 380) ,(58, 381) ,(58, 382) ,(57, 383) ,(56, 384) ,(55, 385) ,(54, 386) ,(53, 387) ,(52, 388) ,(51, 389) ,(50, 390) ,(49, 390) ,(48, 390) ,(47, 390) ,(46, 390) ,(45, 390) ,(44, 390) ,(43, 390) ,(42, 389) ,(41, 389) ,(40, 389) ,(39, 388) ,(38, 388) ,(37, 388) ,(36, 388) ,(35, 388) ,(34, 388) ,(33, 388) ,(32, 388) ,(31, 388) ,(30, 387) ,(29, 387) ,(28, 387) ,(27, 387) ,(26, 387) ,(25, 387) ,(24, 387) ,(23, 387) ,(22, 387) ,(22, 386) ,(22, 385) ,(22, 384) ,(22, 383) ,(22, 382) ,(22, 381) ,(22, 380) ,(22, 379) ,(22, 378) ,(22, 377) ,(22, 376) ,(22, 375) ,(22, 374) ,(22, 373) ,(22, 372) ,(22, 371) ,(22, 370) ,(22, 369) ,(23, 368) ,(24, 367) ,(24, 366) ,(24, 365) ,(24, 364) ,(24, 363) ,(24, 362) ,(24, 361) ,(24, 360) ,(24, 359) ,(24, 358) ,(24, 357) ,(24, 356) ,(24, 355) ,(24, 354) ,(24, 353) ,(24, 352) ,(24, 351) ,(24, 350) ,(24, 349) ,(24, 348) ,(24, 347) ,(24, 346) ,(24, 345) ,(24, 344) ,(24, 343) ,(24, 342) ,(24, 341) ,(24, 340) ,(24, 339) ,(24, 338) ,(24, 337) ,(24, 336) ,(24, 335) ,(24, 334) ,(24, 333) ,(24, 332) ,(24, 331) ,(24, 330) ,(24, 329) ,(24, 328) ,(24, 327) ,(24, 326) ,(24, 325) ,(24, 324) ,(24, 323) ,(24, 322) ,(24, 321) ,(24, 320) ,(24, 319) ,(24, 318) ,(24, 317) ,(24, 316) ,(24, 315) ,(24, 314) ,(24, 313) ,(24, 312) ,(25, 311) ,(26, 310) ,(27, 309) ,(27, 308) ,(27, 307) ,(28, 306) ,(29, 305) ,(30, 304) ,(31, 303) ,(32, 302) ,(32, 301) ,(32, 300) ,(33, 299) ,(34, 298) ,(35, 297) ,(36, 296) ,(36, 295) ,(36, 294) ,(36, 293) ,(36, 292) ,(37, 291) ,(38, 290) ,(39, 289) ,(40, 288) ,(41, 288) ,(42, 288) ,(43, 287) ,(44, 287) ,(45, 286) ,(46, 286) ,(47, 285) ,(48, 284) ,(49, 284) ,(50, 284) ,(51, 284) ,(52, 284) ,(53, 283) ,(54, 282) ,(55, 282) ,(56, 282) ,(57, 282) ,(58, 282) ,(59, 282) ,(60, 282) ,(61, 282) ,(62, 281) ,(63, 280) ,(64, 279) ,(65, 279) ,(66, 279) ,(67, 279) ,(68, 279) ,(69, 279) ,(70, 278) ,(71, 278) ,(72, 278) ,(73, 277) ,(74, 276) ,(75, 275) ,(76, 274) ,(77, 274) ,(78, 273) ,(79, 272) ,(80, 272) ,(81, 271) ,(82, 270) ,(83, 270) ,(84, 270) ,(85, 270) ,(86, 269) ,(87, 268) ,(88, 267) ,(89, 266) ,(90, 266) ,(91, 266) ,(92, 266) ,(92, 265) ,(93, 264) ,(94, 263) ,(95, 262) ,(96, 261) ,(96, 260) ,(97, 259) ,(97, 258) ,(98, 257) ,(99, 256) ,(100, 255) ,(100, 254) ,(101, 253) ,(102, 252) ,(102, 251) ,(102, 250) ,(103, 249) ,(104, 248) ,(105, 247) ,(106, 246) ,(107, 245) ,(108, 245) ,(109, 245) ,(110, 244) ,(111, 243) ,(112, 242) ,(112, 241) ,(112, 240) ,(113, 239) ,(114, 239) ,(115, 239) ,(116, 238) ,(117, 238) ,(118, 238) ,(119, 237) ,(120, 236) ,(121, 235) ,(122, 234) ,(123, 233) ,(124, 233) ,(125, 232) ,(126, 231) ,(127, 230) ,(128, 230) ,(129, 229) ,(130, 229) ,(131, 228) ,(132, 228) ,(133, 228) ,(134, 228) ,(135, 228) ,(136, 228) ,(137, 228) ,(138, 228) ,(139, 228) ,(140, 227) ,(141, 227) ,(142, 227) ,(143, 227) ,(144, 227) ,(145, 227) ,(146, 227) ,(147, 227) ,(148, 226) ,(149, 226) ,(150, 226) ,(151, 226) ,(152, 226) ,(153, 226) ,(154, 226) ,(155, 226) ,(156, 226) ,(157, 226) ,(158, 226) ,(159, 226) ,(160, 226) ,(161, 226) ,(162, 226) ,(163, 225) ,(164, 224) ,(165, 224) ,(166, 223) ,(167, 222) ,(168, 222) ,(169, 222) ,(170, 222) ,(171, 222) ,(172, 222) ,(173, 222) ,(174, 222) ,(175, 222) ,(176, 222) ,(177, 222) ,(178, 222) ,(179, 222) ,(180, 222) ,(181, 222) ,(182, 222) ,(183, 222) ,(184, 222) ,(185, 222) ,(186, 222) ,(187, 222) ,(188, 222) ,(189, 222) ,(190, 222) ,(191, 222) ,(192, 222) ,(193, 222) ,(194, 222) ,(195, 222) ,(196, 222) ,(197, 222) ,(198, 222) ,(199, 222) ,(200, 222) ,(201, 222) ,(202, 222) ,(203, 222) ,(204, 222) ,(205, 222) ,(206, 222) ,(207, 222) ,(208, 222) ,(209, 222) ,(210, 222) ,(211, 222) ,(212, 222) ,(213, 222) ,(214, 222) ,(215, 222) ,(216, 222) ,(217, 222) ,(218, 222) ,(219, 222) ,(220, 221) ,(221, 221) ,(222, 221) ,(223, 221) ,(224, 221) ,(225, 221) ,(226, 221) ,(227, 221) ,(228, 220) ,(229, 220) ,(230, 220) ,(231, 220) ,(232, 220) ,(233, 220) ,(234, 220) ,(235, 220) ,(236, 220) ,(237, 220) ,(238, 220) ,(239, 220) ,(240, 220) ,(241, 220) ,(242, 220) ,(243, 220) ,(244, 220) ,(245, 220) ,(246, 220) ,(247, 220) ,(248, 220) ,(249, 220) ,(250, 220) ,(251, 220) ,(252, 220) ,(253, 220) ,(254, 220) ,(255, 219) ,(256, 218) ,(257, 218) ,(258, 218) ,(259, 217) ,(260, 217) ,(261, 217) ,(262, 217) ,(263, 217) ,(264, 216) ,(265, 216) ,(266, 216) ,(267, 215) ,(268, 215) ,(269, 215) ,(270, 215) ,(271, 215) ,(272, 215) ,(273, 214) ,(274, 214) ,(275, 213) ,(276, 213) ,(277, 213) ,(278, 213) ,(279, 213) ,(280, 213) ,(281, 212) ,(282, 212) ,(283, 211) ,(284, 210) ,(284, 209) ,(284, 208) ,(284, 207) ,(284, 206) ,(284, 205) ,(285, 204) ,(286, 203) ,(286, 202) ,(286, 201) ,(286, 200) ,(286, 199) ,(286, 198) ,(286, 197) ,(287, 196) ,(288, 195) ,(288, 194) ,(288, 193) ,(288, 192) ,(288, 191) ,(288, 190) ,(288, 189) ,(288, 188) ,(289, 187) ,(290, 186) ,(290, 185) ,(290, 184) ,(290, 183) ,(290, 182) ,(290, 181) ,(290, 180) ,(290, 179) ,(290, 178) ,(290, 177) ,(290, 176) ,(290, 175) ,(290, 174) ,(291, 173) ,(291, 172) ,(291, 171) ,(292, 170) ,(293, 169) ,(294, 168) ,(294, 167) ,(294, 166) ,(295, 165) ,(295, 164) ,(295, 163) ,(295, 162) ,(296, 161) ,(296, 160) ,(297, 159) ,(298, 158) ,(298, 157) ,(298, 156) ,(298, 155) ,(298, 154) ,(298, 153) ,(298, 152) ,(298, 151) ,(298, 150) ,(298, 149) ,(298, 148) ,(299, 147) ,(299, 146) ,(299, 145) ,(300, 144) ,(300, 143) ,(300, 142) ,(301, 141) ,(302, 140) ,(303, 139) ,(304, 138) ,(305, 137) ,(306, 136) ,(307, 135) ,(308, 134) ,(309, 133) ,(309, 132) ,(309, 131) ,(310, 130) ,(311, 129) ,(312, 128) ,(313, 127) ,(314, 126) ,(314, 125) ,(314, 124) ,(315, 123) ,(316, 122) ,(317, 121) ,(318, 120) ,(319, 119) ,(320, 118) ,(321, 117) ,(322, 116) ,(323, 115) ,(324, 114) ,(325, 113) ,(325, 112) ,(325, 111) ,(325, 110) ,(325, 109) ,(326, 108) ,(327, 107) ,(328, 106) ,(329, 105) ,(330, 104) ,(331, 103) ,(332, 102) ,(333, 101) ,(334, 100) ,(335, 99) ,(336, 98) ,(337, 97) ,(337, 96) ,(338, 95) ,(338, 94) ,(338, 93) ,(338, 92) ,(338, 91) ,(338, 90) ,(338, 89) ,(338, 88) ,(338, 87) ,(338, 86) ,(338, 85) ,(338, 84) ,(338, 83) ,(338, 82) ,(337, 81) ,(337, 80) ,(337, 79) ,(337, 78) ,(336, 77) ,(336, 76) ,(336, 75) ,(336, 74) ,(336, 73) ,(336, 72) ,(336, 71) ,(336, 70) ,(336, 69) ,(337, 68) ,(338, 67) ,(338, 66) ,(338, 65) ,(338, 64) ,(338, 63) ,(338, 62) ,(338, 61) ,(338, 60) ,(339, 59) ,(339, 58) ,(339, 57) ,(339, 56) ,(339, 55) ,(339, 54) ,(339, 53) ,(339, 52) ,(339, 51) ,(340, 50) ,(341, 49) ,(342, 48) ,(343, 47) ,(344, 46) ,(344, 45) ,(344, 44) ,(345, 43) ,(346, 42) ,(346, 41) ,(346, 40) ,(347, 39) ,(348, 38) ,(349, 37) ,(350, 36) ,(351, 35) ,(352, 34) ,(353, 33) ,(354, 32) ,(355, 31) ,(356, 30) ,(357, 29) ,(358, 28) ,(359, 27) ,(360, 26) ,(361, 25) ,(362, 24) ,(363, 23) ,(364, 22) ,(365, 21) ,(366, 20) ,(367, 19) ,(368, 18) ,(367, 17) ,(366, 16) ,(366, 15) ,(366, 14) ,(366, 13) ,(366, 12) ,(366, 11) ,(366, 10) ,(365, 9) ,(364, 9) ,(363, 9) ,(362, 9) ,(361, 9) ,(360, 9) ,(359, 10) ,(358, 11) ,(357, 12) ,(356, 13) ,(356, 14)]
VEL_MAX = 11.11 # m/s 40km/h
VEL_MAX_PUNTA = 5.56  # m/s 20km/h
ACELERACION = VEL_MAX/30
ACELERACION_PUNTA = VEL_MAX_PUNTA/20
DESACELERACION = -VEL_MAX/4


class Autobus(Agent):
    def __init__(self, unique_id, model,x,y):
        super().__init__(unique_id, model)
        self.velocidad_actual = 0
        self.ocupacion_actual = 0
        self.ocupacion_maxima = 152
        self.movimiento_actual = 0 #612
        self.posicion = (x,y)
        self.distancia_total = 0
        self.destinos = []

    def step(self):
        self.move()

    def move(self):
        if (ciudad.hora_actual >= datetime(2023, 6, 6, 7, 0) and ciudad.hora_actual <= datetime(2023, 6, 6, 8, 59)) or (ciudad.hora_actual >= datetime(2023, 6, 6, 18, 0) and datetime(2023, 6, 6, 19, 59)):
            Velocidad = VEL_MAX_PUNTA
            Accel = ACELERACION_PUNTA
        else:
            Velocidad = VEL_MAX
            Accel = ACELERACION
        nuevo = self.movimiento_actual
        if self.posicion in SEMAFOROS:
            agente = self.model.grid[self.posicion[0]][self.posicion[1]]
            aux = agente[0]
            if self.posicion == aux.posicion:
                if aux.Color == "green":
                    if self.velocidad_actual < Velocidad:
                        self.velocidad_actual = self.velocidad_actual + Accel * 10
                    
                    if self.velocidad_actual >= Velocidad:
                        self.velocidad_actual = Velocidad
                    distancia = self.velocidad_actual * 10 + 0.5 * Accel * 100
                    self.distancia_total += distancia
                    nuevo = int(self.distancia_total/44)
                    if nuevo >= 612:
                        nuevo = 0
                    
                else:
                    self.velocidad_actual = 0
                    distancia = 0
                    nuevo = self.movimiento_actual
                    
        else:
            if self.velocidad_actual < Velocidad:
                self.velocidad_actual = self.velocidad_actual + Accel * 10
                
            if self.velocidad_actual >= Velocidad:
                self.velocidad_actual = Velocidad
            distancia = self.velocidad_actual * 10 + 0.5 * Accel * 100
            self.distancia_total += distancia
            nuevo = int(self.distancia_total/44)
            if nuevo >= 612:
                nuevo = 0
                


        i = self.movimiento_actual
        while i < nuevo:
            aux = RECORRIDO[i]
            if aux in SEMAFOROS:
                for semaforo in SEMAFOROS:
                    agente = self.model.grid[semaforo[0]][semaforo[1]]
                    if agente[0].posicion == aux:
                        if agente[0].Color == "red":
                            nuevo = i - 1
                            self.distancia_total = nuevo * 44
                            self.velocidad_actual = 0
                        else:
                            i+=1
            else:
                i+=1

        self.movimiento_actual = nuevo
        if RECORRIDO[nuevo] in SEMAFOROS:
            nuevo = nuevo - 1
        nuevo_destino = RECORRIDO[nuevo]
        
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

class Peaton(Agent):
    def __init__(self, unique_id, model, x, y, origen, destino, hora):
        super().__init__(unique_id, model)
        self.posicion = (x, y)
        self.paraderoOrigen = origen # 0 - 66
        self.paraderoDestino = destino # 1 - 67
        self.enParadero = True
        self.enDestino = False
        self.horaLLegada = hora


    def step(self):
        pass
    
class Paradero(Agent):
    def __init__(self, unique_id, model, x, y):
        super().__init__(unique_id, model)
        self.posicion = (x, y)
        self.peatones = []
        self.cant_peatones = 0

    def step(self):
        pass



class Semaforo(Agent):
    def __init__(self, unique_id, model, x, y):
        super().__init__(unique_id, model)
        self.posicion = (x, y)
        self.Color = "red"
        self.timer = 2 + random.randint(1,10)

    def step(self):
        #  pass
        
        if self.Color == "green":
           if self.model.schedule.steps % 6 == 0 and self.model.schedule.steps != 0:
               self.Color = "red"
        else:
            if self.model.schedule.steps % self.timer == 0 and self.model.schedule.steps != 0:
                self.Color = "green" if self.Color == "red" else "red"  
        

class Ciudad(Model):
    def __init__(self, N, M):
        self.num_paraderos = N
        self.num_semaforos = M
        self.personaparadero = 0
        self.personaenbus = 0
        self.grid = MultiGrid(400, 400, torus=True)
        # self.schedule = RandomActivation(self)
        self.schedule = RandomActivationByType(self)
        self.hora_actual = datetime(2023, 6, 6, 6, 0)  # Hora de inicio de la simulación

        self.paraderos = []
        self.semaforos = []
        self.autobuses = []
        self.peatones = []
        self.tiemposDeEspera = []
        self.tiemposDeRecorrido = []

        # Crear paraderos con posiciones estáticas
        for i, pos in enumerate(PARADEROS):
            paradero = Paradero(self.schedule.get_agent_count(), self, pos[0], pos[1])
            self.paraderos.append(paradero)
            self.grid.place_agent(paradero, pos)
            self.schedule.add(paradero)

        # Crear semáforos con posiciones estáticas
        for i, pos in enumerate(SEMAFOROS):
            semaforo = Semaforo(self.schedule.get_agent_count(), self, pos[0], pos[1])
            self.semaforos.append(semaforo)
            self.grid.place_agent(semaforo, pos)
            self.schedule.add(semaforo)

        # Crear autobus con posiciones estáticas
        autobus_positions = [(61, 369)]
        for i, pos in enumerate(autobus_positions):
            autobus = Autobus(self.schedule.get_agent_count(), self, pos[0], pos[1])
            self.autobuses.append(autobus)
            self.grid.place_agent(autobus, pos)
            self.schedule.add(autobus)

        # self.datacollector = DataCollector(
        #     model_reporters={"Autobuses en movimiento": lambda m: self.count_moving_buses()},
        #     agent_reporters={})


        self.scheduleB = RandomActivationByTypeFiltered(self)

        self.datacollector = DataCollector(
            {
                "Personas en paradero": lambda m: m.scheduleB.get_type_count(self.personaparadero),
                "Personas en bus": lambda m: m.scheduleB.get_type_count(self.personaenbus)
             }
            )

        self.running = True

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
        # Escenario real cada 10 min una micro
        #
        if self.schedule.steps % 60 == 0:
            autobus = Autobus(self.schedule.get_agent_count(), self, 61, 369)
            self.autobuses.append(autobus)
            self.grid.place_agent(autobus, (61, 369))
            self.schedule.add(autobus)
            
        # Actualizar la hora actual
        self.hora_actual += timedelta(seconds=10)

        # Horarios

        # Horarios Hora Baja
        baja1 = datetime(2023, 6, 6, 6, 0)
        baja2 = datetime(2023, 6, 6, 6, 59)
        baja3 = datetime(2023, 6, 6, 20, 45)
        baja4 = datetime(2023, 6, 6, 23, 0)

        # Horarios Hora Valle
        valle1 = datetime(2023, 6, 6, 9, 0)
        valle2 = datetime(2023, 6, 6, 17, 59)
        valle3 = datetime(2023, 6, 6, 20, 0)
        valle4 = datetime(2023, 6, 6, 20, 44)

        # Horarios Hora Punta
        punta1 = datetime(2023, 6, 6, 7, 0)
        punta2 = datetime(2023, 6, 6, 8, 59)
        punta3 = datetime(2023, 6, 6, 18, 0)
        punta4 = datetime(2023, 6, 6, 19, 59)

        print("Personas en paradero = ", self.personaparadero)
        print("Personas en bus = ", self.personaenbus)
        
        if( (self.hora_actual > baja1 and self.hora_actual < baja2) or (self.hora_actual > baja3 and self.hora_actual < baja4)):
            for paradero in self.paraderos:
                if self.schedule.steps % 18 == 0:
                    flag = True
                    while flag:
                        paradero_origen = random.randint(0, 66)
                        paradero_destino = random.randint(1, 67)
                        if(paradero_origen < paradero_destino):
                            flag = False
                    paradero_origen_cordenadas = PARADEROS[paradero_origen]
                    x_peaton = paradero_origen_cordenadas[0]
                    y_peaton = paradero_origen_cordenadas[1]
                    peaton = Peaton(self.schedule.get_agent_count(), self, x_peaton, y_peaton, paradero_origen, paradero_destino, self.hora_actual)
                    self.personaparadero = self.personaparadero + 1
                    self.peatones.append(peaton)
                    self.schedule.add(peaton)
                    paradero.cant_peatones += 1
        elif( (self.hora_actual > valle1 and self.hora_actual < valle2) or (self.hora_actual > valle3 and self.hora_actual < valle4)):
            for paradero in self.paraderos:
                if self.schedule.steps % 6 == 0:
                    flag = True
                    while flag:
                        paradero_origen = random.randint(0, 66)
                        paradero_destino = random.randint(1, 67)
                        if(paradero_origen < paradero_destino):
                            flag = False
                    paradero_origen_cordenadas = PARADEROS[paradero_origen]
                    x_peaton = paradero_origen_cordenadas[0]
                    y_peaton = paradero_origen_cordenadas[1]
                    peaton = Peaton(self.schedule.get_agent_count(), self, x_peaton, y_peaton, paradero_origen, paradero_destino)
                    self.personaparadero = self.personaparadero + 1
                    self.peatones.append(peaton)
                    self.schedule.add(peaton)
                    paradero.cant_peatones += 1
        elif( (self.hora_actual > punta1 and self.hora_actual < punta2) or (self.hora_actual > punta3 and self.hora_actual < punta4)):
            for paradero in self.paraderos:
                if self.schedule.steps % 2 == 0:
                    flag = True
                    while flag:
                        paradero_origen = random.randint(0, 66)
                        paradero_destino = random.randint(1, 67)
                        if(paradero_origen < paradero_destino):
                            flag = False
                    paradero_origen_cordenadas = PARADEROS[paradero_origen]
                    x_peaton = paradero_origen_cordenadas[0]
                    y_peaton = paradero_origen_cordenadas[1]
                    peaton = Peaton(self.schedule.get_agent_count(), self, x_peaton, y_peaton, paradero_origen, paradero_destino)
                    self.personaparadero = self.personaparadero + 1
                    self.peatones.append(peaton)
                    self.schedule.add(peaton)
                    paradero.cant_peatones += 1
        
        # Realizar subida de personas
        for autobus in self.autobuses:
            # Verificar si el autobus esta en algun paradero
            enParadero = False
            if autobus.posicion in PARADEROS:
                enParadero = True
                paradero_indice = PARADEROS.index(autobus.posicion)
            if(enParadero):
                for peaton in self.peatones:
                    # peaton_indice es para eliminar el peaton solo si se sube a la micro
                    peaton_indice = self.peatones.index(peaton)
                    # Si la micro esta en una posicione del peaton (Osea paradero)
                    if(peaton.posicion == autobus.posicion):
                        # Se resta el peaton del paradero y se suma al autobus
                        autobus.ocupacion_actual += 1
                        self.paraderos[paradero_indice].cant_peatones -= 1
                        # Se agrega un destino a la micro y la hora en la que se subio, esto para obtener
                        # la metrica de tiempo en que se demoro
                        # Primero se extrae la cordenada del paradero
                        paradero_indice_destino = peaton.paraderoDestino
                        coordenada_paradero_destino = PARADEROS[paradero_indice_destino]
                        autobus.destinos.append([coordenada_paradero_destino, self.hora_actual])
                        # Y luego se elimina el peaton
                        del self.peatones[peaton_indice]
                        

        """
        # Realizar bajada de personas
        for autobus in self.autobuses:
            # Verificar si el autobus esta en algun paradero
            enParadero = False
            if autobus.posicion in PARADEROS:
                enParadero = True
                paradero_indice = PARADEROS.index(autobus.posicion)
                coordenada_paradero = PARADEROS[paradero_indice]
            if(enParadero):
                # Lista de destinos del autobus
                destinos = autobus.destinos
                # Comparar cordenadas del paradero con los de destino del bus                
                for destino in destinos:
                    if(destino[0] == coordenada_paradero):
                        self.tiemposDeRecorrido.append(destino[1] - self.hora_actual)
                        autobus.ocupacion_actual -= 1
                    
        
        
        """



                        
                 
                
        
            
        #-------------

    def count_moving_buses(self):
        return sum(1 for agent in self.schedule.agents if isinstance(agent, Autobus) and agent.velocidad_actual > 0)

    def get_neighborhood(self, posicion, moore=True, include_center=True):
        return self.grid.get_neighborhood(posicion, moore, include_center)

    def closest_paradero_destino(self, posicion,movimiento_actual):

        movimiento_actual += 1
        if movimiento_actual == 612:
            movimiento_actual = 0
        
        return RECORRIDO[movimiento_actual],movimiento_actual

def agent_portrayal(agent):
    if agent is None:
        return

    if isinstance(agent, Autobus):
        return {"Shape": "rect",
                "Filled": "true",
                "Layer": 0,
                "Color": "black",
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
        if agent.Color == "red":
            Color = "red"
        else:
            Color = "green"
        return {"Shape": "rect",
                "Filled": "true",
                "Layer": 0,
                "Color": Color,
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

COLORS = {"Personas en paradero": "#00AA00", "Personas en bus": "#0000AA"}

personas = PieChartModule([{"Label": label, "Color": color} for (label, color) in COLORS.items()])


# Definir servidor de visualización
server = ModularServer(Ciudad, [grid, personas], "Simulación de Transporte Urbano", {"N": num_paraderos, "M": num_semaforos})

# Iniciar servidor de visualización
server.port = 8521
# server.add_model_behavior(add_autobus)
server.launch()












