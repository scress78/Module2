"""
This program converts a childs age in months into years and then outputs
how old they are in months and years old.

Author: Spencer Cress
Date: 06/02/2020
"""

def convert_to_months(x):
    return int(x) / 12

if __name__ == "__main__":
    age_in_months = input("Enter child's age in months: ")
    ages_in_years = convert_to_months(age_in_months)

if __name__ == "__main__":
    print(str(age_in_months)+' months is '+str(ages_in_years)+' years old')

#I think this finally works
#it has taken two more hours than I thought it would :)

