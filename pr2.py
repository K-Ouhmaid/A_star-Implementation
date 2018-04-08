
# coding: utf-8

# In[50]:


#A* Implementation
#Implemented by Khalid Ouhmaid

from copy import deepcopy
#each state of puzzle has parent
#h and g
#f= g+h
class puzzle:
    def __init__ (self, starting, parent):
        self.board = starting
        self.parent = parent
        self.f = 0
        self.g = 0
        self.h = 0
#manhattan takes in paramere a state of puzzle
#and calculate the huristics 
    def manhattan(self):
        inc = 0
        h = 0
        for i in range(3):
            for j in range(3):
                h += abs(inc-self.board[i][j])
            inc += 1
        return h
#a state of puzzle is a goal where all the indexes are equal to the value of their indexes
#if one index is n 't equal to the value of index its enough to know that we re n't rich the goal

    def goal(self):
        inc = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != inc:
                    return False
                inc += 1
        return True

    def __eq__(self, other):
        return self.board == other.board
#takes in parametre a state of puzzle to do transfer of indexes
#its return a list of the possible transfers 
def Moving(curr):
    curr = curr.board
    for i in range(3):
        for j in range(3):
            if curr[i][j] == 0:
                x, y = i, j
                break
    q = []
    if x-1 >= 0:
        b = deepcopy(curr)
        b[x][y]=b[x-1][y]
        b[x-1][y]=0
        succ = puzzle(b, curr)
        q.append(succ)
    if x+1 < 3:
        b = deepcopy(curr)
        b[x][y]=b[x+1][y]
        b[x+1][y]=0
        succ = puzzle(b, curr)
        q.append(succ)
    if y-1 >= 0:
        b = deepcopy(curr)
        b[x][y]=b[x][y-1]
        b[x][y-1]=0
        succ = puzzle(b, curr)
        q.append(succ)
    if y+1 < 3:
        b = deepcopy(curr)
        b[x][y]=b[x][y+1]
        b[x][y+1]=0
        succ = puzzle(b, curr)
        q.append(succ)

    return q
#searching the state of puzzle that has the minimum f 
#and return it and his index
def b_Fvalue(List1):
    f = List1[0].f
    index = 0
    for i, item in enumerate(List1):
        if i == 0: 
            continue
        if(item.f < f):
            f = item.f
            index  = i

    return List1[index], index
#AStar
#we defind two lists 
#List1 its open contains the possible transfer states
#closedList contain only the best transfer state that its done to avoid repition
def AStar(start):
    List1 = []
    closedList = []
    List1.append(start)
#we take the state of the puzzle has the best value of f in open List
#delete the state of puzzle token in open List and add it to the closed ListList1.pop(index)
    while List1:
        current, index = b_Fvalue(List1)
        if current.goal():
            return current
        List1.pop(index)
        closedList.append(current)
#do the transfers possible of the state added to the closed List
#its returnning a list of possible transfres
        M = Moving(current)
        for move in M:
            ok = False  
#checking in closedList
            for i, item in enumerate(closedList):
                if item == move:
                    ok = True
                    break
#not in closed list
                if not ok:              
                  newG = current.g + 1 
                  present = False

#openList includes move
                for j, item in enumerate(List1):
                    if item == move:
                        present = True
#compare two state that re the same
#we do an update if the nez state has the minimum g

                        if newG < List1[j].g:
                            List1[j].g = newG
                            List1[j].f = List1[j].g + List1[j].h
                            List1[j].parent = current
#if the state is n't in the open List
#we calculate his g and h 
#and add it to the open List with his parent   
            if not present:
                    move.g = newG
                    move.h = move.manhattan()
                    move.f = move.g + move.h
                    move.parent = current
                    List1.append(move)

    return None


InitialState = puzzle([[1,2,0],[3,4,5],[6,7,8]], None)

result = AStar(InitialState)
NOfMoves = 0

if(not result):
    print ("Sorry No Solution")
else:
    print(result.board)
    R=result.parent
    while R:
        NOfMoves += 1
        print(R.board)
        R=R.parent
print ("Number of Moves: " + str(NOfMoves))

