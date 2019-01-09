from DataStructureProgram.Stack import *
stack = Stack()
stack1 = Stack()


def isleap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # checking whether the year is leap year or not
        return True
    else:
        return False


def calender_stack(month, year):
    """
    This method is used to print calender of given month and year.
    In this method calender is created using stack
    :param month:month given ser
    :param year: year given by year
    :return: nothing
    """
    day = ['Sun', ' Mon', ' Tue', ' Wed', ' Thu', 'Fri', ' Sat']

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    values = 1
    d = 1

    m = month
    y = year
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + 31 * m0 // 12) % 7

    if isleap_year(year):  # check leap year
        days[1] = 29
    row = 6
    column = 7

    print('Your Calender is Ready\n')

    for i in range(0, 6 + 1):
        print(day[i], end=' ')  # print day's for calender
    print()
    for i in range(row):

        for j in range(column):

            if values <= days[m - 1]:  # while d0 is less than j
                if i == 0 and j < d0:  # it will print blank space
                    stack.push(' ')  # use push() to add blanks
                    continue

                stack.push(values)  # add days using push() method
                values += 1

    for i in range(stack.size()):
        stack_element = stack.pop()  # pop element from stack and store in local variable
        stack1.push(stack_element)  # again push element into stack for reverse

    for i in range(row):

        for j in range(column):
            if stack1.size() > 0:
                x = stack1.pop()  # access element one by one using pop() method
                x1 = str(x).ljust(4)  # ljust() method to print in calender structure
                print(x1, end=" ")

        print()
        print()


def calender_stack_runner():
    """
    This method is used as runner for calender_stack(month, year) method
    :return:  nothing
    """
    global year, month
    try:
        month = int(input('Enter Month'))
    except Exception as e:
        print(e)
        print("Enter integer only ")
    try:
        year = int(input('Enter Year'))
    except Exception as e:
        print(e)
        print("Enter integer only")

    calender_stack(month, year)


calender_stack_runner()
