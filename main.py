cal=  lambda x1,y1,x2,y2: int((abs(x1-x2)+abs(y1-y2)+abs(x1+y1-x2-y2))/2)


def cal_list (a,b):
  k=[]
  for i in a:
    k.append(i)
  for i in b:
    k.append(i)
  return cal(k[0],k[1],k[2],k[3])
