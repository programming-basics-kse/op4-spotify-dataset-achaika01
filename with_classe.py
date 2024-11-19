import csv

class Song:
    def __init__(self, title, artist, years, dancebility, is_explicit):
        self.title = title
        self.artist = artist
        self.year = years
        self.dancebility = float(dancebility)
        self.is_explicit = is_explicit

    def __str__(self):
        return f"{self.title} - {self.artist} - {self.year}"

class Analyzer:
    def __init__(self, song_list):
        self.song_list = song_list

    def average_dancebility(self):
        dancebility = 0
        for song in self.song_list:
            dancebility += float(song.dancebility)
        return dancebility / len(self.song_list)

songs = []
with open('top_50_2023.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        songs.append(Song(row[1], row[0], row[3], row[5], row[2]))

for song in songs:
    print(song.title)



analyzer = Analyzer(songs)
print(analyzer.average_dancebility())