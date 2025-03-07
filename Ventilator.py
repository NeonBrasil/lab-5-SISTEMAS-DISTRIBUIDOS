import zmq
import time

ctx = zmq.Context()

# envio de mensagens para os workers
sender = ctx.socket(zmq.PUSH)
sender.bind("tcp://*:5555")

# sincronização com o sink
sink = ctx.socket(zmq.PUSH)
sink.connect("tcp://localhost:5556")

# Receber as dimensões da matriz
rows = int(input("Digite o número de linhas da matriz: "))
cols = int(input("Digite o número de colunas da matriz: "))

# Receber os valores da matriz
matrix = []
print("Digite os valores da matriz:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Receber o escalar
scalar = int(input("Digite o valor do escalar: "))

# Exibir a matriz e pedir confirmação
print("Matriz:")
for row in matrix:
    print(" ".join(map(str, row)))

confirm = input("A matriz está correta? (s/n): ")
if confirm.lower() != 's':
    print("Operação cancelada.")
    exit()

sink.send(b'0') # avisa o sink que os dados serão enviados

# Enviar os valores da matriz e o escalar para os workers
for i in range(rows):
    for j in range(cols):
        sender.send_json({"value": matrix[i][j], "scalar": scalar, "row": i, "col": j})

time.sleep(1)