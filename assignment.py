paper_sheets=int(input("Enter the number of paper sheets"))
total_width = 0 
below_range = 0
in_range = 0 
above_range = 0
def classify(value):
    if value < 208:
        return "Below range" 
    elif value <=212:
        return "In range"
    else:
        return "Above range"
def calculate_average(total, count):
    return total/count

for i in range (paper_sheets):
    width=int(input("Enter the paper sheet width:"))

    result = classify (width)

    total_width += width 

if result =="Below range":
        below_range+=1
elif result =="In range":
        in_range+=1
else:
        above_range+=1  

average_width = calculate_average(total_width, paper_sheets)
print(f"Average_width:{average_width:.1f} mm")
print(f"Total_ width{total_width}mm")
print(result)
print(f"Below range: {below_range}")
print(f"In range: {in_range}")
print(f"Above range: {above_range}")