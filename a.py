def create_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [0] * cols
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

"""
def simulate_movement(matrix, initial_position, final_position):
    
    print_matrix(matrix)
    print("")
    # Obtiene el tamaño de la matriz
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Verifica si la posición inicial y final están dentro de los límites de la matriz
    if (initial_position[0] < 0 or initial_position[0] >= rows or
            initial_position[1] < 0 or initial_position[1] >= cols or
            final_position[0] < 0 or final_position[0] >= rows or
            final_position[1] < 0 or final_position[1] >= cols):
        print("Las posiciones inicial y final están fuera de los límites de la matriz.")
        return
    
    
    # Simula el movimiento
    current_position = initial_position
    matrix[current_position[0]][current_position[1]] = 1
    
    print_matrix(matrix)
    print("")
    
    while current_position != final_position:
        # Mueve el punto hacia la posición final
        if current_position[0] < final_position[0]:
            current_position[0] += 1
        elif current_position[0] > final_position[0]:
            current_position[0] -= 1
        if current_position[1] < final_position[1]:
            current_position[1] += 1
        elif current_position[1] > final_position[1]:
            current_position[1] -= 1
        
        # Marca la posición actual en la matriz
        matrix[current_position[0]][current_position[1]] = 1

        print_matrix(matrix)
        print("")
        
    # Imprime la matriz resultante
    print_matrix(matrix)
"""

def simulate_movement(initial_position, final_position):
    
    # Obtiene el tamaño de la matriz
    rows = 400
    cols = 400
    
    # Verifica si la posición inicial y final están dentro de los límites de la matriz
    if (initial_position[0] < 0 or initial_position[0] >= rows or
            initial_position[1] < 0 or initial_position[1] >= cols or
            final_position[0] < 0 or final_position[0] >= rows or
            final_position[1] < 0 or final_position[1] >= cols):
        print("Las posiciones inicial y final están fuera de los límites de la matriz.")
        return
    
    # Simula el movimiento
    current_position = (initial_position[0],initial_position[1])
    #matrix[current_position[0]][current_position[1]] = 1

    x = initial_position[0]
    y = initial_position[1]
    # Mueve el punto hacia la posición final
    if current_position[0] < final_position[0]:
        x = current_position[0] + 1
    elif current_position[0] > final_position[0]:
        x = current_position[0] - 1
    if current_position[1] < final_position[1]:
        y = current_position[1] + 1
    elif current_position[1] > final_position[1]:
        y = current_position[1] - 1
        
    current_position = (x,y)
    # Marca la posición actual en la matriz

    #matrix[x][y] = 1

    #print(current_position[0], current_position[1])
    #print_matrix(matrix)
    
    return (x, y)
        

# Ejemplo de uso

lista = ((62, 368), (58, 382), (55, 385), (50, 390), (48, 390), (43, 390), (40, 389), (31, 388), (22, 387), (22, 386), (22, 378), (22, 370), (22, 369), (24, 360), (24, 351), (24, 346), (24, 342), (24, 333), (24, 324), (24, 315), (24, 312), (27, 307), (32, 300), (36, 292), (38, 290), (42, 288), (44, 287), (46, 286), (52, 284), (61, 282), (69, 279), (72, 278), (77, 274), (80, 272), (85, 270), (92, 266), (92, 265), (96, 260), (97, 258), (100, 254), (102, 250), (104, 248), (109, 245), (110, 244), (112, 240), (115, 239), (118, 238), (122, 234), (124, 233), (128, 230), (130, 229), (132, 228), (136, 228), (138, 228), (139, 228), (147, 227), (148, 226), (150, 226), (156, 226), (158, 226), (162, 226), (165, 224), (170, 222), (172, 222), (174, 222), (176, 222), (178, 222), (180, 222), (183, 222), (185, 222), (190, 222), (192, 222), (198, 222), (201, 222), (206, 222), (210, 222), (214, 222), (219, 222), (227, 221), (230, 220), (236, 220), (244, 220), (245, 220), (252, 220), (254, 220), (258, 218), (263, 217), (266, 216), (272, 215), (274, 214), (280, 213), (282, 212), (284, 205), (286, 202), (286, 197), (288, 188), (290, 180), (290, 179), (290, 174), (291, 171), (294, 166), (295, 162), (296, 160), (298, 154), (298, 148), (299, 145), (300, 142), (304, 138), (309, 131), (310, 130), (314, 124), (315, 123), (316, 122), (320, 118), (321, 117), (325, 109), (326, 108), (330, 104), (331, 103), (334, 100), (337, 96), (338, 94), (338, 88), (338, 87), (338, 82), (337, 78), (336, 70), (336, 69), (338, 60), (339, 51), (340, 50), (344, 44), (346, 40), (349, 37), (350, 36), (356, 30), (362, 24), (368, 18), (367, 17), (366, 10), (360, 9), (356, 14))
i = 0
j = 0
while i < len(lista):
    if(i == (len(lista)) - 1):
        break
    else:
        initial_position = lista[i]
        final_position = lista[i+1]
        while(initial_position != final_position):
            initial_position = simulate_movement(initial_position, final_position)
            #print(initial_position,",",end="") # Posicicion actual
            j += 1
            print(j)
        i = i+1