# Single responsibility principle

# BAD solution
def math_operations(list_):
    print(f"Mean is {sum(list_) / len(list_)}")
    print(f"Max value is {max(list_)}")


math_operations(list_=[1, 2, 3, 4, 5])


# GOOD solution (with Single responsibility principle)
def get_mean(list_):
    if len(list_):
        return sum(list_) / len(list_)
    return None


def get_max(list_):
    if len(list_):         # není nutné testovat if len(list_) > 0:
        return max(list_)
    return None            # není potřeba mít else:


def print_mean_and_max(list_):
    print(f"Mean is {get_mean(list_)}")
    print(f"Max is {get_max(list_)}")


def main():
    my_list = []  # [1, 2, 3, 4, 5, 6]
    print_mean_and_max(my_list)
    print(f"Mean is: {get_mean(my_list)}")


if __name__ == '__main__':
    main()