from decimal import Decimal,getcontext

getcontext().prec = 6
a = float(Decimal(0.5111))
b = float(Decimal(1.2333))
c = float(Decimal(2))
result = (Decimal(3)+Decimal(5)+Decimal(77)+Decimal(23)+Decimal(0.57))/Decimal(6)
print(float(result))