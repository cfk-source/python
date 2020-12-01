side_a = float(input('enter side A value'))
side_b = float(input('enter side B value'))
side_c = float(input('enter side C value'))

print('Side A =', side_a, 'Side B =', side_b, 'Side C =', side_c)

triangle_area = side_a * side_b * side_c
print('Triangle area =',triangle_area)

if (side_a == side_b) or (side_b == side_c) or (side_a == side_c):
    print('triangle is hip-equal')