import pandas

data = pandas.read_csv("lifestyle_data.csv")
print(data)
# What data type is `data` as output from the `read_csv()` method?
# Using the import, the data variable now is a DataFrame, a tabular exppression of data

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# - You can open the csv file to see what data is available.
# - Use the pandas documentation to explore functions that you can use.
# - Leave your code under the comments.

# Find the total number of students
#print(data.index) # This means there are 2000 students in this csv
# Find the mean average GPA of the students
#print(data['GPA'].mean()) # 3.11596
# Find the standard deviation of how much sleep students get per day
#print(data['Sleep_Hours_Per_Day'].std()) # 1.4609485353055411
# Find the maximum amount of study hours per day
#print(data['Study_Hours_Per_Day'].max()) # 10.0
# Sort the students by social hours per day ascending (lowest -> highest)
#print(data.nsmallest(2000, ['Social_Hours_Per_Day']))
# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
