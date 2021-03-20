class cal:#modules
    add =lambda a,b:a+b

    def fact(n):
        if n <=1:
            return 1
        else:
            return n*cal.fact(n-1)

    def prime(n):
        for i in range(2,n):
            if n%i==0:
                print("its not prime")
                break
        else:
            print("its prime number")
    
class cal1:
    mul=lambda a,b:a*b
