"""1masala"""


def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


my_counter = counter()
# print(my_counter())
# print(my_counter())
# print(my_counter())


"""2masala"""


def counter():
    count = 1

    def increment(factor):
        nonlocal count
        count *= factor
        return count

    return increment


my_counter = counter()

# print(my_counter(2))
# print(my_counter(3))


"""3masala"""


def counter():
    count = 0

    def increment(factor):
        nonlocal count
        count += factor
        return count

    return increment


my_counter = counter()

# print(my_counter(2))
# print(my_counter(3))
# print(my_counter(8))

"""4masala"""


def qoshish(num):

    def qosh(val):
        return num + val

    return qosh


def ayirish(num):

    def ayir(val):
        return num - val

    return ayir


clouser1 = qoshish(10)
clouser2 = ayirish(5)

# print(clouser1(2))
# print(clouser2(3))

"""5masala"""


def function(foiz):
    def new(narx):
        count = narx * (foiz / 100)
        return narx - count

    return new


num1 = function(10)
num2 = function(20)

narx = 500

# print(num1(narx))
# print(num2(narx))


"""6masala"""


def login():
    login_count = 0

    def count_logins():
        nonlocal login_count
        login_count += 1
        return login_count

    return count_logins


count_logins = login()
print(count_logins())
print(count_logins())
print(count_logins())


"""7masala"""
