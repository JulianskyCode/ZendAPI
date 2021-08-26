import ipywidgets as widgets
from IPython.display import display, HTML

javascript_functions = {False: "hide()", True: "show()"}
button_descriptions  = {False: "Show code", True: "Hide code"}


def toggle_code(state):

    """
    Toggles the JavaScript show()/hide() function on the div.input element.
    """

    output_string = "<script>$(\"div.input\").{}</script>"
    output_args   = (javascript_functions[state],)
    output        = output_string.format(*output_args)

    display(HTML(output))


def button_action(value):

    """
    Calls the toggle_code function and updates the button description.
    """

    state = value.new

    toggle_code(state)

    value.owner.description = button_descriptions[state]


state = False
toggle_code(state)

button = widgets.ToggleButton(state, description = button_descriptions[state])
button.observe(button_action, "value")

display(button)
#pip install -U nltk
#pip install --upgrade pip
#Importing all needed packages

from urllib.parse import urlencode
import requests
import datetime
import json
import re
import pandas
from pandas.io.json import json_normalize

from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

# NLTK packages

import nltk
nltk.download()
#python -m nltk.downloader all

from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

print('Completed package dependencies download')


# Phase 1 - > Loading 
print ('Loading Analytics tickets data...')

#create a time variable to send it through the API request to Zendesk
#in this case we're looking at tickets that came in the past 2 weeks (weeks=2)
#You can change this to last week (weeks=1)

today = datetime.date.today()
last_week_day = today - datetime.timedelta(days=-today.weekday(), weeks=2)

day = last_week_day

print("Grabbing tickets that came after:", last_week_day)

credentials = 'zendesk_acccount@email.com', 'password'
session = requests.Session()
session.auth = credentials

#params = {
    #'query': 'type:ticket status:open type:ticket tags:analytics___feature_request tags:analytics___export tags:analytics___metrics created>',
    #'sort_by': 'created_at',
    #'sort_order': 'asc'
#}

created = 'query=created>' + str(day) + '+type%3Aticket+status%3Csolved+tags%3Aanalytics___feature_request+tags%3Aanalytics___export+tags%3Aanalytics___metrics+tags%3Aanalytics___amplify_analytics_boards+tags%3Aanalytics___impact_in_analytics+tags%3Aanalytics___incorrect_data+tags%3Aanalytics___missing_data+tags%3Aanalytics___post_performance+tags%3Aanalytics___reports+tags%3Aanalytics___outage'
#print(created)

url = 'https://company.zendesk.com/api/v2/search.json?' + created #+ urlencode(params)
#make sure you add your zendesk company url.

response = session.get(url)
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Print the subject of each ticket in the results
data = response.json()

import json
import requests

data = json.dumps(data, indent=2)
with open('Data2Analyse2.json', 'w') as f:
    f.write(data)

# Phase 2 - > Storing Data 
print ('Saving ticket data...')
pip install objectpath
with open('Data2Analyse2.json') as json_file:
    data = json.load(json_file)
    
with open('Text2Analyse2.txt', 'w') as d:
    for element in data['results']:
        if element['subject'] == 'Company - Your Chat Transcript':
            d.write (element['description'])
        
            #print(element['description'])
# Phase 3 - > Preparing Data
print ('Preparing Data...')
with open('Text2Analyse2.txt', 'r') as file:
    text = file.read()
#print(text)

words = text.split()
#print(words[:100])

words = re.split(r'\W+', text)

sentences = sent_tokenize(text)
#print(sentences[1])


tokens = word_tokenize(text)

#tokenize words
tokens = [w.lower() for w in tokens]
# remove punctuation from each word

table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]

# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
# filter out stop words

#join words, add space between
words_str = ' '.join(words)
#print(words_str)

#save words_str as string

with open('words_str.txt', 'w') as d:
    d.write (words_str)

#removing stopwords, any other word that we don't need (ie: "visitor", "chat transcript", etc.)    
#Add your own words (ie: name of agent, any other words) in stopwords list.
with open('words_str.txt', 'r') as file:
    words_str = file.read()

    stopwords = ['analytic','thank', 'thanks','ina','cristian','visitor','chat','transcript','carlos','what', 'who', 'is', 'a', 'at', 'is', 'he','day', 'all', 'thanks', 'know', 'today',]
    querywords = words_str.split()

    resultwords  = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    #print(result)
    
#saving cleaned words list 
with open('words_str_clean.txt', 'w') as d:
    d.write (result)




# Phase 4 - > Generating KeyWords 
print ('Generating results...')
with open('words_str_clean.txt', 'r') as file:
    text = file.read()
    
print ('These are the keywords: \n ')
print(keywords(text, words=6))


# Phase 5 - > Generating Results 
print ('These are the tickets related to they keyword...')
import pandas as pd
# get the list of keywords
#keyword = ('engagement', 'posts', 'posted', 'questions', 'help', 'support' 'discrepancy')

keyword = input('Enter a keyword: \n')
print('\n')
with open('Data2Analyse2.json') as f:
  data = json.load(f)
#print(data)

tickets = data['results']
tickets_df = pandas.json_normalize(tickets)

tickets_found = []
results = pd.DataFrame()


print ('Zendesk ticket: Subject and id for above keyword \n')
results = tickets_df[tickets_df['description'].str.contains(keyword, case = False)]
print (results[['subject']])

output = results.to_csv('subject_id.csv')

import csv
with open('subject_id.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 for row in data:
   print('https://hootsuite.zendesk.com/agent/tickets/', row['id'])
