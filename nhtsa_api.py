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
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

