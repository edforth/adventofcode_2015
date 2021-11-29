with open('day01input.txt','r') as f:
    lines = f.read()

print(len(lines))

floor = 0 
enteredbasement = False 
for i in range(0,len(lines)):
    if lines[i] == "(":
        floor = floor+1
    elif lines[i] == ")":
        floor = floor-1
    else:
        print("oops, breaking")
        break 
    if floor == -1 and enteredbasement is False:
        enteredbasement = True
        part2answer = i + 1
part1answer = floor 

#print("# of (",lines.count('('))
#print("# of (",lines.count(')'))
print("Part 1 Answer =",part1answer)
print("Part 2 Answer =",part2answer)