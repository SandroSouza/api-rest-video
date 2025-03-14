import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"likes": 55, "name": "tutorial php", "views": 5000000},
#         {"likes": 14500, "name": "como fazer uma api rest", "views": 6000000},
#         {"likes": 850, "name": "javascripts para iniciantes", "views": 7000000}]


# for i in range(len(data)):
#     response = requests.put(BASE + "videos/" + str(i), data[i])
#     print(response.json)


# response = requests.delete(BASE + "videos/2")
# print(response.json())

response = requests.get(BASE + "videos/1")
print(response.json())