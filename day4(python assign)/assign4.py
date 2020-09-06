#Assignment4

#1.Armstrong numbers

n=1042000
while(n<=702648265):
  m=n
  sum=0
  while(m>0):
    digit=m%10
    sum=sum+(digit**len(str(m)))
    m=m//10
    if(n==num):
      print("the first armstrong number",n)
      break
      n=n+1

#output

the first armstrong number1741725


