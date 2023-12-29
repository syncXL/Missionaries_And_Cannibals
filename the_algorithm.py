import numpy as np
from possible_actions import returnComb
from states_representation import State

def alreadyExplored(pathCH,node):
    cur_pos = node.position
    stateH = {"A" : []}
    for nodeCH in pathCH:
        if nodeCH.position == cur_pos:
            stateH["A"].append(nodeCH.banks["A"])
    dist = list(
        map(
            lambda node_hist : all(node.banks["A"] == node_hist),stateH["A"]
        )
    )
    if True in dist:
        return True
    return False
def policy(bank_A,bank_B):
    if (bank_A[0] < bank_A[1] and bank_A[0]!=0):
        return False
    elif (bank_B[0] < bank_B[1] and bank_B[0]!=0):
        return False
    elif np.min(bank_A) < 0 or np.min(bank_B) < 0:
        return False
    else:
        return True
def prPath(theP):
    for i,sol  in enumerate(theP) :
        print(f"Solution {i+1}")
        for j,node in enumerate(sol):
            print(f"{j}. \t Bank A:{node.banks["A"]} \t Bank B: {node.banks["B"]} \t action: {node.action}")

def explore(boatLim,n_miss,n_cann):
    actions = returnComb(boatLim,n_miss,n_cann)
    routes = [[State([[n_miss,n_cann],[0,0]],[0,0],True,"")]]
    paths = []
    while len(routes) != 0:
        chosenRoute = routes.pop(0)
        lastNode = chosenRoute[-1]
        focused_bank = lastNode.banks["A"] if lastNode.position else lastNode.banks["B"]
        other_bank = lastNode.banks["B"] if lastNode.position else lastNode.banks["A"]
        if not policy(lastNode.banks["A"],lastNode.banks["B"]):
            continue
        elif  alreadyExplored(chosenRoute[:-1],lastNode):
            continue
        elif np.sum(lastNode.banks["A"]) == 0 and np.sum(lastNode.banks["B"]) == (n_cann + n_miss):
            paths.append(chosenRoute)
            continue
        else:
            focused_bank = focused_bank - actions
            other_bank = other_bank + actions
            if lastNode.position:
                the_children = [([bank[0],bank[1]],actions[i],not lastNode.position) for i,bank in enumerate(zip(focused_bank,other_bank))]
            else:
                the_children = [([bank[1],bank[0]],actions[i],not lastNode.position) for i,bank in enumerate(zip(focused_bank,other_bank))]
            the_children = lastNode.make_children(the_children)
            for i in the_children:
                clone_chosen_Route = chosenRoute.copy()
                clone_chosen_Route.append(i)
                routes.append(clone_chosen_Route)
    return paths

pathS = explore(3,6,6)
prPath(pathS)