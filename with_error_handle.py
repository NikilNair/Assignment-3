'''
For this assignment this code will check if a given year is a leap year. This code
must be run as python 3, and requests the user to input a year. Afterwards the
program will print whether or not the given year is a leap year.

'''
year = None
while year is None:
  input_val = input("Which year do you want to check? ")
  try:
    year = int(input_val)
  except ValueError:
    print(f"{input_val} is not a number, please enter a number only".format(input=input_val))


if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"{year} is a leap year.")
    else:
      print(f"{year} is not a leap year.")
  else:
    print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")

