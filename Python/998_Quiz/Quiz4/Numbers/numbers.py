mynumbers = [6,9,32,28,15,22,3,18]

minimum = mynumbers[1]   
maximum = mynumbers[1] 

for z in mynumbers: 
    if z < minimum: 
        minimum = z 
 
for z in mynumbers:
    if z > maximum: 
        maximum = z

avg=1
for z in range(0, len(mynumbers)):
    avg=avg+mynumbers[z]
avg=avg/len(mynumbers)
   


print("maximum is =", maximum, "minimum is =", minimum, "Average=", avg) 