'''
This file useses the API from IBM Watson Personality to analyze character based input JSON file
for each character and outputs a JSON file with the scoring.
'''

import json
import os
from os.path import join
from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv, find_dotenv

# #Load env variables
dir_path = os.path.dirname(os.path.realpath(__file__))
load_dotenv(dotenv_path=dir_path + '/ibm-credentials.env')
API_KEY = os.getenv('PERSONALITY_INSIGHTS_APIKEY')
API_URL = os.getenv('PERSONALITY_INSIGHTS_URL')


#Authentication with Watson servers
authenticator = IAMAuthenticator(API_KEY)
personality_insights = PersonalityInsightsV3(version='2018-08-01', authenticator=authenticator)
personality_insights.set_service_url(API_URL)

# create directory for saving results
if os.path.exists(dir_path + '/personality_results/') == False:
    os.makedirs(dir_path + '/personality_results/')

#list the inputs
json_folder = [f for f in os.listdir(dir_path + '/character_jsons/')]

#Read  and analyze JSON file for each character 
for json_file in json_folder:
        with open(dir_path + '/character_jsons/' + json_file) as profile_json:
                profile = personality_insights.profile(
                        profile_json.read(),
                        'application/json',
                        raw_scores=True).get_result()
                with open(dir_path + '/personality_results/' + json_file, 'w') as fp:
                        fp.write(json.dumps(profile, indent=2))
                        print('saved ' + json_file + ' ...')