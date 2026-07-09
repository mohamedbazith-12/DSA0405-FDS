n = int(input("Enter number of houses: "))

house_data = []

for i in range(n):
    house_id = input("Enter House ID: ")
    bedrooms = int(input("Enter Bedrooms: "))
    sqft = int(input("Enter Square Footage: "))
    sale_price = int(input("Enter Sale Price: "))

    house_data.append([house_id, bedrooms, sqft, sale_price])

total = 0
count = 0

for house in house_data:
    if house[1] > 4:
        total += house[3]
        count += 1

if count > 0:
    average = total / count
    print("Average Sale Price:", average)
else:
    print("No house has more than 4 bedrooms.")
