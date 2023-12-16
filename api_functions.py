import requests
import json
import string

'''
Functions for making API requests. The general format of these functions can be copied to utilize any Blizzard API call so long as the correct API URL is placed in as the 'search' variable. Generally, 
any <404> response will result from some part of the URL assembly being incorrect, so thats the first place to check. 

The only function that you should not attempt to modify for a new purpose is create_access_request. This function is necessary for all other Blizzard API based functions to work.

For any function that uses 'token' as an argument, the below variables client_ID and client_secret must be passed into the function create_access_token, from which the return must be parsed for the
access_token string to be used as the 'token' argument where needed. Blizzard api can handle 36,000 requests per hour at a rate of 100/sec from this unique access token, exceeding which requests can
still be made but will be subject to throttling. While the token argument could be eliminated entirely by including the create_access_token functionality within every function requiring the argument
it would double the amount of api calls being made and generally slow things down even more.

No limitations were specified under raiderIO api documentation, but it can be assumed the limits are similar if any of their info is being handled
through blizzard api.

client_ID = "a1c50b73455b43fcb6cd2581635e652b"
client_secret = "4XR19xXGeWAwBQGoY1OSJG7evdCQzQY1"
'''
def raiderIo_request(toon_name,toon_realm):
     #raiderIo_request: Retrieve's metadata surrounding a character. This API is preferable due to the ease of obtaining data from this sources over several different Blizzard APIs.
     search = 'https://raider.io/api/v1/characters/profile?region=us&realm=' + toon_realm + '&name=' + toon_name + '&fields=raid_progression'
     response = requests.get(search)
     print('RaiderIO response: ',response)
     return response.json()

def create_access_token(client_id, client_secret, region = 'us'):
     # create_access_token: Takes in the client ID and secret variables and sends a post request to the API. This generates an access token that allows get requests to be made.
     # The response from server is a json package that is turned into a python dictionary. To use the access token moving forward, it must be parsed from the response. An example is shown below.
     #
     #access_token = create_access_token(client_ID, client_secret)
     #access_token = access_token['access_token']

    data = { 'grant_type': 'client_credentials' }
    response = requests.post('https://%s.battle.net/oauth/token' % region, data=data, auth=(client_id, client_secret))
    print('Creating access token:',response)
    return response.json()

def character_access_request(toon_name,toon_realm,token):
     # character_access_request: The access token, character name, and character realm are taken as arguments and inserted into the link to form the specific character lookup query. The response is a dictionary
     # containing the full equipment layout of the searched character.
    search = "https://us.api.blizzard.com/profile/wow/character/" + toon_realm + "/" + toon_name + "/equipment?namespace=profile-us&locale=en_US&access_token=" + token
    response = requests.get(search)
    print('Asking Blizzard API for character equipment information:',response)
    return response.json()

def item_access_request(id,token):
     # item_access_request: Takes the id of an item and the access token as arguments. Looks up and returns the given items information from Blizzard API. 
     # Item ID's are being gathered within character_access_request function if you wish to use a bulk assignment for a character. For a specific item, the item ID can be found online and passed in
     # as an argument.

    search = 'https://us.api.blizzard.com/data/wow/item/' + str(id) + '?namespace=static-us&locale=en_US&access_token=' + token
    response = requests.get(search)
    print('Asking blizzard API for information on item', id, ':', response)
    return response.json()

def profile_access_request(toon_name,toon_realm,token):
     #profile_access_request: The only purpose of this request is to scrape the player's level.
     search = 'https://us.api.blizzard.com/profile/wow/character/' + toon_realm +'/' + toon_name + '?namespace=profile-us&locale=en_US&access_token=' + token
     response = requests.get(search)
     print('Asking Blizzard API for profile information:', response)
     return response.json()


def test_api_request(token):
     #test_api_request: This function exists solely to pull a character level from a profile request for response testing purposes. To see the full request instead of the level, 
     # edit the third line in this function to remove ['level']. As a warning, the full request will be hundreds of lines of blizzard API response. Additionally, if another key is desired for testing, simply
     # change 'level' to the desired key.
     search = 'https://us.api.blizzard.com/profile/wow/character/korialstrasz/terregoat?namespace=profile-us&locale=en_US&access_token=' + token
     response = requests.get(search)
     response = response.json()['level']
     print('Asking Blizzard API for profile information:', response)
     return response
