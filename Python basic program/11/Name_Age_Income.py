import csv

# create the data to be written to the CSV file
data = [['Name', 'Age', 'Income'],
        ['Subash', 22, 1000000],
        ['Invicti', 22, 800000],
        ['Drudge', 21, 700000],
        ['Dark', 24, 600000],
        ['hiphop', 20, 500000],
        ['Hp', 35, 400000],
        ['black', 25, 300000],
        ['hat', 23, 200000]]

# open a CSV file in write mode
with open('Name_Age_Income.csv', mode='w', newline='') as file:
    # create a CSV writer object
    writer = csv.writer(file)
    # write the data to the CSV file
    writer.writerows(data)
