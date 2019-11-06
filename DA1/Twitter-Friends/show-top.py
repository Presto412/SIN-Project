import csv
from pprint import pprint
followers = []
with open("response.csv", "r") as f:
    followers = [i.strip().split(",") for i in f.readlines()][1:]

cleaned_followers = []
for i in followers:
    score = int(i[1]) + int(i[2])
    name = i[0]
    cleaned_followers.append((name, score))
top_100_followers = sorted(
    (cleaned_followers), key=lambda tup: tup[1], reverse=True)[:100]
print(''.join(f[0] + "," + str(f[1]) + "\n" for f in top_100_followers))
