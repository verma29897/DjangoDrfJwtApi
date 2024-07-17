import requests

def token_generate():

    token_url = "http://127.0.0.1:8000/api/token/"
    login_data = {
    "username": "verma123",
    "password": "Krishna@97"
    }

    response = requests.post(token_url, data=login_data)
    print(response.json())
    if response.status_code == 200:
        tokens = response.json()
        print(f"Access Token: {tokens['access']}")
        return tokens['access']
def get_method(access_token):

    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    posts_url = "http://127.0.0.1:8000/api/posts/"
    response = requests.get(posts_url, headers=headers)
    print(response.json())
    if response.status_code == 200:
        posts = response.json()
        print("Posts:", posts)
    return response.json()["id"]
def post_method(access_token):
    posts_url = "http://127.0.0.1:8000/api/posts/"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    new_post_data = {
        "title": "New Post Title",
        "content": "This is the content of the new post.",
    }

    response = requests.post(posts_url, headers=headers, data=new_post_data)

    if response.status_code == 201:
        new_post = response.json()
        print(new_post)

def put_method(access_token,id):
    posts_url = f"http://127.0.0.1:8000/api/posts/{id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    new_post_data = {
        "title": "New Post Title",
        "content": "This is the content of the new post.",
    }

    response = requests.post(posts_url, headers=headers, data=new_post_data)

    if response.status_code == 201:
        new_post = response.json()
        print(new_post)
def delete_method(access_token,id):
    posts_url = f"http://127.0.0.1:8000/api/posts/{id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.delete(posts_url, headers=headers)
    print(response.json())

    

def main():
    access_token = token_generate()
    print(access_token)
    post_method(access_token)
    id=get_method(access_token)
    put_method(access_token,id)
    delete_method(access_token,id)

if __name__ == "__main__":
    main()
