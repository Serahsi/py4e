hrs = input("Enter hours: ")
h = float(hrs)
rate = input("Enter rate: ")
r = float(rate)

if h <= 40:
    pay = h * r
elif h > 40:
    pay = (40 * r) + (h - 40) * (r * 1.5)

print("Your pay is", pay)

