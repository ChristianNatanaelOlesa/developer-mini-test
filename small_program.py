def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def process_number(number):
    if is_prime(number):
        return None

    if number % 15 == 0:
        return "FooBar"

    if number % 3 == 0:
        return "Foo"

    if number % 5 == 0:
        return "Bar"

    return str(number)


def main():
    result = []

    for number in range(100, 0, -1):
        processed = process_number(number)

        if processed is not None:
            result.append(processed)

    print(" ".join(result))


if __name__ == "__main__":
    main()