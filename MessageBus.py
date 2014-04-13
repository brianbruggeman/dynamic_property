#!/usr/bin/env python
"""
Standard Pub/Sub pattern

API mimics zmq for future integration with zmq
"""

import zmq
import time
import datetime

working_tcp_connect = "tcp://127.0.0.1:5555"
default_binding = "ipc://testing"
qualifier = "Testing"


def publish(data, topic=None, binding=None, sock=None):
    if topic is None:
        topic = qualifier
    if binding is None:
        binding = default_binding
    if sock is None:
        context = zmq.Context()
        sock = context.socket(zmq.PUB)
        sock.bind(binding)
        first_data = "Gobbly Gook"
        sock.send(first_data)
        time.sleep(0.15)  # magic number found through testing
    data_to_send = "%s %s" % (topic, data)
    sock.send(data_to_send)
    return sock


def subscribe(topic=None, binding=None, sock=None):
    if binding is None:
        binding = default_binding
    if topic is None:
        topic = qualifier
    if sock is None:
        context = zmq.Context()
        sock = context.socket(zmq.SUB)
        print 'Subscribing to "%s/%s"' % (binding, topic)
        sock.connect(binding)
        sock.setsockopt(zmq.SUBSCRIBE, topic)
    return sock


def wait(sock=None):
    print "Started: %s" % time.strftime('%l:%M%p %Z on %b %d, %Y')
    while True:
        sock = subscribe(sock=sock)
        data = sock.recv()
        topic, data = data.split()
        now = time.strftime('%l:%M%p %Z on %b %d, %Y')
        print 'Received: "%s" @ %s' % (data, now)
    return data

def data_generator():
    for x in xrange(0, 100):
        yield x