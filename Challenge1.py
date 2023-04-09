x, y, z= [1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]
common= set(x).intersection(set(y))
common= set(common).intersection(set(z))
sum=0
for i in common: 
    sum+= i*min([x.count(i), y.count(i), z.count(i)])
print(sum)