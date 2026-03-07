def is_sum_of_three_squares(m):
    for a in range(int(m**0.5) + 1):
        for b in range(int(m**0.5) + 1):
            for c in range(int(m**0.5) + 1):
                if a*a + b*b + c*c == m:
                    return True
    return False
m = int(input("Enter an integer: "))
if is_sum_of_three_squares(m):
    print("True")
else:
    print("False")
