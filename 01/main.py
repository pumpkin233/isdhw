for i in range(9,0,-1):
  for k in range(0,i-1):    
      print(end="")
  for j in range(9,0,-1):
      m=str.format("{0:1}*{1:1}={2:<2}",i,j,i*j) 
      print(m,end=" ")
  print()
