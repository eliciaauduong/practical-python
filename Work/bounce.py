# bounce.py
#
# Exercise 1.5
height = 100
bounce_count = 0
while bounce_count < 10:
    height *= 0.6
    print(bounce_count + 1, round(height, ndigits = 4))
    bounce_count += 1