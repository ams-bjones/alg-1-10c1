import math

def semi (triangle):
    answer = 0
    #sets up a variable called answer, and stores a number 90) in it
    for side in triangle:
        #loops throuygh the sides in the triangle list send to teh function
        answer = answer + side
        #adds the sides to the answer
    answer = answer /2
    #half the answer, and store it back in the variable
    return (answer)
    #send the contents of the answer variable back to the caller
    
def aword(semi, triangle):
    #sets up function called 'aword' and inputs two variables, a number called semi, and a list called triangle'
    answer = 1
    #sets up a variable called answer and stores 1 in it.
    arglist =[semi]
    #sets up a list to loop through, and puts the number in semi as the first item
    for side in triangle:
        arglist.append(semi-side)
        #add (semi-side) for each side into the arglist
    for thing in arglist:
        answer = answer * thing
        #multiply all the things together in arglist
    answer = math.sqrt(answer)
    #find the square root of the things multiplied together
    return (answer)
    #give the number back to the caller

def area(triangle):
    s = semi(triangle)
    #finds the semiperimeter
    answer = aword(s,triangle)
    # uses the semiperimeter to find the area of the triangle
    return (answer)