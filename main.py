import random
guessed_num= int(input("Guess a number between 1 to 100"))
generated_num= random.randint(1,100)

if guessed_num<generated_num:
  print("You guessed too smaller")
elif guessed_num>generated_num:
  print("you guessed too larger")
else:
  print("Hurray!............ you are winner")


