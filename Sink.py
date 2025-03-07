import sys
import time
import zmq

ctx = zmq.Context()

# abre para conexão com worker e ventilator
receiver = ctx.socket(zmq.PULL)
receiver.bind("tcp://*:5556")

s = receiver.recv() # espera por mensagem do ventilator
t_start = time.time() # inicia contagem do tempo
tasks = 100

for task_nbr in range(tasks):
    s = receiver.recv_string()
    print(".", end="")

t_end = time.time()
print(f"\nTempo total: {(t_end-t_start):.5f}s")
