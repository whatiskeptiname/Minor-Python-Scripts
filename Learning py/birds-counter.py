birds = [0,0,0,0,0,0,0,0,0]
bird = 0
while 1:
    bird = int(input("Enter the bird name"))
    if bird == 9:
        break
    birds[bird] = birds[bird] + 1
    
        
for i in range(0,9) :
    print(f"The no {i} bird came for {birds[i]} times")