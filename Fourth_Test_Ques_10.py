# 1	 0	1	0	1	0	1	0	1	0
# 1	 0	1	0	1	0	1	0	1	0
# 1	 0	1	0	1	0	1	0	1	0
# 1	 0	1	0	1	0	1	0	1	0
# 1	 0	1	0	1	0	1	0	1	0
# 1	 0	1	0	1	0	1	0	1	0
# 1	 0	1	0	1	0	1	0	1	0
# 1	 0	1	0	1	0	1	0	1	0
# 1	 0	1	0	1	0	1	0	1	0
# 1	 0	1	0	1	0	1	0	1	0



for row in range(10):
    num=1
    for col in range(10):
        if num>1:
           num=0
        if row<=10:
          print(num,end=" ")
          num=num+1
    print()
