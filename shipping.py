weight = 8.4

# Ground Shipping

ground_flat_charge = 20

if weight <= 2:
  ground_shipping = weight * 1.5 + ground_flat_charge
  print(ground_shipping)
elif weight > 2 and weight <= 6:
  print("$3.00")
elif weight > 6 and weight <= 10:
  print("$4.00")
elif weight > 10:
  print("$4.75")