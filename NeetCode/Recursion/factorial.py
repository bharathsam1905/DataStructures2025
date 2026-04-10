class Recursion:
    def factorial(self,n:int)->int:
          if n<=1:
               return 1
          else:
               return n*self.factorial(n-1)


f1=Recursion()
print(f1.factorial(5))
