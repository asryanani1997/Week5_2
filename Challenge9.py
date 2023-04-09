x="900876"
if len(x) in [4,6]:
    if x.isdigit():
        if not any(i.isspace() for i in x):
            print (True) 
        else: print(False)
    else: print(False)
else: print(False)
