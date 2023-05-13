total = open("Life_Period_02.txt","r")
totalfigure = total.read().split("\n")
loop = totalfigure[0];
period = totalfigure[1]
for y in range(1,int(loop)):
    for i in range(2,len(totalfigure)) :
        print(totalfigure[i])
        for x in range(len(totalfigure[i])):
            live = 0
            if x<len(totalfigure[i])-1:
                if totalfigure[i][x+1]=="x":
                    live+=1
            if x>=1:
                if totalfigure[i][x-1]=="x":
                    live+=1
            if i>=3:
                afterfigure = totalfigure[i-1]
                if afterfigure[x]=="x":
                    live+=1
            if i<len(totalfigure[i]):
                prevfigure = totalfigure[i+1]
                if prevfigure[x]=="x":
                    live+=1
            if totalfigure[i][x]==" " and live==3:
                totalfigure[i] = totalfigure[i][:x]+"x"+totalfigure[i][x+1:]
            if totalfigure[i][x]=="x" and (live==0 or live==1 or live==4):
                totalfigure[i] = totalfigure[i][:x]+" "+totalfigure[i][x+1:]
            
            
        
        
            
            
                
                
        
        
