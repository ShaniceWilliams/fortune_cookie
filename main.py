import random

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,5)

fortune_text = ""

if fortune_number == 1:
  fortune_text = "You will have a great day!"
if fortune_number == 2:
  fortune_text = "Every cloud has a silver lining!"
if fortune_number == 3:
  fortune_text = "Tell the people you love that you love them."
if fortune_number == 4:
  fortune_text = "Tomorrow is a day for making decisions."
if fortune_number == 5:
  fortune_text = "This will be your year!"

print(f"{fortune_text} Your lucky Number is: {lucky_number}")