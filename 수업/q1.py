money = 5000
price = 2800
left = money-price
print("거스름돈 :", left)
print("500원 동전 개수 :", int(left/500))
print("100원 동전 개수 :", int((left%500)/100))

