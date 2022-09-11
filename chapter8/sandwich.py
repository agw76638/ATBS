import pyinputplus as pyip

bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt = 'What type of bread would you like?\n')
print(bread)
protein = pyip.inputMenu(['chiken', 'turkey', 'ham', 'tofu'])
cheese = pyip.inputYesNo(prompt='Do you want cheese?\n')
if cheese == yes:
    cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
pyip.inputYesNo(prompt='Do you want')
pyip.inputInt(prompt="How maany sandwiches do you want?\n", min=1)

# TODO display total cost