def returnComb(cap,*pop_entity):
    max_len = len(pop_entity)
    theEdges = [list(range(0,pop_entity[i]+1)) for i in range(max_len)]
    routes = [[i] for i in theEdges[0]]
    paths = []
    while len(routes) != 0:
        chosenRoute = routes.pop(0)
        chosenEdge = len(chosenRoute)
        if chosenEdge == max_len:
            if sum(chosenRoute) in range(1,cap+1):
                paths.append(chosenRoute)
        else:
            for edge in theEdges[chosenEdge]:
                newRoute = chosenRoute.copy()
                newRoute.append(edge)
                routes.append(newRoute)
    return paths

pathS = returnComb(4,5,5,5,5)
for i,action in enumerate(pathS):
    print(f"{i}: {action}")

