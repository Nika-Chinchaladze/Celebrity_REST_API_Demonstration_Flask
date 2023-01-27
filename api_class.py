import requests
from random import choice


class CelebrityApi:
    def __init__(self):
        self.my_api = "http://peackyblinder.pythonanywhere.com/"
        self.my_key = "TommyShelby"

    def get_all(self):
        respond = requests.get(url=f"{self.my_api}all")
        data = respond.json()["celebrity_data"]
        return data

    def get_random(self):
        data = choice(self.get_all())
        return data

    def get_search(self, category, defined_value, operator):
        # define api endpoint:
        endpoint = ""
        if category == "first_name":
            endpoint = f"{self.my_api}search/first_name?celebrity_name={defined_value.capitalize()}"
        elif category == "last_name":
            endpoint = f"{self.my_api}search/last_name?celebrity_surname={defined_value.capitalize()}"
        elif category == "gender":
            endpoint = f"{self.my_api}search/gender?celebrity_gender={defined_value.capitalize()}"
        elif category == "movie_genre":
            endpoint = f"{self.my_api}search/movie_genre?celebrity_genre={defined_value.capitalize()}"
        elif category == "age":
            endpoint = f"{self.my_api}search/age?celebrity_age={defined_value}&operator={operator}"
        elif category == "followers":
            endpoint = f"{self.my_api}search/followers?celebrity_followers={defined_value}&operator={operator}"
        # Retrieve Data:
        respond = requests.get(url=endpoint)
        data = respond.json()["data"]
        return data

    def add_celebrity(self, first_name, last_name, gender, age, movie_genre, followers, img_url):
        new_celebrity = {
            "first_name": first_name.capitalize(),
            "last_name": last_name.capitalize(),
            "gender": gender.capitalize(),
            "age": int(age),
            "movie_genre": movie_genre.capitalize(),
            "followers": int(followers),
            "img_url": img_url
        }
        respond = requests.post(url=f"{self.my_api}add", json=new_celebrity)
        answer = respond.status_code
        return answer

    def update_celebrity(self, celebrity_id, category, defined_value):
        endpoint = f"{self.my_api}update/{celebrity_id}/{category}?{category}={defined_value}&api_key={self.my_key}"
        respond = requests.patch(url=endpoint)
        answer = respond.status_code
        return answer

    def change_celebrity(self, celebrity_id, first_name, last_name, gender, age, movie_genre, followers, img_url):
        respond = requests.put(
            url=f"{self.my_api}change/{celebrity_id}?first_name={first_name}&last_name={last_name}&gender={gender}&"
                f"age={age}&movie_genre={movie_genre}&followers={followers}&img_url={img_url}&api_key={self.my_key}"
        )
        answer = respond.status_code
        return answer

    def delete_celebrity(self, celebrity_id):
        respond = requests.delete(url=f"{self.my_api}delete/{celebrity_id}?api_key={self.my_key}")
        answer = respond.status_code
        return answer
