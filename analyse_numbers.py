def is_number_natural(number):
    if number % 1 == 0 and number > 0:
        return True
    else
        return False

def main():
    my_number = 12
    print(my_number, "is number natural", is_number_natural(my_number))
if __name__ == '__main__':
    main()
