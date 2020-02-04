def dfs(listmain,i,j, visited, dict):
    stack = []
    stack.append([i,j])
    visited[i][j] = 1
    listmain[i][j] = 0
    while(len(stack) != 0):
        first = stack[0]
        stack.pop(0)
        s = str(first[0]) + "," + str(first[1])
        l = dict[s]
        for k in range (0,len(l)):
            neighbor = l[k]
            if neighbor[0] > -1 and neighbor[0]<row and neighbor[1]> -1 and neighbor[1] < col:
                if (listmain[neighbor[0]][neighbor[1]] == 1) and (visited[neighbor[0]][neighbor[1]] != 1):
                    stack.insert(0, [neighbor[0],neighbor[1]])
                    visited[neighbor[0]][neighbor[1]] = 1
                    listmain[neighbor[0]][neighbor[1]] = 0
    return listmain, visited

row = int(input())
col = int(input())
listmain = []
for i in range(0, row):
    l = input().split(" ")
    l = list(map(int,l))
    listmain.append(l)
clusters = 0
dict = {}
visited = []
v = []
for j in range(0,col):
    v.append(0)
for i in range(0,row):
    visited.append(v.copy())
for i in range(0,row):
    for j in range(0, col):
        s= str(i)+","+str(j)
        dict[s] = [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]
for i in range(0,row):
    for j in range(0, col):
        if listmain[i][j] == 1:
            l, v = dfs(listmain, i,j, visited, dict)
            listmain = l.copy()
            visited = v.copy()

            clusters = clusters + 1

print(clusters)





