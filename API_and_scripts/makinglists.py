import requests
import json

response = requests.get('https://developers.zomato.com/api/v2.1/search?entity_id=286&entity_type=city',
                        params={"start": 20},

                        headers={'user-key': '14f8b3cfa9aab42131b3602f14c659f4'})

rest = []

# print(response.json()['restaurants'][0]['restaurant']) #returns the name of the first restaurant

for x in response.json()['restaurants']:
    rest.append({"name": x['restaurant']['name'],
                 "url": x['restaurant']['url'],
                 "location": x['restaurant']['location']['address'],
                 "hours": x['restaurant']['timings'],
                 "cuisine":x['restaurant']['cuisines']})

print((rest))


# with open("categories.JSON") as f:
#     data = json.load(f)

# # print(data["cuisines"])
# for flavor in data["categories"]:
#     cuisine_list.append(flavor['categories']['name'])

# print(cuisine_list)
