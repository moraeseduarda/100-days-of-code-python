def prime_checker(number):
    num_divisors = 0
    for i in range(1, 101):
        check = n % i
        if check == 0:
            num_divisors += 1
    if num_divisors == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input())
prime_checker(number=n)