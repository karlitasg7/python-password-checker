import requests

url = 'https://api.pwnedpasswords.com/range/'

if __name__ == '__main__':
    res = requests.get(url)
    print(res)
