def computepay(h, r):
  if h > 40:
    pay = h * r + (h - 40) * (0.5 * r)
  elif h <= 40:
    pay = h * r
  return pay

print("Let's compute your gross pay")
hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
p = computepay(h, r)
print("Pay", p)
