from itertools import batched

def exploreObject(t: type, sorted = True, cols = 2, pad = 30, dunder = False):
    print(f"Functions inside {type(t)} : \n\n")
    functionNames = []
    if dunder:
        functionNames = [name for name in dir(t) if name[0] == "_"]
    else:
        functionNames = [name for name in dir(t) if name[0] != "_"]

    if sorted:
        functionNames.sort(key= lambda x : len(x))
    functionNames = [list(batch) for batch in batched(functionNames, cols)]

    for i in functionNames:
        output = ""
        for j in i:
            output += f"{j:<{pad}}"
        print(output)
    print("\n")