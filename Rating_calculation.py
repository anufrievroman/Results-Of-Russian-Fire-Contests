import pandas as pd

# Reading the database
data = pd.read_csv("Database.csv")

first_places_a  = data['1st place'].dropna().to_list()
second_places_a = data['2nd place'].dropna().to_list()
third_places_a  = data['3rd place'].dropna().to_list()
first_places_b  = data['1st place (additional)'].dropna().to_list()
second_places_b = data['2nd place (additional)'].dropna().to_list()
third_places_b  = data['3rd place (additional)'].dropna().to_list()

# Let's put all participats in the same list and ret rid of repetitions
all_participants    = first_places_a + first_places_b + second_places_a + second_places_b + third_places_a + third_places_b
unique_participants = list(set(all_participants))

# Here we count how many victories everyone got
rating = []
for name in unique_participants:
    num_of_first_places  = first_places_a.count(name) + first_places_b.count(name)
    num_of_second_places = second_places_a.count(name) + second_places_b.count(name)
    num_of_third_places  = third_places_a.count(name) + third_places_b.count(name)
    total_num_of_wins    = num_of_first_places + num_of_second_places + num_of_third_places
    score = 3*num_of_first_places + 2*num_of_second_places + 1*num_of_third_places
    rating.append([name, num_of_first_places, num_of_second_places, num_of_third_places, total_num_of_wins, score])

sorted_rating = sorted(rating, key=lambda column: float(column[5]), reverse=True)
sorted_rating = sorted(sorted_rating, key=lambda column: float(column[4]), reverse=True)

# Write the file
with open("Rating_table.csv","w+") as f:
    f.writelines(['Name,','1st place,','2nd place,','3rd place,','Total,','Score,','\n'])
    for line in sorted_rating:
        f.writelines(str(line)[1:-1]+'\n')
