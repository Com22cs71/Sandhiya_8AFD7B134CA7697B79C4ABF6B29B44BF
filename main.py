def fact_rec(n):
  if n==1 or n==0:
    return 1
  else:
    return 0
number=int(input("Enter the value"))
res=fact_rec(number)
print("The factorial of",number,"is",res)