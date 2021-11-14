import random

#when user can only play 100 times
total_score = 0
possibility = 0
print("================= 100 TIMES =================")
for j in range(100):    
    dice = random.randint(1,6)
    if(total_score > 59):
        possibility = j
        break
    if(((dice == 1) or (dice == 2)) and ((total_score == 0))):
        continue
    elif(((dice == 1) or (dice == 2)) and ((total_score > 0))):
        total_score = total_score - 1
    elif((dice < 6) and (dice > 2)):
        total_score = total_score + 1
    elif(dice == 6):
        total_score = total_score + dice
    print(total_score)
    print("the times user has rolled the dice " + str(j))


win_possibility = possibility / float(100)
print(win_possibility)
#there 0.1% of going down one floor => -0.1% in total winning percentage 
win_possibility = win_possibility - 0.1 
print("the possibility of winning is: " + str(win_possibility))
        



print("================= UNLIMITED TIMES =================")
#when user can play unlimited times 
possibility = 0
total_score = 0
flag = True
while(flag):    
    possibility = possibility + 1
    dice = random.randint(1,6)
    if(total_score > 59):
        flag = False
        break
    if(((dice == 1) or (dice == 2)) and ((total_score == 0))):
        continue
    elif(((dice == 1) or (dice == 2)) and ((total_score > 0))):
        total_score = total_score - 1
        flag = True
    elif((dice < 6) and (dice > 2)):
        total_score = total_score + 1
        flag = True
    elif(dice == 6):
        total_score = total_score + dice
        flag = True


win_possibility = possibility / float(100)
print(win_possibility)
#there 0.1% of going down one floor => -0.1% in total winning percentage 
win_possibility = win_possibility - 0.1
print("the possibility of is: " + str(win_possibility))