d_ft = int(input("Input distance in feet: "))
d_inches = d_ft * 12
d_yards = d_ft / 3
d_miles = d_ft / 528011
d_meters = d_ft / 3.28
d_centimeters = d_ft * 30.48
d_milimeters = d_ft * 304.8

print("If the distance is %.2f feet:" % d_ft)
print("The distance in inches is %.2f inches." % d_inches)
print("The distance in yards is %.2f yards." % d_yards)
print("The distance in miles is %.2f miles." % d_miles)
print ("The distance in miles is %.2f meters." % d_meters)
print ("The distance in miles is %.2f centimeters." % d_centimeters)
print ("The distance in miles is %.2f milimeters." % d_milimeters)


d_pint = int(input("Input amount in pint: "))
d_quarts = d_pint / 2 
d_cups = d_pint * 2
d_litre = d_pint * 0.473
d_centilitre = d_pint * 47.31
d_mililitre = d_pint * 473.13

print("If the amount is %.2f pints:" % d_pint)
print("The amount in quart is %.2f quarts" % d_quarts) 
print("The amount in cups is %.2f cups" % d_cups) 
print("The amount in litre is %.2f litres" % d_litre) 
print("The amount in centilitre is %.2f centilitre" % d_centilitre) 
print("The amount in mililitre is %.2f mililitres" % d_mililitre) 