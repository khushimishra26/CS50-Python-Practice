#to work on lists, calculating averages and so forth. Fstring can be used as well.
scores=[]
for i in range(3):
    scores.append(int(input("Enter score: ")))              #taking input from user and appending values in the list [append() does not require defining the array during declaration time, it'll keep on adding the values in the list each time it is invoked]
average=str(sum(scores)/len(scores))
print(f"Average of all scores is: {average}")