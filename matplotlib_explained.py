"""
MATPLOTLIB FOR DATA ANALYTICS - EXPLAINED STEP BY STEP
======================================================

Who is this for?  Complete beginners in data analytics.
How to use it?    Read each section, run the file, and look at the chart it
                  produces. Close a chart window to see the next one.

Install the libraries once (in your terminal / command prompt):
    pip install matplotlib pandas numpy

Run the file:
    python matplotlib_explained.py


WHAT IS MATPLOTLIB?
-------------------
Matplotlib is the most popular Python library for drawing charts.
In data analytics we use charts to:
    1. EXPLORE data   -> "What does my data look like?"
    2. FIND patterns  -> "Are sales going up? Are there outliers?"
    3. COMMUNICATE    -> "Show my manager the story in the data."


THE PARTS OF A CHART (learn these words, they are used everywhere)
------------------------------------------------------------------
    Figure : the whole canvas / window / picture.  (Think: the sheet of paper)
    Axes   : one single chart drawn inside the figure. (Think: one drawing on the paper)
             A figure can hold ONE axes or MANY axes (a dashboard).
    Axis   : the x-axis (horizontal) and y-axis (vertical) of an axes.
    Title  : text at the top of a chart. Says WHAT the chart shows.
    Label  : text next to an axis. Says WHAT the numbers are (e.g. "Sales ($)").
    Legend : the small box that explains which colour/line is which series.
    Grid   : light background lines that make values easier to read.
    Marker : the dot/square drawn on each data point.
"""

# =====================================================================
# STEP 1: IMPORT THE LIBRARIES
# =====================================================================

# "import" loads a library so we can use it.
# "as plt" gives it a short nickname so we type plt.plot() instead of
# matplotlib.pyplot.plot(). Everyone in the world uses the nickname "plt".
import matplotlib.pyplot as plt

# NumPy = fast maths on numbers and arrays (lists of numbers).
# We use it here to create fake data and calculate things like averages.
import numpy as np

# pandas = tables of data (like Excel inside Python).
# A table in pandas is called a DataFrame. Nickname: pd.
import pandas as pd


# =====================================================================
# STEP 2: CREATE SOME DATA
# =====================================================================
# Real projects load data from a file, for example:
#       df = pd.read_csv("my_data.csv")        # CSV file
#       df = pd.read_excel("my_data.xlsx")     # Excel file
# To keep this tutorial runnable for everyone, we create sample data.

# Random numbers change every run. A "seed" fixes them so you get the
# same numbers each time (useful when learning and when sharing results).
np.random.seed(42)

# --- Data set 1: monthly business numbers (a small table) ---
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]   # a Python list of text
sales  = [200, 240, 310, 280, 350, 420]               # a list of numbers
costs  = [150, 170, 200, 210, 240, 260]

# Build a DataFrame (table) from a dictionary:
#   key   = column name
#   value = the list of values in that column
df = pd.DataFrame({"month": months, "sales": sales, "costs": costs})

# Create a NEW column by doing maths on existing columns.
# Pandas does it row by row: profit = sales - costs for every month.
df["profit"] = df["sales"] - df["costs"]

print(df)   # Print the table so you can see what the data looks like.
print()

# --- Data set 2: 500 employee ages ---
# np.random.normal(mean, spread, how_many) makes numbers that cluster around
# the mean in a bell shape (a "normal distribution"), just like real ages.
ages = np.random.normal(loc=35, scale=8, size=500)

# --- Data set 3: experience vs salary for 100 employees ---
# np.random.uniform(low, high, how_many) makes numbers evenly between low and high.
experience = np.random.uniform(0, 15, 100)                    # years, 0 to 15
# Salary rises by about 3000 per year of experience, plus random noise,
# so there IS a real relationship for our chart to reveal.
salary = 30000 + experience * 3000 + np.random.normal(0, 5000, 100)

# --- Data set 4: employees per department ---
departments = ["HR", "IT", "Sales", "Finance"]
headcount   = [12, 30, 25, 15]


# =====================================================================
# CHART 1: LINE CHART
# ---------------------------------------------------------------------
# WHAT IT IS : points joined by a line.
# WHEN TO USE: to show how something CHANGES OVER TIME (days, months, years).
# HOW TO READ: go left to right. Rising line = growth, falling line = decline.
#              The gap between two lines shows how different two series are.
# =====================================================================

# Create a new empty figure (canvas).
# figsize=(width, height) is in INCHES. (8, 4) = wide and short, good for trends.
plt.figure(figsize=(8, 4))

# plt.plot(x_values, y_values, ...) draws a line.
#   df["month"]  -> x values (the months on the horizontal axis)
#   df["sales"]  -> y values (the numbers on the vertical axis)
#   marker="o"   -> draw a circle on every data point ("s" = square, "^" = triangle)
#   color        -> line colour. "tab:blue" is one of Matplotlib's built-in nice colours.
#   label        -> the name shown in the legend for this line.
plt.plot(df["month"], df["sales"], marker="o", color="tab:blue", label="Sales")

# Draw a second line on the SAME chart. Calling plt.plot() again adds to the
# current chart instead of creating a new one.
#   linestyle="--" -> dashed line ("-" solid, ":" dotted, "-." dash-dot)
plt.plot(df["month"], df["costs"], marker="s", color="tab:red",
         linestyle="--", label="Costs")

plt.title("Monthly Sales vs Costs")   # Title: WHAT the chart is about.
plt.xlabel("Month")                   # Label for the horizontal axis.
plt.ylabel("Amount ($)")              # Label for the vertical axis (include units!).

# Show the legend box. It uses the label="..." text we gave each line above.
# WITHOUT the label arguments, plt.legend() would have nothing to show.
plt.legend()

# Light grid. alpha is transparency: 0 = invisible, 1 = solid. 0.3 = subtle.
plt.grid(alpha=0.3)

# tight_layout() automatically adjusts spacing so labels are not cut off.
plt.tight_layout()

# Save the chart as an image file in the folder where you run the script.
# dpi = dots per inch = sharpness. 150 is good for reports/slides.
# IMPORTANT: call savefig BEFORE plt.show(), because show() clears the figure.
plt.savefig("chart1_line.png", dpi=150)

# Open the chart in a window. Close the window to continue to the next chart.
plt.show()

# WHAT THIS CHART TELLS US: both sales and costs grow, but sales grow faster,
# so the gap (profit) gets bigger over the months.


# =====================================================================
# CHART 2: BAR CHART
# ---------------------------------------------------------------------
# WHAT IT IS : one bar per category; taller bar = bigger value.
# WHEN TO USE: to COMPARE CATEGORIES (departments, products, regions).
# HOW TO READ: compare the heights of the bars.
# =====================================================================

plt.figure(figsize=(6, 4))

# plt.bar(categories, values) draws vertical bars.
# It RETURNS the bars, which we store in a variable so we can label them.
bars = plt.bar(departments, headcount, color="tab:green")

plt.title("Employees by Department")
plt.ylabel("Number of employees")

# Write the value on top of every bar so people don't have to guess.
plt.bar_label(bars)

plt.tight_layout()
plt.show()

# TIP: when category names are long, use plt.barh() for HORIZONTAL bars.
# TIP: sort categories from biggest to smallest to make the chart easier to read.


# =====================================================================
# CHART 3: HISTOGRAM
# ---------------------------------------------------------------------
# WHAT IT IS : shows how the values of ONE numeric column are spread out.
#              The data is cut into "bins" (ranges) and the bar height is how
#              many values fall inside each bin.
# WHEN TO USE: to see the SHAPE of data: where most values are, whether it is
#              symmetric, skewed, or has strange values.
# HOW TO READ: tall bars = many values in that range.
# DIFFERENCE FROM A BAR CHART: bar chart compares categories, a histogram shows
#              the distribution of numbers, so its bars touch each other.
# =====================================================================

plt.figure(figsize=(6, 4))

# bins=20 -> split the age range into 20 equal buckets.
#   Too few bins hide detail; too many bins look noisy. Try 10 to 30.
# edgecolor="white" -> thin white outline so neighbouring bars are separated.
plt.hist(ages, bins=20, color="tab:purple", edgecolor="white")

# Draw a vertical line at the average age.
#   ages.mean() calculates the average of all 500 ages.
#   f"...{value:.1f}" is an f-string: it puts the number inside text,
#   and ":.1f" means "show 1 decimal place".
plt.axvline(ages.mean(), color="black", linestyle="--",
            label=f"Mean = {ages.mean():.1f}")

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of employees")   # histogram y-axis = count (frequency)
plt.legend()
plt.tight_layout()
plt.show()

# WHAT THIS CHART TELLS US: most employees are around 35, and fewer are very
# young or very old (a bell shape).


# =====================================================================
# CHART 4: SCATTER PLOT
# ---------------------------------------------------------------------
# WHAT IT IS : each row of data is ONE dot placed by two numbers (x and y).
# WHEN TO USE: to check if TWO NUMERIC VARIABLES are RELATED (correlation).
# HOW TO READ: dots rising left to right = positive relationship
#              (as x goes up, y goes up). Dots falling = negative relationship.
#              A shapeless cloud = no relationship.
# =====================================================================

plt.figure(figsize=(6, 4))

# alpha=0.7 makes dots slightly see-through so overlapping dots are visible.
plt.scatter(experience, salary, alpha=0.7, color="tab:orange", label="Employees")

# --- Add a trend line (the "line of best fit") ---
# np.polyfit(x, y, 1) finds the straight line y = slope * x + intercept
# that best matches the dots. The "1" means a straight line (degree 1).
slope, intercept = np.polyfit(experience, salary, 1)

# np.linspace(start, stop, n) creates n evenly spaced numbers.
# We need many x values to draw a smooth straight line.
x_line = np.linspace(experience.min(), experience.max(), 100)

# Compute the y value on the line for each x, then draw it.
plt.plot(x_line, slope * x_line + intercept, color="black", label="Trend line")

plt.title("Experience vs Salary")
plt.xlabel("Years of experience")
plt.ylabel("Salary ($)")
plt.legend()
plt.tight_layout()
plt.show()

# WHAT THIS CHART TELLS US: more experience goes with higher salary.
# The "slope" tells us how much salary rises per extra year of experience.
# REMEMBER: correlation does NOT prove one thing causes the other.
print(f"Salary increases by about ${slope:,.0f} per extra year of experience")


# =====================================================================
# CHART 5: BOX PLOT
# ---------------------------------------------------------------------
# WHAT IT IS : a compact summary of one numeric column.
# WHEN TO USE: to see the MEDIAN, the SPREAD and the OUTLIERS quickly,
#              especially to compare several groups side by side.
# HOW TO READ:
#     - Orange line in the box : the median (middle value)
#     - The box                : the middle 50% of the data (Q1 to Q3)
#     - The whiskers           : the normal range of the rest of the data
#     - Dots beyond whiskers   : OUTLIERS (unusually high or low values)
# =====================================================================

plt.figure(figsize=(5, 4))
plt.boxplot(salary)
plt.title("Salary Spread")
plt.ylabel("Salary ($)")
plt.tight_layout()
plt.show()


# =====================================================================
# CHART 6: PIE CHART
# ---------------------------------------------------------------------
# WHAT IT IS : a circle divided into slices; slice size = share of the total.
# WHEN TO USE: only when you have FEW categories (about 5 or fewer) and want to
#              show PARTS OF A WHOLE. Humans compare bar heights more accurately
#              than slice angles, so a bar chart is often the better choice.
# =====================================================================

plt.figure(figsize=(5, 5))

# labels     -> the name written next to each slice
# autopct    -> automatically print the percentage on each slice.
#               "%1.1f%%" means: show 1 decimal place and add a % sign.
# startangle -> where the first slice begins (90 = at the top).
plt.pie(headcount, labels=departments, autopct="%1.1f%%", startangle=90)

plt.title("Share of Employees by Department")
plt.show()


# =====================================================================
# CHART 7: SEVERAL CHARTS IN ONE FIGURE (SUBPLOTS)
# ---------------------------------------------------------------------
# WHEN TO USE: to put related charts side by side, like a mini dashboard.
#
# TWO STYLES OF MATPLOTLIB (important to understand):
#   1) pyplot style  : plt.plot(), plt.title()  ... used above. Quick and simple.
#   2) object style  : fig, ax = plt.subplots() then ax.plot(), ax.set_title()
#                      You control EXACTLY which chart (axes) you draw on.
#                      Use this style whenever you have more than one chart.
# =====================================================================

# plt.subplots(rows, columns) creates a Figure and a grid of Axes.
#   fig  = the whole canvas
#   axes = a 2x2 grid of charts, so we pick one with axes[row, column]
#          (counting starts at 0, so axes[0, 0] is top-left)
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Top-left: profit trend line
axes[0, 0].plot(df["month"], df["profit"], marker="o", color="tab:green")
axes[0, 0].set_title("Profit Trend")        # NOTE: ax.set_title, not plt.title
axes[0, 0].set_ylabel("Profit ($)")         # NOTE: ax.set_ylabel, not plt.ylabel

# Top-right: bar chart
axes[0, 1].bar(departments, headcount, color="tab:blue")
axes[0, 1].set_title("Headcount by Department")

# Bottom-left: histogram
axes[1, 0].hist(ages, bins=15, color="tab:purple", edgecolor="white")
axes[1, 0].set_title("Age Distribution")

# Bottom-right: scatter plot
axes[1, 1].scatter(experience, salary, alpha=0.7, color="tab:orange")
axes[1, 1].set_title("Experience vs Salary")
axes[1, 1].set_xlabel("Years")
axes[1, 1].set_ylabel("Salary ($)")

# A title for the entire figure (above all four charts).
fig.suptitle("Mini Dashboard", fontsize=14)

fig.tight_layout()                           # stop the charts overlapping
fig.savefig("chart7_dashboard.png", dpi=150)
plt.show()


# =====================================================================
# CHART 8: PLOT DIRECTLY FROM PANDAS (a shortcut you will use every day)
# ---------------------------------------------------------------------
# A DataFrame has its own .plot() method that calls Matplotlib for you.
# It saves typing because column names become labels automatically.
# =====================================================================

# kind can be "line", "bar", "barh", "hist", "scatter", "box", "pie"
df.plot(x="month", y=["sales", "costs"], kind="bar", figsize=(7, 4))

# Pandas draws the chart, but we can still use plt to polish it.
plt.title("Sales and Costs by Month")
plt.ylabel("Amount ($)")
plt.xticks(rotation=0)    # keep month names horizontal (default is rotated)
plt.tight_layout()
plt.show()


# =====================================================================
# SUMMARY: WHICH CHART SHOULD I USE?
# =====================================================================
#   Question you are asking                  Chart            Code
#   ---------------------------------------  ---------------  ----------------
#   How does it change over time?            Line chart       plt.plot()
#   Which category is bigger?                Bar chart        plt.bar()
#   How is one number spread out?            Histogram        plt.hist()
#   Are two numbers related?                 Scatter plot     plt.scatter()
#   What is typical, and are there outliers? Box plot         plt.boxplot()
#   What share does each part have?          Pie chart        plt.pie()
#
# GOOD-CHART CHECKLIST (do this for every chart you make):
#   [ ] A clear title that says what the chart shows
#   [ ] Axis labels with units ($, %, years ...)
#   [ ] A legend if there is more than one line/colour
#   [ ] Readable text: not cut off, not overlapping (tight_layout helps)
#   [ ] Only as much decoration as needed. Simple is easier to understand.
#
# COMMON BEGINNER MISTAKES:
#   - Calling plt.show() before plt.savefig(): the saved image will be blank.
#   - Forgetting label="..." and then calling plt.legend(): legend is empty.
#   - Using a pie chart with many slices: use a bar chart instead.
#   - Not labelling axes: nobody knows what the numbers mean.
#
# NEXT STEPS:
#   1. Replace the sample data with your own CSV/Excel file.
#   2. Learn seaborn (built on Matplotlib): prettier charts with less code.
#   3. Practise: load a dataset, then make a line, a histogram and a scatter plot.
