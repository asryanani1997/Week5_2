x= ({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
})

y=round((x["sell_price"]-x["cost_price"])*x["inventory"])
print(y)