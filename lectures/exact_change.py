def exact_change(bills):
    amount_of_each = dict()
    amount_of_each[5] = 0
    amount_of_each[10] = 0
    amount_of_each[20] = 0

    for bill in bills:
        amount_of_each[bill] += 1
        amount_owed = bill - 5
        if amount_owed == 5:
            if amount_of_each[5] == 0:
                return False
            else:
                amount_of_each[5] -= 1

        if amount_owed == 15:
            if amount_of_each[10] >= 1 and amount_of_each[5] >= 1:
                amount_of_each[10] -= 1
                amount_of_each[5] -= 1
            elif amount_of_each[10] == 0 and amount_of_each[5] >= 3:
                amount_of_each[5] -= 1
            else:
                return False

    return True


if __name__ == "__main__":
    print(exact_change([5,5,5,10,20]))
    print(exact_change([5,5,10,10,20]))
    print(exact_change([5,5,10]))
    print(exact_change([10,10]))