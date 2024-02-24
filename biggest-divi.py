def find_max_divisors(numbers):
    max_divisors = 0
    number_with_max_divisors = None

    for number in numbers:
        divisor_count = count_divisors(number)
        if divisor_count > max_divisors:
            max_divisors = divisor_count
            number_with_max_divisors = number
        elif divisor_count == max_divisors:
            number_with_max_divisors = max(number_with_max_divisors, number)

    return number_with_max_divisors, max_divisors

def count_divisors(number):
    divisor_count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            divisor_count += 1
    return divisor_count

def main():
    numbers = []
    for i in range(20):
        number = int(input(""))
        numbers.append(number)

    max_divisor_number, max_divisor_count = find_max_divisors(numbers)
    print(max_divisor_number,max_divisor_count)
    print()
if __name__ == "__main__":
    main()
