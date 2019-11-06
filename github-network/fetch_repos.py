#!/usr/bin/env python

import requests
import json
import itertools
import math
import tqdm
import pymongo


with pymongo.MongoClient("localhost", 27017) as client:
    db = client.get_database("github")
    users = db.get_collection("users")
    people = list(users.find(
        {"repos": {"$exists": False}}, ["login", "repos_url"]))
    print(len(people))
    params = {
        "access_token": "218e0dfd9fefce586faa1f6a4856aacd6bd7456e"
    }

    for person in tqdm.tqdm(people):
        repos = requests.get(person["repos_url"], params=params).json()
        users.update_one({"login": person["login"]}, {
                         "$set": {"repos": list(repos)}})
