from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    sum_num = 0
    for num in number_list:
        sum_num += float(Decimal(num))
        #print(num)
        #print(sum_num)
    result = float(Decimal(sum_num)/Decimal(len(number_list)))
    print(result)
    return float(Decimal(result))

print(decimal_average([3, 5, 77, 23, 0.57], 6))
print(decimal_average([4.5788689699797, 34.7576578697964, 86.8877666656633, 12], 6))
print(decimal_average([31, 55, 177, 2300, 1.57], 9))
# getcontext().prec = 6
# result = float(Decimal(3)+Decimal(5)+Decimal(77))
# getcontext().prec = 6
# print(Decimal(4.5788689699797))
# print(Decimal(34.7576578697964))
# print(Decimal(86.8877666656633))
# print(float(Decimal(12)))