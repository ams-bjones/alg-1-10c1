#question 2 in code
def min (numList):
    ''' Finds the minimun from a list of numbers '''
    answer = None
    for num in numList:
        if answer == None:
            answer = num
        if num < answer:
            answer = num
    return answer

def max (numList):
    ''' finds the maximum from a list of numbers'''
    answer = None
    for num in numList:
        if answer == None:
            answer = num
        if num > answer:
            answer = num
    return answer