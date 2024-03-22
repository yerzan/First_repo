def real_cost(base: int, discount: int = 0):
    return base * (1 - discount)

price_Nemiroff = 50
price_Cognac = 100
price_Licour = 500

final_price_Nemiroff = real_cost(price_Nemiroff)
final_price_Cognac = real_cost(price_Cognac, 0.05)
final_price_Licour = real_cost(price_Licour, 0.5)

print(f"Final price Nemiroff {final_price_Nemiroff}")
print(f"Final price Cognac {final_price_Cognac}")
print(f"Final price Licour {final_price_Licour}")
