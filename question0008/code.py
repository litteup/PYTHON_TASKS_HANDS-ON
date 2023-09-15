
#Days to years, weeks and days conversion

days = int(input("Enter days: "))
years = days // 365
daysAfterYear = days % 365
weeks = daysAfterYear // 7
daysLeft = daysAfterYear % 7

print(f'YEARS: {years}\nWEEKS: {weeks} \nDAYS: {daysLeft}')






