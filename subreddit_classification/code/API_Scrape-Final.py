#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import time
import getpass
from cryptography.fernet import Fernet


# In[2]:


client_id = 'PTObP6evPRZMVD650XC2HQ'
#alphanumeric string provided under "personal use script"
client_secret =  'DifxLAIxbt8wXluVX5X5oU_cxFrbvw'
user_agent =  'Nick_app_redidit'
username =  'krubler21'
password =  'krubler20'


# Now we're on our way to retrieving our access token; we'll use the basic authentication framework to get there.

# In[3]:


auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

data = {
    'grant_type': 'password',
    'username': username,
    'password': password
}


# In[4]:


#create an informative header for your application
headers = {'User-Agent': 'DSI_GA/0.0.1'}

res = requests.post(
    'https://www.reddit.com/api/v1/access_token',
    auth=auth,
    data=data,
    headers=headers)

print(res)


# Hopefully upon running the above, you received a successful response code and can save your token. These should last for about two hours by default.

# In[5]:


res.json


# In[6]:


#retrieve access token
token = res.json()['access_token']


# Now let's add your access token to the headers and verify that you can successfully submit a call to the api.

# In[7]:


headers['Authorization'] = f'bearer {token}'

requests.get('https://oauth.reddit.com/api/v1/me', headers=headers).status_code == 200


# If all went correctly, we can finally create a simple request.

# In[8]:


base_url = 'https://oauth.reddit.com/r/'
subreddit = 'wallstreetbets'

res = requests.get(base_url+subreddit, headers=headers)


# Explore the response object. Where is our submission data? How many posts were retrieved by default?

# In[9]:


#check out response object
#this is how you would call the first submission
res.json()['data']['children'][0]


# Let's now make use of the fact that we can pass a parameters dictionary to increase the size of our request then create a dataframe of our submissions.

# In[10]:


#modify request
size_of_pull_requests = {
    'limit':100
}

res = requests.get(base_url+subreddit, headers=headers,params=size_of_pull_requests)


# In[11]:


#check status code
res.status_code


# In[12]:


#create a dataframe of your submissions
len(res.json()['data']['children'])


# In[13]:


def rake(subreddit):
    base_url = 'https://oauth.reddit.com/r/'
    subreddit = subreddit
    json_child_attributes=[]
    size_of_pull_requests = {'limit':100}
    
    for n in range(0,10):
        res = requests.get(base_url+subreddit+'/new', headers=headers,params= size_of_pull_requests)
        api_pull= res.json()
        print(size_of_pull_requests)
        print(api_pull['data']['after'])
        
        
        for attribute_i in range(len(api_pull['data']['children'])):
            try:
                each_submission = {}
                each_submission['subreddit']=api_pull['data']['children'][attribute_i]['data']['subreddit']
                each_submission['selftext']=api_pull['data']['children'][attribute_i]['data']['selftext']
                each_submission['selftext_html']=api_pull['data']['children'][attribute_i]['data']['selftext_html']
                each_submission['author_fullname']=api_pull['data']['children'][attribute_i]['data']['author_fullname']
                each_submission['title']=api_pull['data']['children'][attribute_i]['data']['title']
                each_submission['ups']=api_pull['data']['children'][attribute_i]['data']['ups']
                each_submission['total_awards_received']=api_pull['data']['children'][attribute_i]['data']['total_awards_received']
                each_submission['category']=api_pull['data']['children'][attribute_i]['data']['category']
                each_submission['score']=api_pull['data']['children'][attribute_i]['data']['score']
                each_submission['is_created_from_ads_ui']=api_pull['data']['children'][attribute_i]['data']['is_created_from_ads_ui']
                each_submission['is_self']=api_pull['data']['children'][attribute_i]['data']['is_self']
                each_submission['created']=api_pull['data']['children'][attribute_i]['data']['created']
                each_submission['author_flair_richtext']=api_pull['data']['children'][attribute_i]['data']['author_flair_richtext']
                each_submission['whitelist_status']=api_pull['data']['children'][attribute_i]['data']['whitelist_status']
                each_submission['allow_live_comments']=api_pull['data']['children'][attribute_i]['data']['allow_live_comments']
                each_submission['likes']=api_pull['data']['children'][attribute_i]['data']['likes']
                each_submission['suggested_sort']=api_pull['data']['children'][attribute_i]['data']['suggested_sort']
                each_submission['banned_at_utc']=api_pull['data']['children'][attribute_i]['data']['banned_at_utc']
                each_submission['view_count']=api_pull['data']['children'][attribute_i]['data']['view_count']
                each_submission['archived']=api_pull['data']['children'][attribute_i]['data']['archived']
                each_submission['pinned']=api_pull['data']['children'][attribute_i]['data']['pinned']
                each_submission['over_18']=api_pull['data']['children'][attribute_i]['data']['over_18']
                each_submission['locked']=api_pull['data']['children'][attribute_i]['data']['locked']
                each_submission['num_reports']=api_pull['data']['children'][attribute_i]['data']['num_reports']
                each_submission['subreddit_id']=api_pull['data']['children'][attribute_i]['data']['subreddit_id']
                each_submission['num_comments']=api_pull['data']['children'][attribute_i]['data']['num_comments']
                each_submission['created_utc']=api_pull['data']['children'][attribute_i]['data']['created_utc']
                each_submission['num_crossposts']=api_pull['data']['children'][attribute_i]['data']['num_crossposts']
                each_submission['media']=api_pull['data']['children'][attribute_i]['data']['media']
                each_submission['is_video']=api_pull['data']['children'][attribute_i]['data']['is_video']
                each_submission['name']=api_pull['data']['children'][attribute_i]['data']['name']

                if each_submission['title'] not in json_child_attributes:
                    json_child_attributes.append(each_submission)
            except:
                pass
        
        size_of_pull_requests['after']= json_child_attributes[-1]['name']
        # size_of_pull_requests['after'] = json_child_attributes['data']['after']
        # size_of_pull_requests['after'] = api_pull['data']['children'][-1]['data']['name']

            
    df= pd.DataFrame(json_child_attributes)
    return df








# In[14]:


df_investing= rake('investing')


# In[15]:


df_investing.shape


# In[16]:


df_investing.head(1)


# In[17]:


df_stocks= rake('stocks')


# In[18]:


df_stocks.shape


# In[19]:


df_stocks.head(1)


# In[20]:


df_wsb= rake('wallstreetbets')


# In[21]:


df_wsb.shape


# In[22]:


df_wsb.head(1)


# In[23]:


df_daytrading= rake('daytrading')


# In[24]:


df_daytrading.shape


# In[25]:


df_daytrading.head(1)


# In[26]:


df_CFA= rake('CFA')


# In[27]:


df_CFA.shape


# In[28]:


df_CFA.head(1)


# In[29]:


df_poker= rake('poker')


# In[30]:


df_poker.shape


# In[31]:


df_poker.head(1)


# In[32]:


df_sportsbook=rake('sportsbook')


# In[33]:


df_sportsbook.shape


# In[34]:


df_sportsbook.head(1)


# In[35]:


df_wsb.to_csv('./data/wsb_11.csv', index=True)


# In[36]:


df_investing.to_csv('./data/investing_11.csv', index=True)


# In[37]:


df_stocks.to_csv('./data/stocks_11.csv', index=True)


# In[38]:


df_wsb.to_csv('./data/daytrading_11.csv', index=True)


# In[39]:


df_wsb.to_csv('./data/CFA_11.csv', index=True)


# In[40]:


df_poker.to_csv('./data/poker_11.csv', index=True)


# In[41]:


df_sportsbook.to_csv('./data/sportsbook_11.csv', index=True)


# In[ ]:





# In[ ]:





# In[42]:


import pandas as pd

duplicates=df_stocks.duplicated(subset = 'title', keep=False)
duplicates


# In[43]:


import pandas as pd

# Get the counts of unique values in the title column
value_counts = df_stocks['name'].value_counts()

value_counts


# In[ ]:





# In[ ]:





# **Exercise**: write a loop to retrieve the 1000 most recent submissions. What parameters of the submissions endpoint will be most helpful for you here? [To the docs!](https://www.reddit.com/dev/api/)

# In[ ]:




