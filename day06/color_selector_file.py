with open('colors.txt') as fh:
  colors = []
  for line in fh:
    colors.append(line.rstrip("\n"))
    
for i in range(len(colors)):
  print("{}. {}".format(i, colors[i]))
  
selected = int(input("Select color: "))
print("The selected color is: ", colors[selected])
