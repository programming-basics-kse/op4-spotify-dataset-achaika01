import csv
import ast
from csv import excel


def is_valid(num:str)->bool:
    try:
        num = float(num)
        if -1 <= num <= 1:
            return True
        return False
    except ValueError:
        return False

# with open('top_50_2023.csv', 'r') as cvsfile:
#     header = next(cvsfile)
#     print(header)
#     data = []
#     for line in cvsfile:
#         line = line[:-1].split(',')
#         data.append(line)
#
# print(data[0])

with open('top_50_2023.csv', 'r') as cvsfile:
    cvs_reader = csv.reader(cvsfile, delimiter=',')
    header = next(cvsfile)
    rows = []
    for row in cvs_reader:
        rows.append(row)
# print(row[0])
GENRE = 4
YEARS = 3
DANCEABILITY = 5
EXPLICIT = 2
LIVELINESS = 11
ENERGY = 7
ARTIST = 0
#GENRE = header.index('genres')
for row in rows:
    row[GENRE] = ast.literal_eval(row[GENRE])
    row[YEARS] = row[YEARS][:4]
#YEARS = header.index('album_release_date')
# for row in rows:
#     row[YEARS] = ast.literal_eval(row[YEARS])

# DANCEABILITY = header.index('danceability')
sum_dance = 0
counter = 0
for row in rows:
    if is_valid(row[DANCEABILITY]):
        counter += 1
        sum_dance += float(row[DANCEABILITY])
print('average', sum_dance/counter)

is_explicit_count = 0
for row in rows:
    if row[EXPLICIT] == 'True':
        is_explicit_count += 1
print('explicit', is_explicit_count)

#top 3 genres
genres_count = {}
for row in rows:
    for genre in row[GENRE]:
        if genre in genres_count:
            genres_count[genre] += 1
        else:
            genres_count[genre] = 1
top_3 = sorted(genres_count.items(),key=lambda x: x[1], reverse=True)[:3]
print('top 3', top_3)

#the most popular year
years_count = {}
for row in rows:
    year = row[YEARS][:4]
    if year in years_count:
        years_count[year] += 1
    else:
        years_count[year] = 1
print(years_count)
most_popular_year = max(years_count, key=years_count.get)
print(f"Most popular year:", most_popular_year, "with", years_count[most_popular_year], "albums.")

#Average Liveliness with Energy Criteria
sum_liveliness = 0
count = 0
for row in rows:
    try:
        energy = float(row[ENERGY])
        liveliness = float(row[LIVELINESS])
        if energy > 0.5:
            sum_liveliness += liveliness
            count += 1
    except ValueError:
        continue
average_liveliness = sum_liveliness / count
print('average liveliness', average_liveliness)

#The most popular artist
artists = {}
for row in rows:
    artist = row[ARTIST].strip()
    if artist in artists:
        artists[artist] += 1
    else:
        artists[artist] = 1
most_popular_artist = max(artists, key=artists.get)
print(f"Most popular artist:", most_popular_artist)