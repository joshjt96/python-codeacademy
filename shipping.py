weight = 4.8

# Ground Shipping

ground_flat_charge = 20
premium_shipping = 125
ground_shipping_text = "Ground Shipping Cost: "

print("Ground Shipping Premium: $", + premium_shipping)

if weight <= 2:
  ground_shipping = weight * 1.5 + ground_flat_charge
  print(ground_shipping_text, + ground_shipping)
elif weight > 2 and weight <= 6:
    ground_shipping = weight * 3 + ground_flat_charge
    print(ground_shipping_text, + ground_shipping)
elif weight > 6 and weight <= 10:
    ground_shipping = weight * 4 + ground_flat_charge
    print(ground_shipping_text, + ground_shipping)
elif weight > 10:
    ground_shipping = weight * 4.75 + ground_flat_charge
    print(ground_shipping_text, + ground_shipping)

# Drone Shipping

drone_shipping_text = "Drone Shipping Cost: "

if weight <= 2:
  drone_shipping = weight * 4.50
  print(drone_shipping_text, + drone_shipping)
elif weight > 2 and weight <= 6:
    drone_shipping = weight * 9
    print(drone_shipping_text, + drone_shipping)
elif weight > 6 and weight <= 10:
    drone_shipping = weight * 12
    print(drone_shipping_text, + drone_shipping)
elif weight > 10:
    drone_shipping = weight * 14.25
    print(drone_shipping_text, + drone_shipping)