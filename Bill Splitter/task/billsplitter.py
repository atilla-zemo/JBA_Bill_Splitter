# write your code here
import random

try:
    number_of_friends = int(input("Enter the number of friends joining (including you):\n"))
    if not (number_of_friends > 0):
        raise TypeError
    else:
        friends = dict()
        print("\nEnter the name of every friend (including you), each on a new line:")
        for num in range(number_of_friends):
            friends[str(input())] = 0

    total_bill_value = int(input("\nEnter the total bill value:\n"))

    fair_share = round(total_bill_value / number_of_friends, 2)
    for key in friends:
        friends[key] = fair_share

    print(random.sample(friends, 1))
    lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky_feature == "Yes":
        print(f" is the lucky one!")


except TypeError:
    print("No one is joining for the party")
