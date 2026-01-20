import matplotlib.pyplot as plt
students = {
    "A": [70, 75, 80, 85, 90, 78, 88],
    "B": [60, 65, 70, 68, 72, 66, 69],
    "C": [80, 85, 88, 90, 92, 86, 89]
}

averages = {}
class_total = 0

for name in students:
    total = 0
    for mark in students[name]:
        total += mark

    avg = total / 7
    averages[name] = avg
    class_total += avg

class_avg = class_total / len(students)

highest_avg = 0
topper = ""

for name in averages:
    if averages[name] > highest_avg:
        highest_avg = averages[name]
        topper = name

print("Topper:", topper)
print("Class Average:", class_avg)

print("Students below class average:")
for name in averages:
    if averages[name] < class_avg:
        print(name)

names = list(averages.keys())
avg_marks = list(averages.values())

plt.bar(names, avg_marks)
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Average Marks of Students")
plt.show()
