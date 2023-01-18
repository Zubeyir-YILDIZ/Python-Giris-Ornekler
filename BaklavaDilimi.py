genişlik=int(input("genişlik değeri girin : "))
yükseklik=int(input("yükseklik değeri girin : "))

for x in range(yükseklik):
    
    for y in range(genişlik-x-1):
        print(" ",end='')
    
    for z in range(x+1):
        print("*",end=' ')   
    print(" ")
for k in range(yükseklik):
    

    for m in range(k+1):
        print(" ",end='')
    
    
    for l in range(genişlik-k-1):
        print("*",end=' ')
    print(" ")
    
    


        
