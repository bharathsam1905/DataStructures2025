class Fibonacci:
    def fib(self,n:int)->int:
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)

f1=Fibonacci()
print(f1.fib(10))

    