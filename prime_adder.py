# Sum of 2 prime numbers
import random

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_primes(start, end):
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes

def choose_and_sum_primes(prime_list):
    if len(prime_list) < 2:
        return None, None, "Not enough prime numbers in the list to choose from."
    
    chosen_primes = random.sample(prime_list, 2)
    prime1 = chosen_primes[0]
    prime2 = chosen_primes[1]
    total_sum = prime1 + prime2
    return prime1, prime2, total_sum

if __name__ == "__main__":
    start_range = 1
    end_range = 1000

    print(f"Generating prime numbers between {start_range} and {end_range}...")
    primes = generate_primes(start_range, end_range)

    if len(primes) < 2:
        print(f"Error: Not enough prime numbers found between {start_range} and {end_range} to choose two distinct primes.")
    else:
        prime1, prime2, total_sum = choose_and_sum_primes(primes)
        print(f"Chosen prime numbers: {prime1} and {prime2}")
        print(f"Sum: {total_sum}")