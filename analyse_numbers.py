def is_number_natural(number):
    if number % 1 == 0 and number > 0:
        return True
    else:
        return False


def main():
    my_numbers = [12, 13, 14, 15, 16, 17, 134134, 311]
    for i in my_numbers:
        print(my_numbers[i - 1], "is number natural", is_number_natural(my_numbers[i - 1]))


if __name__ == '__main__':
    main()
