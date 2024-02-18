import requests
import random


def github_api_check_repo():
    github_api_url = "https://api.github.com/users/avielb/repos"
    response = requests.get(github_api_url)
    print(response.status_code)

    repositories = response.json()
    num_of_repos = len(repositories)
    print(f"number of repositories : {num_of_repos}")
    assert num_of_repos >= 5, "does not have enough repositories"


def check_agify():
    names = []
    for _ in range(3):
        random_name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3))
        names.append(random_name)

    for name in names:
        api_url = f"https://api.agify.io/?name={name}"

        try:
            response = requests.get(api_url)

            age_data = response.json()
            age = age_data.get('age', None)

            if age is not None:
                assert 0 <= age <= 120
                print(f"{name} age is : {age}")

        except requests.exceptions.RequestException as e:
            print(f"Error for {name}: {e}")


def check_israel_universities():
    api_url = "http://universities.hipolabs.com/search?country=Israel"

    try:
        response = requests.get(api_url)

        universities_data = response.json()
        universities_count = len(universities_data)

        assert universities_count >= 5 ,"There are less than 5 universities in Israel."

        if universities_count >= 5:
            print(f"There are at least 5 universities in Israel.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


github_api_check_repo()

check_agify()

check_israel_universities()

