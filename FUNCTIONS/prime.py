def prime(a):
    for i in range (2,a) :
        if a % i == 0 :
            return "It is not a prime number"
    return "It is a Prime number"

a = int(input("Enter a number : "))
print(prime(a))
