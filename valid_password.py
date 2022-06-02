def is_valid_password(password):
    password_items = [int(i) for i in password.split(':')]
    if len(password_items) > 3:
        return False
    if is_palindrome(password_items[0]) and is_prime(password_items[1]) and is_even(password_items[2]):
        return True
    else:
        return False


def is_prime(num):
    if num == 1:
        return False
    return len([i for i in range(1, num+1) if num % i == 0]) == 2


def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]


def is_even(num):
    return num % 2 == 0


psw = input()


print(is_valid_password(psw))
