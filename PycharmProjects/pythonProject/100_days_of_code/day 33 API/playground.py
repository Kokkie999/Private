import requests
# from datetime import datetime
#
# MY_LAT = 52.167137
# MY_LONG = 4.634807
#
# # ISS_LOCATION
# # response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # response.raise_for_status()
# #
# # data = response.json()
# #
# # longitude = data["iss_position"]["longitude"]
# # latitude = data["iss_position"]["latitude"]
# #
# # iss_position = (longitude, latitude)
# #
# # print(iss_position)
#
# # SUNSET & SUNRISE
# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0,
# }
#
# response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
#
# time_now = datetime.now()
#
# print(sunrise)
# print(sunset)
# print(time_now.hour)

parameters = {
    "where": "1=1",
    #"outFields": "sgisid,vopcode",
    #"returnCentroid": "true",
    "f": "json",
    "token": "vYNaREh6jNSfkvY819tskCS4Rnhf6a0Qnev6S3d0rs2QsLQisuqFDA1QEl32l8qaTdeeA4Uo9UFlRIr1xn_x-O1nkqC7vGYIOrnq6VlFcX7HP-yOW1Eu47IrVWyKLQ1OkV0R0wcHSwd27IxI937tlwtxQj6o97-BJUIEO6Qqnt8oY95iyse6YrNeoRkX-40y1KeAG-TUnIZrs7Um0v3squY0Yw1FVZEpkwGK7EYylT84aRV4booLlSusZak1qZoa",
}

response = requests.get(url="https://arcgis.schiphol.nl/arcgishosted/rest/services/Hosted/Vliegtuig_Opstel_Plaats_%28VOP%29/FeatureServer/0/query", params=parameters)
response.raise_for_status()

data = response.json()

print(data)

