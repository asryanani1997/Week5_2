x= [-1, -2, -3, -4, -5, -6]
y=0
z=0
for i in x: 
    if i%2==0:
        y+=i
    if i%2!=0:
        z+=i

print([y,z])