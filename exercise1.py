#exercise 1: 
def show_stars(rows):
    for i in range (rows):
        i=i+1
        for j in range (i):
            print("*"),
        print("\n")

print("When there are 5 rows:")
show_stars(5) #test with parameters 5
print("When there are 8 rows:")
show_stars(8) #test with parameters 8