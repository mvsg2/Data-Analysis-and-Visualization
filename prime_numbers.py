# I want to add some code here that has a bunch of instructions to pin-point what the primes are...
def get_primes():
  lower_limit = int(input("Enter lower range: "))  
  upper_limit = int(input("Enter upper range: "))  
  
  for num in range(lower_limit,upper_limit + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  
