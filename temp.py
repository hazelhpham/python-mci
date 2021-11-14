# -*- coding: utf-8 -*-
"""
Name: Huong Pham 
Start date: 2/11/2021
Finish date: 

Use Pandas to analyze the data of names 



use counter to count occurences so it does not harm your performance speed

"""


import pandas as pd
#import matplotlib.pyplot as plt
import glob
from collections import Counter
#import numpy as np
#import seaborn as sns

#1: Dùng Pandas đọc và tổng hợp dữ liệu của các năm
folder_path = '/Users/hazel/Desktop/03 Python exercies_2021/Names'
file_list = glob.glob(folder_path + "/*.txt")
length_of_files = len(file_list) #139
main_dataframe = pd.DataFrame(pd.read_csv(file_list[0]))
main_dataframe.columns = ['Name','Gender','SSN']
main_dataframe['Year'] = 1880

j = 1881
for i in range(1,len(file_list)):
    data = pd.read_csv(file_list[i])
    data.columns = ['Name','Gender','SSN']
    data['Year'] = j  
    j=j+1
    df = pd.DataFrame(data)
    main_dataframe = pd.concat([main_dataframe,df],axis=0)

print(main_dataframe)


#2: Vẽ biểu đồ tổng số trẻ em sinh ra theo giới tính và năm (Total births by sex and year)
#bar chart??? 
#print(new_dataframe)
#Female, year, totalF
#Male, year, totalM


#testing function count() for year 1880
#totalF_1880 = main_dataframe[(main_dataframe['Year'] == 1880) & (main_dataframe['Gender']=='F')].count()
#totalM_1880 = main_dataframe[(main_dataframe['Year'] == 1880) & (main_dataframe['Gender']=='M')].count()
#print("Count of Male in year 1880",totalM_1880[0])
#print("Count of Female in year 1880",totalF_1880[0])

#=========================================================================================================

"""
listTotalF = []
listTotalM = []
index = []
j = 1880
for i in range(0,10):
    totalF = 0
    totalM = 0
    index.append(j)
    totalF = main_dataframe[(main_dataframe['Year'] == j) & (main_dataframe['Gender']=='F')].count()
    totalM = main_dataframe[(main_dataframe['Year'] == j) & (main_dataframe['Gender']=='M')].count()
    j=j+1
    listTotalF.append(totalF[0])
    listTotalM.append(totalM[0])

   
df = pd.DataFrame({'Female': listTotalF,
                    'Male': listTotalM}, index=index)
ax = df.plot.bar(rot=0, color={"Female": "pink", "Male": "blue"})
"""

#3 Tạo subset gồm top 1000 cái tên phổ biến mỗi năm theo từng loại giới tính
# unique names -> gender F ->  count in 1880, 1881, 1882, etc 
# unique names -> gender M ->  count in 1880, 1881, 1882, etc 

#get a list of unique names
#unique_names = set(main_dataframe['Name'])
#print(len(unique_names)) #98400
#print(len(main_dataframe['Name'])) #1956907

j = 1880
listNames = []
print(Counter(main_dataframe))

for i in range (0, 300):
    name = list(unique_names)[i]
    print(name)
    countName = main_dataframe[(main_dataframe['Year'] == j) & (main_dataframe['Gender'] == 'Female') & (main_dataframe['Name'] == name)].count()
    person = [name, countName[0]]
    listNames.append(person)
    j = j + 1 

#print(listNames)
#count names based on years and genders. 
#unique names - 1880 - Female 
#unique names - 1880 - Male 

#4 Vẽ biểu đồ số lượng các bé sinh theo năm có các tên sau: Philip, Harry, Elizabeth, Marilyn 


#5Vẽ biểu đồ thể hiện sự đa dạng trong việc đặt tên qua các năm theo từng giới tính (thể hiện bằng xu hướng giảm dần từng năm của tổng tỷ lệ % của top 1000 tên phổ biến)
#6 Vẽ biểu đồ thể hiện sự thay đổi trong cách đặt chữ cái đầu tiên trong tên của nam và nữ qua các năm 1900, 1960 và 2018
#7 Xác định xu hướng tên con trai biến thành tên con gái và ngược lại. Lấy ví dụ tên có chữ “Lesl...” Ban đầu nam đặt nhiều sau đó giảm, nữ ngược lại.