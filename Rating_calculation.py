import pandas as pd

df = pd.read_csv("Database.csv")

first_places_a  = []
second_places_a = []
third_places_a  = []
first_places_b  = []
second_places_b = []
third_places_b  = []
for i in range(df.shape[0]):
    first_places_a.append(str(df.iloc[i][2]))
    second_places_a.append(str(df.iloc[i][3]))
    third_places_a.append(str(df.iloc[i][4]))
    first_places_b.append(str(df.iloc[i][5]))
    second_places_b.append(str(df.iloc[i][6]))
    third_places_b.append(str(df.iloc[i][7]))

# Let's put all participats in the same list and ret rid of repetitions
all_participants    = first_places_a + first_places_b + second_places_a + second_places_b + third_places_a + third_places_b
unique_participants = list(set(all_participants))
unique_participants = [x for x in unique_participants if x != 'nan']

rating = [0]*len(unique_participants)

# Here we count how many victories everyone got
for i in range(len(unique_participants)):
    num_of_first_places  = first_places_a.count(unique_participants[i])+first_places_b.count(unique_participants[i])
    num_of_second_places = second_places_a.count(unique_participants[i])+second_places_b.count(unique_participants[i])
    num_of_third_places  = third_places_a.count(unique_participants[i])+third_places_b.count(unique_participants[i])
    total_num_of_wins    = num_of_first_places + num_of_second_places + num_of_third_places

    # So we give 3 points for the 1st place, 2 for second and 3 for third_places
    score = 3*num_of_first_places + 2*num_of_second_places + 1*num_of_third_places
    rating[i] = [unique_participants[i], num_of_first_places, num_of_second_places, num_of_third_places, total_num_of_wins, score]

sorted_rating = sorted(rating, key=lambda column: float(column[4]), reverse=True)
sorted_rating = sorted(sorted_rating, key=lambda column: float(column[5]), reverse=True)

# Write the file
with open("Rating_table.csv","w+") as f:
    f.writelines(['Name,','1st place,','2nd place,','3rd place,','Total,','Score,','\n'])
    for i in range(len(unique_participants)):
        f.writelines(['%s,' % sorted_rating[i][0],
            '%s,' % sorted_rating[i][1],
            '%s,' % sorted_rating[i][2],
            '%s,' % sorted_rating[i][3],
            '%s,' % sorted_rating[i][4],
            '%s,' % sorted_rating[i][5],'\n'])
