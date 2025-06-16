
temperature = 30
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

from test.test_selectors import SelectSelectorTestCase

age = 22
if age >= 18:
    message = " Eligible"
else:
    message = "Not eligible"

age = 22

message = "Eligible" if age >= 18 else "Not eligible"
print(message)