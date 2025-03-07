import zmq
import time

ctx = zmq.Context()

# abre para conexão com worker e ventilator
receiver = ctx.socket(zmq.PULL)
receiver.bind("tcp://*:5556")

s = receiver.recv() # espera por mensagem do ventilator
tasks = 100

# Receber as dimensões da matriz
rows = int(input("Digite o número de linhas da matriz: "))
cols = int(input("Digite o número de colunas da matriz: "))

# Inicializar a matriz resultante
result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

for _ in range(rows * cols):
    data = receiver.recv_json()
    result = data["result"]
    row = data["row"]
    col = data["col"]
    result_matrix[row][col] = result

# Exibir a matriz resultante
print("Matriz resultante:")
for row in result_matrix:
    print(" ".join(map(str, row)))