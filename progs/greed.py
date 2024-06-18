"""
fix and array with 5 values
loop a counter to count how many times
does a value repeats itself in the array
set a variable to measure the score

"""
dices = [5, 1, 3, 4, 1]
counting = {}
#for i in range(1,7):
#    counting[i] = dices.count(i)
#    print(counting)
#score = 0

#d = {i:e for i,e in enumerate(l)}
counting = {i:dices.count(i) for i in range(1,7): }
