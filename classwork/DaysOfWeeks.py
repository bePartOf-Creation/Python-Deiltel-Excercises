my_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
new_week_list = ["Java", "Digging-Deep", "Python", "Sleep", "Catch Cruise", "Flex", "Flex Again"]
squares = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]


def modify_week(weeks):
    weeks.append(weeks.pop(0))
    print(weeks)


def my_todo_list(weeks, my_plans):
    to_do_list = dict(zip(weeks, my_plans))
    return print(to_do_list)


def make_daily_plan(weeks, my_plans):
    my_daily_plan = {}
    for x, y in zip(weeks, my_plans):
        my_daily_plan[x] = y
    return print(my_daily_plan)


def convert_to_dict(square, value):
    diction = {}
    for x, y in zip(square, value):
        diction[x] = y ** 2
    return print(diction)


def lazy_range(n):
    """a lazy version of range"""
    i = 0
    while i < n:
        yield i
        i += 1
    return i


data_science_collection = {}


def ds_group():
    for i in range(3):
        group_key = int(input("Enter your group number : "))
        group_members = input("Enter your Group Names : ").split(",")
        data_science_collection[group_key] = group_members
    return print(data_science_collection)


def main():
    modify_week(my_week)
    my_todo_list(my_week, new_week_list)
    make_daily_plan(my_week, new_week_list)
    convert_to_dict(squares, values)
    print(lazy_range(6))
    ds_group()


if __name__ == '__main__':
    main()
