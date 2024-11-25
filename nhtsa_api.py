import requests


def get_car_info(year, make, model):
    url =  f"https://api.nhtsa.gov/SafetyRatings/modelyear/{year}/make/{make}/model/{model}"
    vehicle_description = f"{year} {make} {model} "
    #car_id = ""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            car_id = data["Results"][0]["VehicleId"]
            # for i in data["Results"]:
            #     if i["VehicleDescription"] == vehicle_description:
            #         car_id = i["VehicleId"]
            return car_id
        elif:
            return f" No results found for {year} {make} {model}"

        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def get_car_ratings(car_id):
    url = f"https://api.nhtsa.gov/SafetyRatings/VehicleId/{car_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            id_data = response.json()
            overallRating = id_data["Results"][0] #["OverallRating"]
            return overallRating
        else:
            print(f"Error: {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

