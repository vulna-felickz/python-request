import requests

def get_question(token):
    url = "https://stackoverflow.com/questions/26000336"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    return response.content

def main():
    token = "YOUR_BEARER_TOKEN_HERE"
    question = get_question(token)
    print(question)

if __name__ == "__main__":
    main()
