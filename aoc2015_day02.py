with open('day02input.txt','r') as f:
    lines = f.read().splitlines()


print(lines)

wrappingpaperneeded = 0 
ribbonneeded = 0 
for line in lines:
    s = line.split('x')
    l = int(s[0])
    w = int(s[1])
    h = int(s[2])
    lw = l*w 
    wh = w*h 
    hl = h*l 
    perimeter1 = (l+w)*2
    perimeter2 = (w+h)*2
    perimeter3 = (h+l)*2
    shortestperimeter = min(perimeter1,perimeter2,perimeter3)
    shortestsidearea = min(lw,wh,hl)
    wrappingpaperneeded = wrappingpaperneeded + (lw*2)+(wh*2)+(hl*2)+shortestsidearea
    ribbonneeded = ribbonneeded + shortestperimeter + (l*w*h)

print("Part 1 answer = ",wrappingpaperneeded)
#Correct first try (1606483)

#Part 2
print("Part 1 answer = ",ribbonneeded)
#Correct first try (3842356)
