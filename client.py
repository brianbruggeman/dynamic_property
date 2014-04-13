import sys
import zmq

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 = sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

topicfilter = "10001"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

print "Collecting updates from weather server..."
socket.connect("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect("tcp://localhost:%s" % port1)

while True:
    string = socket.recv()
    topic, data = string.split()
    print topic, data