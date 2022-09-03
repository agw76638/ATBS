tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
tableLen = len(tableData)

def printTable():
    colWidths = [0] * tableLen
    for x in range(tableLen):
        for y in range(len(tableData[x])):
            if len(tableData[x][y]) > colWidths[x]:
                colWidths[x] = len(tableData[x][y])
    
    for m in range(len(tableData[0])):
        for n in range(tableLen):
            print((tableData[n][m]).rjust(colWidths[n]), end=" ")
        print()

printTable()