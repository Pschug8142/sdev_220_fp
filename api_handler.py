import requests
import json
import string
from api_functions import create_access_token, raiderIo_request, character_access_request, item_access_request, profile_access_request,test_api_request

'''
This module utilizes the functions from api_functions.py to pull all needed information from various WoW API sources. The data in the API requests is parsed and organized into a nested dictionary structure.
'''

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
     'realm': 'none',
     #setting up a dictionary to store player gear info. As items can have or not have a wide variety of stats assigned, all key pair values are set to none and later replaced through assignment. 
     #when assignment is complete, the key values still containing none are deleted.
     'gear_dict' :
          { 
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
player_dict['gear_dict']['head']['id']         = (equipment_list[0]['item']['id'])
player_dict['gear_dict']['head']['name']       = (equipment_list[0]['name'])
player_dict['gear_dict']['neck']['id']         = (equipment_list[1]['item']['id'])
player_dict['gear_dict']['neck']['name']       = (equipment_list[1]['name'])
player_dict['gear_dict']['shoulder']['id']     = (equipment_list[2]['item']['id'])
player_dict['gear_dict']['shoulder']['name']   = (equipment_list[2]['name'])
player_dict['gear_dict']['chest']['id']        = (equipment_list[3]['item']['id'])
player_dict['gear_dict']['chest']['name']      = (equipment_list[3]['name'])
player_dict['gear_dict']['waist']['id']        = (equipment_list[4]['item']['id'])
player_dict['gear_dict']['waist']['name']      = (equipment_list[4]['name'])
player_dict['gear_dict']['legs']['id']         = (equipment_list[5]['item']['id'])
player_dict['gear_dict']['legs']['name']       = (equipment_list[5]['name'])
player_dict['gear_dict']['feet']['id']         = (equipment_list[6]['item']['id'])
player_dict['gear_dict']['feet']['name']       = (equipment_list[6]['name'])
player_dict['gear_dict']['wrist']['id']        = (equipment_list[7]['item']['id'])
player_dict['gear_dict']['wrist']['name']      = (equipment_list[7]['name'])
player_dict['gear_dict']['hand']['id']         = (equipment_list[8]['item']['id'])
player_dict['gear_dict']['hand']['name']       = (equipment_list[8]['name'])
player_dict['gear_dict']['finger']['id']       = (equipment_list[9]['item']['id'])
player_dict['gear_dict']['finger']['name']     = (equipment_list[9]['name'])
player_dict['gear_dict']['finger_2']['id']     = (equipment_list[10]['item']['id'])
player_dict['gear_dict']['finger_2']['name']   = (equipment_list[10]['name'])
player_dict['gear_dict']['trinket']['id']      = (equipment_list[11]['item']['id'])
player_dict['gear_dict']['trinket']['name']    = (equipment_list[11]['name'])
player_dict['gear_dict']['trinket_2']['id']    = (equipment_list[12]['item']['id'])
player_dict['gear_dict']['trinket_2']['name']  = (equipment_list[12]['name'])
player_dict['gear_dict']['cloak']['id']        = (equipment_list[13]['item']['id'])
player_dict['gear_dict']['cloak']['name']      = (equipment_list[13]['name'])
player_dict['gear_dict']['weapon']['id']       = (equipment_list[14]['item']['id'])
player_dict['gear_dict']['weapon']['name']     = (equipment_list[14]['name'])
player_dict['gear_dict']['shield']['id']       = (equipment_list[15]['item']['id'])
player_dict['gear_dict']['shield']['name']     = (equipment_list[15]['name'])



#This selection structure is used to assign the stat values for each key pair. 
i = 0
while i in range(len(gear_list)):
     x = 0
     attribute_main = item_access_request((player_dict['gear_dict'][gear_list[i]]['id']), access_token)['preview_item'] #assigning the bulk stats of given item [i] to attribute main
     attribute_stats = attribute_main['stats'] #assigning the core stats to attribute stats. Necessary to cut down on code bulk.
     
     if x == 0:

          if 'weapon' in attribute_main: #checking if the item is a weapon.
               #print('WEAPON FOUND')
               player_dict['gear_dict'][gear_list[i]]['attack_speed'] = attribute_main['weapon']['attack_speed']['display_string']
               player_dict['gear_dict'][gear_list[i]]['damage'] = attribute_main['weapon']['damage']['display_string']
               player_dict['gear_dict'][gear_list[i]]['dps'] = attribute_main['weapon']['dps']['display_string']

          if 'armor' in attribute_main: #checking if the item is an armor piece.
               #print('ARMOR FOUND')
               player_dict['gear_dict'][gear_list[i]]['armor'] = attribute_main['armor']['display']['display_string']

          if 'shield_block' in attribute_main: #checking if the item is offhand shield.
               #print('SHIELD FOUND')
               player_dict['gear_dict'][gear_list[i]]['block'] = attribute_main['shield_block']['display']['display_string']

     while x in range(len(attribute_stats)):

          attribute = attribute_stats[x] #x is being used to iterate through stats indices. When a stat is matched to a value below, it is considered found and its corresponding stat value is assigned
                                         #to its key pair compliment.
       
          

          if attribute['type']['name'] == 'Intellect':
               player_dict['gear_dict'][gear_list[i]]['intellect'] = attribute['display']['display_string']
          elif attribute['type']['name'] == 'Agility':
               player_dict['gear_dict'][gear_list[i]]['agility'] = attribute['display']['display_string']
          elif attribute['type']['name'] == 'Stamina':
               player_dict['gear_dict'][gear_list[i]]['stamina'] = attribute['display']['display_string']
          elif attribute['type']['name'] == 'Strength':
               player_dict['gear_dict'][gear_list[i]]['strength'] = attribute['display']['display_string']
          elif attribute['type']['name'] == 'Critical Strike':
               player_dict['gear_dict'][gear_list[i]]['crit'] = attribute['display']['display_string']
          elif attribute['type']['name'] == 'Haste':
               player_dict['gear_dict'][gear_list[i]]['haste'] = attribute['display']['display_string']
          elif attribute['type']['name'] == 'Versatility':
               player_dict['gear_dict'][gear_list[i]]['versatility'] = attribute['display']['display_string']
          elif attribute['type']['name'] == 'Mastery':
               player_dict['gear_dict'][gear_list[i]]['mastery'] = attribute['display']['display_string']



          x += 1
     i += 1

# Here, the dictionary is check for key values = 'none'. If they are found, that means the item had no corresponding values for that stat, and that they can be safely pruned from the 
# produced dictionary.    
i = 0
while i in range(len(gear_list)):
     x = 0
     while x in range(len(item_list)):
          if player_dict['gear_dict'][gear_list[i]][item_list[x]] == 'none':
               del player_dict['gear_dict'][gear_list[i]][item_list[x]]
          x += 1
     i += 1

#converting dictionary into a json format
gear_json = json.dumps(player_dict['gear_dict'], indent=4)
player_json = json.dumps(player_dict, indent=4)
#print(gear_json, '\n')
print(player_json)


#TEST CODE. CAN SAFELY BE IGNORED.
# running character_access_request() and printing off the resulting json
#print(character_access_request(access_token))
print(access_token)

#TEST CODE: CAN SAFELY BE IGNORED
#Block prints off equipment list at specified index for verification purposes.
#print(equipment_list[0])
#print("\n ///////////////////////////////////////////////////////////////// \n")
#print(equipment_list[2])
#print(type(equipment_list))
#print("\n ///////////////////////////////////////////////////////////////// \n")


