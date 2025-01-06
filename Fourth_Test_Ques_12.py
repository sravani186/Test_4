# 1	 2	3	4	5
# 5	 4	3	2	1	
# 1	 2	3	4	5
# 5	 4	3	2	1
# 1	 2	3	4	5

num=0
for row in range(5):
    for col in range(5):
        if row%2==0:
           num=num+1
           print(num,end=" ")
        else:
          print(num,end=" ")
          num=num-1
    print()