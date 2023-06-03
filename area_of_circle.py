# Function
def area_of_circle(rad) -> int:
    pi = 22/7
    area = rad * rad * pi
    return area


# Getting the radius value from the user
radius = int(input("Enter the value of Radius : "))
output = area_of_circle(radius)
print(output)


