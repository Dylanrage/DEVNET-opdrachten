#!/usr/bin/env python
# coding: utf-8

# In[66]:


#### Google Geocoding API
#### Y. Rooseleer, BiASC
#### => API Calls, Request/Response, Authentication, Data Management/Filtering/Selecting/Transforming
import requests
import json
import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Imported libraries for the script')
print('STARTING Google Geocoding API Example Script')
print('=> API Calls, Request/Response, Authentication, Data Management/Filtering/Selecting/Transforming')
#dir(urllib)
#dir(requests)


# In[67]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Getting input')
#####
address = input("Town or City? ")
                


# In[71]:


import requests
import datetime
import json
print ("Current date and time: ")
print(datetime.datetime.now())
api_scheme = "https://"
api_authority = "maps.googleapis.com"
api_path = "/maps/api/geocode/json"
main_api = api_scheme + api_authority + api_path
#main_api = "https://maps.googleapis.com/maps/api/geocode/json"
api_key = "A123456789--USEYOUROWNKEY"
api_query = "?"+"key"+"="+api_key+"&"+"address"+"="+address
uri = main_api + api_query
# uri = main_api+"?"+"key"+"="+api_key+"&"+"address"+"="+address
print('Creating full request')
print(uri)
resp  = requests.get(uri)
print("------1--------")
print(type(resp))
#print(dir(resp))
#print(dir(requests.adapters))
#print(resp.__dict__)
print("------2--------")
print(resp.status_code)
print("------3--------")
print(resp.text)
print("------4--------")
json_data = resp.json()
print(type(json_data))
print("------5--------")
print(json_data)
#print("------6--------")
#str_doc = json.dumps(json_data, indent=4)
#print(str_doc)


# In[19]:


import datetime
print ("Current date and time: ")
print(datetime.datetime.now())
print('Success of the request')
print("STATUS")
print('------1--------')
print(resp.status_code)
print('------2-------')
json_status = json_data["status"]
#print("API Status: " + json_status)
print(json_status)
print('------3-------')
alternative = resp.json()["status"]
print(alternative)


# In[28]:


print ("Current date and time: ")
print(datetime.datetime.now())
print('Raw result of the request')
if resp.status_code == 200:
    print("RAW RESULT IN JSON - STATUS CODE")
    print(resp.status_code)
if json_status == "OK":
    print("RAW RESULT IN JSON - STATUS TEXT")
    print( json_status )
    print('--------------')
    print(json_data)
    print('--------------')


# In[74]:


##### => PRINT ALL KEYS (TREE STRUCTURE)
##### NOT FINISHED 
print ("Current date and time: ")
print(datetime.datetime.now())
print('Keys in the response')
    
#! /usr/bin/python

def print_dict(dictionary, ident = '', braces=1):
    """ Recursively prints nested dictionaries."""

    for key, value in dictionary.iteritems():
        if isinstance(value, dict):
            #print('%s%s%s%s' %(ident,braces*'[',key,braces*']'))
            print_dict(value, ident+'  ', braces+1)
        else:
            print(ident+'%s = %s' %(key, value))

#if __name__ == '__main__':

example_dict = { 'key1' : 'value1',
                 'key2' : 'value2',
                 'key3' : { 'key3a': 'value3a' },
                 'key4' : { 'key4a': { 'key4aa': 'value4aa',
                                       'key4ab': 'value4ab',
                                       'key4ac': 'value4ac'},
                             'key4b': 'value4b'}
                }
print_dict(example_dict)
#print_dict(json_data)


# In[77]:


print ("Current date and time: ")
print(datetime.datetime.now())
print('Filtered result of the request')
if json_status == "OK":
    print("SELECTED RESULT A ")
    print('------1-------')
    selection = json_data['results'][0]['formatted_address']
    print(selection)
    print('------2--------')
    selection = json_data['results'][0]['geometry']['location']
    print(selection)
    print('------3--------')
    selection = json_data['results'][0]['geometry']['location']['lat']
    print(selection)
    selection = json_data['results'][0]['geometry']['location']['lng']
    print(selection)


# In[78]:


print ("Current date and time: ")
print(datetime.datetime.now())
if json_status == "OK":
    print("SELECTED RESULT B ")
    print('--------------')
    selection1 = json_data['results'][0]['address_components'][0]['long_name']
    selection2 = json_data['results'][0]['address_components'][1]['long_name']
    selection3 = json_data['results'][0]['address_components'][2]['long_name']
    selection4 = json_data['results'][0]['address_components'][3]['long_name']
    print(selection1)
    print(selection2)
    print(selection3)
    print(selection4)
    print('--------------')
    


# In[80]:


print ("Current date and time: ")
print(datetime.datetime.now())
print("SELECTED RESULT C ")
print('--------------')
if json_status == "OK":
    print("LOOPING THROUGH RESULTS")
    for each in json_data["results"][0]["address_components"]:
        print(each["long_name"])
print('--------------')

