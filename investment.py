shares = 10
share_price = 150
investment_cost = shares * share_price

print("Total Investment Cost:", investment_cost)

new_share_price = 175
current_value = shares * new_share_price
profit = current_value - investment_cost
percentage_return = (profit / investment_cost) * 100

print("Current Investment Value:", current_value)
print("Profit:", profit)
print("Percentage Return:", percentage_return)
