#box
x = 18
y = 24
z = 44

#obj
p = 5
q = 5
r = 13
ans = 0

def boxes (dimx,dimy,dimz,a,b,c):

    maxval=0
    maxval_combination = [0,0,0]

    #Finding the combination that gives maximum value by p
    if int(dimx/a) * int(dimy/b) * int(dimz/c) > maxval:
        maxval =  int(dimx/a) * int(dimy/b) * int(dimz/c)
        maxval_combination = [a,b,c]
    
    if int(dimx/a) * int(dimy/c) * int(dimz/b) > maxval:
        maxval = int(dimx/a) * int(dimy/c) * int(dimz/b)
        maxval_combination = [a,c,b]
    
    if int(dimx/b) * int(dimy/a) * int(dimz/c) > maxval:
        maxval = int(dimx/b) * int(dimy/a) * int(dimz/c)
        maxval_combination = [b,a,c]

    if int(dimx/b) * int(dimy/c) * int(dimz/a) > maxval:
        maxval = int(dimx/b) * int(dimy/c) * int(dimz/a)
        maxval_combination = [b,c,a]

    if int(dimx/c) * int(dimy/b) * int(dimz/a) > maxval:
        maxval = int(dimx/c) * int(dimy/b) * int(dimz/a)
        maxval_combination = [c,b,a]

    if int(dimx/c) * int(dimy/a) * int(dimz/b) > maxval:
        maxval = int(dimx/c) * int(dimy/a) * int(dimz/b)
        maxval_combination = [c,a,b]

    #Add the calculated boxes value to final answer
    global ans
    ans += maxval

    #if that value is zero then return because no more boxes can fit inside 
    if(maxval == 0):
        return

    #Finding space remaining in respective dimensions
    free_space = [dimx % maxval_combination[0] , dimy % maxval_combination[1], dimz % maxval_combination[2]]

    #Finding the appropriate remaining 3D space in the box
    #(the one with max value in 'free_space' array will determine how much sapce remains empty *By Observation*)

    #Finding the dimension that leaves maximum free space
    max_free_space = max(free_space)


    #Passing the remaining space for that dim and initial values(the ones passed in the function by last recursive call) for other two
    if(free_space[0] == max_free_space):
        boxes(free_space[0],dimy,dimz,a,b,c)
        
    elif(free_space[1] == max_free_space):
        boxes(dimx,free_space[1],dimz,a,b,c)
        
    elif(free_space[2] == max_free_space):
        boxes(dimx,dimy,free_space[2],a,b,c)


boxes(x,y,z,p,q,r)
print(ans)



"""
#pseudo Code

answer = 0
function boxes(dimensions)

    val <- call (bestorientation)
    add val to answer

    when val = 0
        return
    
    spaceleft <- call(freespace)

    call(boxes)

call(boxes)
print(answer)

"""