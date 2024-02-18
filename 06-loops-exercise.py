
# 7 boom game
# print boom if number divide by 7 or has the 7 in it's digit
for n in range(1,101):
    num_contains_seven = "7" in str(n)
    if n % 7 == 0 or num_contains_seven:
        print("boom")
    else:
        print(n)