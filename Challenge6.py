x=516
y=str(x)
sum_digits=0 
for i in y:
    sum_digits+= int(i)

print(x%sum_digits==0)