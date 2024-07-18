import turtle
from collections import Counter

n_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(n_num)
get_sum = sum(n_num)
mean = get_sum / n
n_num.sort()
if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v ==max(list(data.values()))]
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))

# Set up turtle screen
window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Mean, Median, and Mode")

# Draw mean value
mean_turtle = turtle.Turtle()
mean_turtle.penup()
mean_turtle.goto(-100, 50)
mean_turtle.write("Mean / Average: " + str(mean), font=("Arial", 16, "normal"))

# Draw median value
median_turtle = turtle.Turtle()
median_turtle.penup()
median_turtle.goto(-100, 0)
median_turtle.write("Median: " + str(median), font=("Arial", 16, "normal"))

# Draw mode value
mode_turtle = turtle.Turtle()
mode_turtle.penup()
mode_turtle.goto(-100, -50)
mode_turtle.write(get_mode, font=("Arial", 16, "normal"))

turtle.done()
