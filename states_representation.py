class State:
    def __init__(self,banks,action,parent):
        self.banks = banks
        self.action = action
        self.parent = parent
    def make_children(self,attributes):
        self.the_children = [State(i) for i in attributes]
        return self.the_children
    def return_children(self):
        return self.the_children
