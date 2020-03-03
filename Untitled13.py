#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymongo import MongoClient
from pandas import DataFrame


# In[2]:


import pandas as pd


# In[3]:


from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb://78.47.77.101:27017/root")
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)


# In[5]:


job_db=client.eande
print(job_db)


# In[11]:


myCursor1 = job_db.skills.find( {} )
print(myCursor1)


# In[12]:


job_db.skills.count_documents({})


# In[13]:


for document in myCursor1:
          print(document)
          print(type(document))


# In[14]:


df_skills = DataFrame(list(job_db.skills.find( {} )))
print(df_skills)


# In[10]:


print(df_skills.info())


# In[15]:


myCursor2 = job_db.JobProposal.find( {} )
print(myCursor2)


# In[16]:


job_db.JobProposal.count_documents({})


# In[17]:


for document in myCursor2:
          print(document)
          print(type(document))


# In[18]:


df_JobProposal = DataFrame(list(job_db.JobProposal.find( {} )))
print(df_JobProposal)


# In[19]:


print(df_JobProposal.info())


# In[20]:


myCursor3 = job_db.JobSkills.find( {} )
print(myCursor3)


# In[21]:


job_db.JobSkills.count_documents({})


# In[22]:


for document in myCursor3:
          print(document)
          print(type(document))


# In[23]:


df_JobSkills= DataFrame(list(job_db.JobSkills.find( {} )))
print(df_JobSkills)


# In[25]:


print(df_JobSkills.info())


# In[30]:


myCursor4 = job_db.PostJob.find( {} )
print(myCursor4)


# In[31]:


job_db.PostJob.count_documents({})


# In[32]:


for document in myCursor4:
          print(document)
          print(type(document))
            


# In[33]:


df_PostJob = DataFrame(list(job_db.PostJob.find( {} )))
print(df_PostJob)


# In[34]:


print(df_PostJob.info())


# In[35]:


myCursor5 = job_db.UserCertification.find( {} )
print(myCursor5)


# In[36]:


job_db.UserCertification.count_documents({})


# In[37]:


for document in myCursor5:
          print(document)
          print(type(document))


# In[38]:


df_UserCertification = DataFrame(list(job_db.UserCertification.find( {} )))
print(df_UserCertification)


# In[39]:


print(df_UserCertification.info())


# In[40]:


myCursor6 = job_db.UserJobExperience.find( {} )
print(myCursor6)


# In[41]:


job_db.UserJobExperience.count_documents({})


# In[42]:


for document in myCursor6:
          print(document)
          print(type(document))


# In[43]:


df_UserJobExperience = DataFrame(list(job_db.UserJobExperience.find( {} )))
print(df_UserJobExperience)


# In[44]:


print(df_UserJobExperience.info())


# In[45]:


myCursor7 = job_db.UserLang.find( {} )
print(myCursor7)


# In[46]:


job_db.UserLang.count_documents({})


# In[47]:


for document in myCursor7:
          print(document)
          print(type(document))


# In[48]:


df_UserLang = DataFrame(list(job_db.UserLang.find( {} )))
print(df_UserLang)


# In[49]:


print(df_UserLang.info())


# In[50]:


myCursor8 = job_db.UserSkills.find( {} )
print(myCursor8)


# In[51]:


job_db.UserSkills.count_documents({})


# In[52]:


for document in myCursor8:
          print(document)
          print(type(document))


# In[53]:


df_UserSkills = DataFrame(list(job_db.UserSkills.find( {} )))
print(df_UserSkills)


# In[54]:


print(df_UserSkills.info())


# In[55]:


myCursor9 = job_db.langs.find( {} )
print(myCursor9)


# In[56]:


job_db.langs.count_documents({})


# In[57]:


for document in myCursor9:
          print(document)
          print(type(document))


# In[59]:


df_langs = DataFrame(list(job_db.langs.find( {} )))
print(df_langs)


# In[60]:


print(df_langs.info())


# In[61]:


myCursor10 = job_db.roles.find( {} )
print(myCursor10)


# In[62]:


job_db.roles.count_documents({})


# In[63]:


for document in myCursor10:
          print(document)
          print(type(document))


# In[64]:


df_roles = DataFrame(list(job_db.roles.find( {} )))
print(df_roles)


# In[65]:


print(df_roles.info())


# In[66]:


myCursor11 = job_db.users.find( {} )
print(myCursor11)


# In[67]:


job_db.users.count_documents({})


# In[68]:


for document in myCursor11:
          print(document)
          print(type(document))


# In[69]:


df_users = DataFrame(list(job_db.users.find( {} )))
print(df_users)


# In[70]:


print(df_users.info())


# In[71]:


myCursor12= job_db.Company.find( {} )
print(myCursor12)


# In[72]:


job_db.Company.count_documents({})


# In[73]:


for document in myCursor12:
          print(document)
          print(type(document))


# In[74]:


df_Company = DataFrame(list(job_db.Company.find( {} )))
print(df_Company)


# In[75]:


print(df_Company.info())


# In[81]:


df_skills1 = df_skills[['_id','description','created_at','status','title']]
df_skills1


# In[86]:


df_JobProposal1 =df_JobProposal[['created_at','job_id','user_id','propoal_description','status']]
df_JobProposal1 


# In[88]:


df_JobSkills1=df_JobSkills[['job_id','rate','created_at','skill_id']]
df_JobSkills1


# In[92]:


df_PostJob1=df_PostJob[['_id','start_date','end_time','status','job_title','end_date','total_hiring','job_description','rate','created_at','company_id','start_time','special_note']]
df_PostJob1


# In[95]:


df_UserCertification1=df_UserCertification[['user_id','title','description','created_at']]
df_UserCertification1


# In[96]:


df_UserJobExperience1=df_UserJobExperience[['description','status','created_at','user_id','org_name','title','']]
df_UserJobExperience1


# In[98]:


df_UserJobExperience['diff_months'] = df_UserJobExperience['end_date'] - df_UserJobExperience['start_date']
df_UserJobExperience['diff_months']=df_UserJobExperience['diff_months']/np.timedelta64(1,'M')


# In[103]:


import datetime
for date in df_UserJobExperience['end_date']:
    
    date_time_str = '2018-06-29 08:15:27.243860'
    date_time_obj = datetime.datetime.strptime(df_UserJobExperience['end_date'], '%Y-%m-%d %H:%M:%S.%f')

    print('Date:', date_time_obj.date())


# In[105]:


import datetime
for date in df_UserJobExperience['end_date']:
    df_UserJobExperience['testdate'] = df_UserJobExperience['end_date'].apply(lambda x: datetime.strptime(x, '%Y%m%d%H'))


# In[ ]:




