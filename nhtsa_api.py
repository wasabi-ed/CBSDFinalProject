import requests


def get_car_info(year, make, model):
    url =  f"https://api.nhtsa.gov/SafetyRatings/modelyear/{year}/make/{make}/model/{model}"
    vehicle_description = f"{year} {make} {model} "
    # car_id = ""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["Count"] == 0:
                return True
            car_id = data["Results"][0]["VehicleId"]
            return car_id
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
            overallRating = id_data["Results"][0]
            return overallRating
        else:
            print(f"Error: {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

