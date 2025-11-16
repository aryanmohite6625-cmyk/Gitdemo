def get_prime(num):
    primes = []
    for num in range(2,num+1):
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
                primes.append(num)
    return primes

last_num= int(input("Enter the last number: "))
print(get_prime(last_num))

