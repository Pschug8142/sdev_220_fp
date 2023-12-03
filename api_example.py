import requests
import json


#The variables client_ID and client_secret are given through the battlenet API registration. They are passed as a sort of username and password to gain an access token from the api service.
client_ID = "a1c50b73455b43fcb6cd2581635e652b"
client_secret = "4XR19xXGeWAwBQGoY1OSJG7evdCQzQY1"
#region is used to demarcate which region the servers are in
region = 'us'
#access_token in this instance is just to display how the client_ID and client_secret tokens are passed into the api.
access_token = {'access_token':'token'}

"""
create_access_token: Takes in the client ID and secret variables and sends a post request to the API. This generates an access token that allows get requests to be made. The response from server is a json package that is turned into a python dictionary.
"""
def create_access_token(client_id, client_secret, region = 'us'):
    data = { 'grant_type': 'client_credentials' }
    response = requests.post('https://%s.battle.net/oauth/token' % region, data=data, auth=(client_id, client_secret))
    return response.json()

#access token is requested. resulting python dictionary is key matched to assign the returned access token to the variable 'access_token'
access_token = create_access_token(client_ID, client_secret)
access_token = (access_token['access_token'])

#example of request being made to the API. The access token is taken as an argument and appended to the link as the argument for the access_token namespace. Further, 'korialstrasz' and 'terregoat' could be take as realm_slug and character_name arguments instead
#to allow for a user search system.
def access_request(token):
    search = "https://us.api.blizzard.com/profile/wow/character/korialstrasz/terregoat/equipment?namespace=profile-us&locale=en_US&access_token=" + token
    response = requests.get(search)
    return response.json()

#running access_request() and printing off the resulting json
print(access_request(access_token))




