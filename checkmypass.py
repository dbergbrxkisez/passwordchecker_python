import requests
import hashlib  # This Built in module can do SHA1 Hashing.

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


# This function will go and request our data and give us response.
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    # IT'll check if the status code is not ok and raise an error.
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again.')

# Gives Runtime error because the given value is not hashed. Api only responds if the value is hashed.
# request_api_data('123')

# with the response given by request_api_data(). We wanna check our original password. i.e = password123


def pwned_api_check(password):
    # check password if it exists in API response
    # First hash the password here.
    # if we just do ```print(password.encode('utf-8'))``` .       It's encoded in utf-8 as b'123'
    # print(password.encode('utf-8'))
    # if we add ```hashlib.sha1(password.encode('utf-8'))``` .    We get <sha1 HASH object @ 0x1067ff9e0>
    # print(hashlib.sha1(password.encode('utf-8')))
    # if we add .hexdigit() to the ```hashlib.sha1(password.encode('utf-8'))``` .   We can convert the object to Hexadecimal.
    # print(hashlib.sha1(password.encode('utf-8')).hexdigest())
    # if we need to agree with the api then we need to do convert this hexadecimal value to uppercase by using .upper()
    # we get the complete SHA1 encoded Hash of the given password string.
    # print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1password


print(pwned_api_check('123'))
