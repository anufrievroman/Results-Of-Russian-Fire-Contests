import pandas as pd

# Reading the database
data = pd.read_csv("Database.csv")

first_a  = data['1st place'].dropna().to_list()
second_a = data['2nd place'].dropna().to_list()
third_a  = data['3rd place'].dropna().to_list()
first_b  = data['1st place (additional)'].dropna().to_list()
second_b = data['2nd place (additional)'].dropna().to_list()
third_b  = data['3rd place (additional)'].dropna().to_list()

# Let's collect only unique participants
participants = list(set(first_a + first_b + second_a + second_b + third_a + third_b))

# Let's count how many victories everyone has
rating = []
for name in participants:
    num_of_first_places  = first_a.count(name) + first_b.count(name)
    num_of_second_places = second_a.count(name) + second_b.count(name)
    num_of_third_places  = third_a.count(name) + third_b.count(name)
    total_num_of_wins    = num_of_first_places + num_of_second_places + num_of_third_places
    score = 3*num_of_first_places + 2*num_of_second_places + 1*num_of_third_places
    rating.append([name, num_of_first_places, num_of_second_places, num_of_third_places, total_num_of_wins, score])

# Let's sort first by total victories and then by score
sorted_rating = sorted(rating, key=lambda column: float(column[5]), reverse=True)
sorted_rating = sorted(sorted_rating, key=lambda column: float(column[4]), reverse=True)

# Write the file
with open("Rating_table.csv","w+") as f:
    f.writelines('Name, 1st place, 2nd place, 3rd place, Total wins, Score\n')
    for line in sorted_rating:
        f.writelines(str(line)[1:-1]+'\n')
