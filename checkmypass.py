import requests

# Initially It gives <Response [400]> , Which means unauthorized or something is not right with the api.
# url = 'https://api.pwnedpasswords.com/range/' + 'password123'
# res = requests.get(url)
# print(res)

# This api uses SHA1 Hashing so first few characters of it will give <Response [200]> which means OK.
# Using K-Anonymity works by we only give first 5 characters of our hash function
# SHA1 of password123 = CBFDAC6008F9CAB4083784CBD1874F76618D2A97
# First 5 character of password123 is CBFDA.
# url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
# res = requests.get(url)
# print(res)
