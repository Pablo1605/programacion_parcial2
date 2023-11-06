'''Parcial 2'''

def validate_sequence(dna): #Función para verificar que los datos ingresados sean validos
    valid_chars = {'A', 'T', 'C', 'G'}
    return len(dna) == 6 and set(dna).issubset(valid_chars)

def is_mutant(dna): #Función is_mutant 
    rows = len(dna)
    cols = len(dna[0])
    sequences_count = 0

    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if 0 <= i + 3*dx < rows and 0 <= j + 3*dy < cols:
                    if dna[i][j] == dna[i + dx][j + dy] == dna[i + 2*dx][j + 2*dy] == dna[i + 3*dx][j + 3*dy]:
                        sequences_count += 1
                        if sequences_count > 1:
                            return True

    return False


#Entrada de datos para ADN
dna = []
for i in range(6):
    valid_row = False
    while not valid_row:
        row = input(f"Ingrese la fila {i+1} de ADN (debe contener 6 letras A, T, C o G, y no debe contener espacios): ").upper()
        valid_row = validate_sequence(row)
        if not valid_row:
            print("La fila ingresada no es válida. Por favor, inténtelo nuevamente.")

    dna.append(row)

#Verificacion booleana para guardar dentro de la variable mutant si el ADN es de mutante o no (verdadero en caso de ser mutante y falso si no lo es) 
mutant = is_mutant(dna)

#Aca se imprime en pantalla si el ADN es de mutante o no
if mutant:
    print("El humano es mutante.")
else:
    print("El humano no es mutante.")