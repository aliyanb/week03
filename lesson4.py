# shop_cash = [10000, 34000, 30000, 45000, 90000, 7899]
# expenses = [1000, 3000, 20000, 5000, 5600, 7654, 3425]
# all_cash = sum(shop_cash)
# all_expenses = sum(expenses)
# profit = all_cash - all_expenses
# print(profit)

# funtion
# shop_cash = [10000, 34000, 30000, 45000, 90000, 7899]
# expenses = [1000, 3000, 20000, 5000, 5600, 7654, 3425]
# shop_cash2 = [100030, 340020, 303000, 450400, 900020, 72899]
# expenses2 = [10003, 30200, 200300, 50400, 56200, 76254, 34225]
# def get_money(shop_cash: list, expenses: list):
#     all_cash = sum(shop_cash)
#     all_expenses = sum(expenses)
#     profit = all_cash - all_expenses
#     return profit

# print(get_money(shop_cash, expenses))      result 1
# monday = get_money(shop_cash, expenses)
# day2 = get_money(shop_cash2, expenses2)
# print(day2)


# *args **kwargs   аргументы

# def get_argument(*args, **kwargs):
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)

# get_argument(1, 2, 3, "gfgh", {1, 0})
# get_argument(1, 2, 3, "gfgh", {1, 0}, name="Aliya", age=21)

# d = {
#     'name': 'Aliya',
#     'age': 21
# }


def get_list_square(*args, **kwargs):
    result = []
    if args:
        for i in args:
            result.append(i**2)
    if kwargs:
        for key, value in kwargs.items():
            if type(value) == str:
                kwargs.update({
                    key: value.upper()
                })
            elif type(value) == set:
                kwargs.update({
                    key: [value]
                })


    return result, kwargs
print(get_list_square(1, 3, 5, 4, 22, name="Aliya", age=21, sets={1, 3}))












