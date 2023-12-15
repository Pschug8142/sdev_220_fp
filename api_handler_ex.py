'''
READ ME:

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

THIS COPY OF API HANDLER EXISTS ONLY AS FUNCTIONAL REFERENCE POINT, AND SHOULD NOT BE USED OUTSIDE OF THAT PURPOSE.

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

import requests
import json
import string

#setting up dictionary to handle player metadata
player_dict = {
     'name': 'none',
     'level': 'none',
     'race': 'none',
     'class': 'none',
     'active_spec_name': 'none',
     'active_spec_role': 'none',
     'gender': 'none',
     'faction': 'none',
     'achievement_points': 'none',
     'realm': 'none'
}

#setting up a dictionary to store player gear info. As items can have or not have a wide variety of stats assigned, all key pair values are set to none and later replaced through assignment. 
#when assignment is complete, the key values still containing none are deleted.
gear_dict = {
     'head' : {
          'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'
     },
     'neck' : {
          'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'
     },
     'shoulder' : {
          'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'
     },
     'chest' : {
          'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'
     },
     'waist' : {
          'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'   
     },
     'legs' : {
          'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'     
     },
     'feet' : {
          'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'     
     },
     'wrist' : {
          'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'       
     },
     'hand' :{
           'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'              
     }, 
     'finger': {
          'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'     
     }, 
     'finger_2' :{
          'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'    
     },
     'trinket' : {
          'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'      
     },
     'trinket_2' : {
          'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'     
     },
     'cloak' : {
          'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'
     },
     'weapon' : {
          'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'     
     },
     'shield' : {
          'name': 'none',
          'id': 'none',
          'stamina': 'none',
          'strength': 'none',
          'agility': 'none',
          'intellect': 'none',
          'crit': 'none',
          'haste': 'none',
          'mastery': 'none',
          'versatility': 'none',
          'damage': 'none',
          'dps': 'none',
          'attack_speed': 'none',
          'armor': 'none',
          'block': 'none'    
     }
}


#the below lists are used as index equivalents to the dictionaries.
gear_list = ('head','neck','shoulder','chest','waist','legs','feet','wrist','hand','finger','finger_2','trinket','trinket_2','cloak','weapon','shield')
item_list = ('intellect','stamina','strength','agility','crit','haste','mastery','versatility','damage','dps','attack_speed','armor','block')

# The variables client_ID and client_secret are given through the battlenet API registration. They are passed as a sort of username and password to gain an access token from the api service.
client_ID = "a1c50b73455b43fcb6cd2581635e652b"
client_secret = "4XR19xXGeWAwBQGoY1OSJG7evdCQzQY1"

#code variables that wont make it into production.
test_char = 'terregoat'
test_realm = 'korialstrasz'
toon_name = test_char
toon_realm = test_realm


def raiderIo_request(toon_name,toon_realm):
     #raiderIo_request: Retrieve's metadata surrounding a character
     search = 'https://raider.io/api/v1/characters/profile?region=us&realm=' + toon_realm + '&name=' + toon_name + '&fields=raid_progression'
     response = requests.get(search)
     print('RaiderIO response: ',response)
     return response.json()

def create_access_token(client_id, client_secret, region = 'us'):
     # create_access_token: Takes in the client ID and secret variables and sends a post request to the API. This generates an access token that allows get requests to be made.
     # The response from server is a json package that is turned into a python dictionary.
    data = { 'grant_type': 'client_credentials' }
    response = requests.post('https://%s.battle.net/oauth/token' % region, data=data, auth=(client_id, client_secret))
    print('Creating access token:',response)
    return response.json()

def character_access_request(toon_name,toon_realm,token):
     # character_access_request: The access token, character name, and character realm are taken as arguments and inserted into the link to form the specific character lookup query. 
    search = "https://us.api.blizzard.com/profile/wow/character/" + toon_realm + "/" + toon_name + "/equipment?namespace=profile-us&locale=en_US&access_token=" + token
    response = requests.get(search)
    print('Asking Blizzard API for character equipment information:',response)
    return response.json()

def item_access_request(id,token):
     # item_access_request: Takes the id of an item and the access token as arguments. Lookups up and returns the given items information from Blizzard API. Item ID's can be found from character_access_requeste response

    search = 'https://us.api.blizzard.com/data/wow/item/' + str(id) + '?namespace=static-us&locale=en_US&access_token=' + token
    response = requests.get(search)
    print('Asking blizzard API for information on item', id, ':', response)
    return response.json()

def profile_access_request(toon_name,toon_realm,token):
     search = 'https://us.api.blizzard.com/profile/wow/character/' + toon_realm +'/' + toon_name + '?namespace=profile-us&locale=en_US&access_token=' + token
     response = requests.get(search)
     print('Asking Blizzard API for profile information:', response)
     return response.json()

# 'access token' is requested. resulting python dictionary is key matched to assign the returned access token to the variable 'access_token'
access_token = create_access_token(client_ID, client_secret)
access_token = access_token['access_token']

#retrieving player metadata from radierIo and assigning it to player_dict
player_data = raiderIo_request(toon_name,toon_realm)
player_data_level = profile_access_request(toon_name,toon_realm,access_token)
player_dict['level'] = player_data_level['level']
player_dict['name'] = player_data['name']
player_dict['race'] = player_data['race']
player_dict['class'] = player_data['class']
player_dict['active_spec_name'] = player_data['active_spec_name']
player_dict['active_spec_role'] = player_data['active_spec_role']
player_dict['gender'] = player_data['gender']
player_dict['faction'] = player_data['faction']
player_dict['achievement_points'] = player_data['achievement_points']
player_dict['realm'] = player_data['realm']


#Setting the variable 'equipment_list' to be equal to the returned json( which has been converted to dict) from the blizzard api.
equipment_list = character_access_request(toon_name,toon_realm,access_token)

# There is data present that isn't required from the api request. Here, we're getting rid of it by setting the 'equipment_list' variable equal to the desired
# block we need from the api GET.
equipment_list = equipment_list['equipped_items']

#This block is pulling the name and ID of the player's equipped items out of 'equipment_list' and assigning these values to their respective key pairs.
gear_dict['head']['id']         = (equipment_list[0]['item']['id'])
gear_dict['head']['name']       = (equipment_list[0]['name'])
gear_dict['neck']['id']         = (equipment_list[1]['item']['id'])
gear_dict['neck']['name']       = (equipment_list[1]['name'])
gear_dict['shoulder']['id']     = (equipment_list[2]['item']['id'])
gear_dict['shoulder']['name']   = (equipment_list[2]['name'])
gear_dict['chest']['id']        = (equipment_list[3]['item']['id'])
gear_dict['chest']['name']      = (equipment_list[3]['name'])
gear_dict['waist']['id']        = (equipment_list[4]['item']['id'])
gear_dict['waist']['name']      = (equipment_list[4]['name'])
gear_dict['legs']['id']         = (equipment_list[5]['item']['id'])
gear_dict['legs']['name']       = (equipment_list[5]['name'])
gear_dict['feet']['id']         = (equipment_list[6]['item']['id'])
gear_dict['feet']['name']       = (equipment_list[6]['name'])
gear_dict['wrist']['id']        = (equipment_list[7]['item']['id'])
gear_dict['wrist']['name']      = (equipment_list[7]['name'])
gear_dict['hand']['id']         = (equipment_list[8]['item']['id'])
gear_dict['hand']['name']       = (equipment_list[8]['name'])
gear_dict['finger']['id']       = (equipment_list[9]['item']['id'])
gear_dict['finger']['name']     = (equipment_list[9]['name'])
gear_dict['finger_2']['id']     = (equipment_list[10]['item']['id'])
gear_dict['finger_2']['name']   = (equipment_list[10]['name'])
gear_dict['trinket']['id']      = (equipment_list[11]['item']['id'])
gear_dict['trinket']['name']    = (equipment_list[11]['name'])
gear_dict['trinket_2']['id']    = (equipment_list[12]['item']['id'])
gear_dict['trinket_2']['name']  = (equipment_list[12]['name'])
gear_dict['cloak']['id']        = (equipment_list[13]['item']['id'])
gear_dict['cloak']['name']      = (equipment_list[13]['name'])
gear_dict['weapon']['id']       = (equipment_list[14]['item']['id'])
gear_dict['weapon']['name']     = (equipment_list[14]['name'])
gear_dict['shield']['id']       = (equipment_list[15]['item']['id'])
gear_dict['shield']['name']     = (equipment_list[15]['name'])



#This selection structure is used to assign the stat values for each key pair. 
i = 0
while i in range(len(gear_list)):
     x = 0
     attribute_main = item_access_request((gear_dict[gear_list[i]]['id']), access_token)['preview_item'] #assigning the bulk stats of given item [i] to attribute main
     attribute_stats = attribute_main['stats'] #assigning the core stats to attribute stats. Necessary to cut down on code bulk.
     
     if x == 0:

          if 'weapon' in attribute_main: #checking if the item is a weapon.
               #print('WEAPON FOUND')
               gear_dict[gear_list[i]]['attack_speed'] = attribute_main['weapon']['attack_speed']['display_string']
               gear_dict[gear_list[i]]['damage'] = attribute_main['weapon']['damage']['display_string']
               gear_dict[gear_list[i]]['dps'] = attribute_main['weapon']['dps']['display_string']

          if 'armor' in attribute_main: #checking if the item is an armor piece.
               #print('ARMOR FOUND')
               gear_dict[gear_list[i]]['armor'] = attribute_main['armor']['display']['display_string']

          if 'shield_block' in attribute_main: #checking if the item is offhand shield.
               #print('SHIELD FOUND')
               gear_dict[gear_list[i]]['block'] = attribute_main['shield_block']['display']['display_string']

     while x in range(len(attribute_stats)):

          attribute = attribute_stats[x] #x is being used to iterate through stats indices. When a stat is matched to a value below, it is considered found and its corresponding stat value is assigned
                                         #to its key pair compliment.
       
          

          if attribute['type']['name'] == 'Intellect':
               gear_dict[gear_list[i]]['intellect'] = attribute['display']['display_string']
          elif attribute['type']['name'] == 'Agility':
               gear_dict[gear_list[i]]['agility'] = attribute['display']['display_string']
          elif attribute['type']['name'] == 'Stamina':
               gear_dict[gear_list[i]]['stamina'] = attribute['display']['display_string']
          elif attribute['type']['name'] == 'Strength':
               gear_dict[gear_list[i]]['strength'] = attribute['display']['display_string']
          elif attribute['type']['name'] == 'Critical Strike':
               gear_dict[gear_list[i]]['crit'] = attribute['display']['display_string']
          elif attribute['type']['name'] == 'Haste':
               gear_dict[gear_list[i]]['haste'] = attribute['display']['display_string']
          elif attribute['type']['name'] == 'Versatility':
               gear_dict[gear_list[i]]['versatility'] = attribute['display']['display_string']
          elif attribute['type']['name'] == 'Mastery':
               gear_dict[gear_list[i]]['mastery'] = attribute['display']['display_string']



          x += 1
     i += 1

# Here, the dictionary is check for key values = 'none'. If they are found, that means the item had no corresponding values for that stat, and that they can be safely pruned from the 
# produced dictionary.    
i = 0
while i in range(len(gear_list)):
     x = 0
     while x in range(len(item_list)):
          if gear_dict[gear_list[i]][item_list[x]] == 'none':
               del gear_dict[gear_list[i]][item_list[x]]
          x += 1
     i += 1

#converting dictionary into a json format
gear_json = json.dumps(gear_dict, indent=4)
player_json = json.dumps(player_dict, indent=4)
print(gear_json, '\n')
print(player_json)


#TEST CODE. CAN SAFELY BE IGNORED.
# running character_access_request() and printing off the resulting json
#print(character_access_request(access_token))
#print(access_token)

#TEST CODE: CAN SAFELY BE IGNORED
#Block prints off equipment list at specified index for verification purposes.
#print(equipment_list[0])
#print("\n ///////////////////////////////////////////////////////////////// \n")
#print(equipment_list[2])
#print(type(equipment_list))
#print("\n ///////////////////////////////////////////////////////////////// \n")
'''

