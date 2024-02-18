from selenium import webdriver

from selenium.webdriver.common.by import By

def check_combinator_site():

    dr = webdriver.Chrome()
    dr.get("https://www.ycombinator.com/")
    assert dr.title == "Y Combinator" ,"title is not Y Combinator !"


def check_docker_site_title():
    dr = webdriver.Chrome()
    dr.get("https://hub.docker.com/")
    expected = "Docker Hub Container Image Library | App Containerization"
    assert dr.title == expected

check_combinator_site()
check_docker_site_title()