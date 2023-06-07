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

def simulate_movement(matrix, initial_position, final_position):
    
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

    print(current_position[0], current_position[1])
    print_matrix(matrix)
    
    return matrix, [current_position[0], current_position[1]]
        

# Ejemplo de uso
rows = 5
cols = 5
matrix = create_matrix(rows, cols)

initial_position = [1, 1]
final_position = [3, 4]

lista = [[1,1], [1,3], [3,3], [1,2]]
i = 0
while i < len(lista):
    if(i == (len(lista)) - 1):
        break
    else:
        initial_position = lista[i]
        final_position = lista[i+1]
        while(initial_position != final_position):
            matrix, initial_position = simulate_movement(matrix, initial_position, final_position)
            print(initial_position) # Posicicion actual
        i = i+1