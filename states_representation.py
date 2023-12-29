import numpy as np
class State:
    def __init__(self,banks,action,position,parent):
        self.banks = {"A":np.array(banks[0]),"B": np.array(banks[1])}
        self.action = np.array(action)
        self.position = position
        self.parent = parent

    def make_children(self,attributes):
        self.the_children = [State(i[0],i[1],i[2],self) for i in attributes]
        return self.the_children
    # def return_children(self):
    #     return self.the_children\