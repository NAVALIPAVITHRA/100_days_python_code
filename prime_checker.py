def prime_checker(num):
    is_prime=True
    for i in range(2,num):
      if num%i==0:
         is_prime=False
    if is_prime:
       print("prime")
    else:
       print("not")
num=int(input())
prime_checker(num)