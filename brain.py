import node
import connection
import random


class Brain:
    def __init__(self, inputs):
        self.connections = []
        self.nodes = []
        self.inputs = inputs
        self.net = []
        self.layers = 2
