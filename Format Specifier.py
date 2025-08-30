#format specifiers = { value:flags} format a value based on what flags are inserted
#.(number)f = round to that many decimal places (fixed point)
#:(number) = allocate that many spaces
#: 03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate position value
# := = place sign to left most position
# : = insert a space before positive numbers
# :, = comma separator
price1 = 3.1459
price2 = -9833754.78
price3 = 12.34

print(f"Price 1 is Rs.{price1: .1f}")
print(f"Price 2 is Rs.{price2:,}")
print(f"Price 3 is Rs.{price3:+,.2f}")
