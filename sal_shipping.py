weight=input("How heavy is ur package? (lbs, no unit needed ) ")
weight=int(weight)
price = 0

## ground shippinh
if weight<=2:
  price= 1.5*weight + 20.00
elif 6>=weight>2:
  price = 3.0*weight + 20.00
elif 10>= weight > 6:
  price = 4.0*weight +20.00
elif weight>10:
  price = 4.75*weight + 20.00
else:
  print("dwg wut")
print("Ground Shipping Regular: $",price)

cost_ground_premium = 125.00

print("Ground Shipping Premium $", cost_ground_premium)

#DRONE DROPS

if weight<=2:
  price= 4.5*weight 
elif 6>=weight>2:
  price = 9.0*weight 
elif 10>= weight > 6:
  price = 12.0*weight 
elif weight>10:
  price = 14.25*weight 
else:
  print("dwg wut")

print("Drone drop: $"+str(price))
print("Choose which one is the cheapest (best option) or choose the most expensive one to help us ;) ")
print(""" Sal's Shipping Signing Off 

      Have a good day! """)
