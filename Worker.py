import time
import zmq

ctx = zmq.Context()

# recebe mensagem do ventilator
receiver = ctx.socket(zmq.PULL)
receiver.connect("tcp://localhost:5555")

# envia mensagem para o sink
sender = ctx.socket(zmq.PUSH)
sender.connect("tcp://localhost:5556")

while True:
    data = receiver.recv_json()
    value = data["value"]
    scalar = data["scalar"]
    row = data["row"]
    col = data["col"]

    result = value * scalar
    sender.send_json({"result": result, "row": row, "col": col})