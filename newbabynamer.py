#! /usr/bin/python3
import random
import pandas

url = 'https://www.ssa.gov/OACT/babynames/index.html'
htmldata = pandas.read_html(url)
namedata = htmldata[0]

print("Welcome to the Baby Name Chooser!")
print("This script randomly picks a name from a list of the 10 top boys' and girls' names from the Social Security Administration.")
print("Is this name for a boy or a girl?")
while True:
    gender = input("Please type 'boy' or 'girl'")
    if gender == 'boy':
        break
    elif gender == 'girl':
        break
    else:
        print("Please try again")

while True:
    if gender == "boy":
        name = namedata.loc[random.randint(0, 9), 'Male name']
    elif gender == "girl":
        name = namedata.loc[random.randint(0, 9), 'Female name']
    print("How about " + name + " as a name?")
    response = input("Please type 'yes' or 'no'")
    if response == 'yes':
        print("Congratulations!  You have chosen a baby name!")
        break
    else:
        print("Let's try again.")
