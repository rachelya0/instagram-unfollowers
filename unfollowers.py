import json

with open('followers.json') as f:
    followers = json.load(f)

with open('following.json') as f:
    following = json.load(f)

followers_list = []
for follow in followers["relationships_followers"]:
    followers_list.append(follow["string_list_data"][0]["value"])

following_list = []
for follow in following["relationships_following"]:
    following_list.append(follow["string_list_data"][0]["value"])

unfollowers = list(set(following_list) - set(followers_list))
for user in unfollowers:
    print(user)