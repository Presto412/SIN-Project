import twitter
from pprint import pprint
api = twitter.Api(consumer_key='JBGrjqJSDZcuQwySRPecvAVgF',
                  consumer_secret='3RgFUTBTrjPgxSHkXFwNvryFmuu61tCHxh3hy78pnxFHXBHBcG',
                  access_token_key='1139771994809888768-FBzFs5kiPT4YeVsGFeP5yUIJKZEU9i',
                  access_token_secret='hW46XofTV4Z7L8D6nX7D1cxN1kdeLrqRaHY7wRmysqTWt', sleep_on_rate_limit=True)
# pprint(api.VerifyCredentials())
users = api.GetFollowers(screen_name="sachin_rt", total_count=200)
with open("response.csv", "w") as f:
    f.write(''.join(str(u.name) + "," + str(u.friends_count) +
                    ","+str(u.followers_count) + "\n" for u in users))
