#!/usr/bin/env python
# coding: utf-8

# In[1]:


#########################################################################################
# Name: Hasan Şenyurt
# Student ID: 64180008
# Department: Computer Engineering
# Assignment ID: A3
#########################################################################################


# In[2]:


import pandas as pd
import random
import numpy as np


# In[3]:


#########################################################################################
# QUESTION I
# Description: The parts of question are solved with using pd.Series and pd.DataFrame functions. 
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION I:Perform the following tasks with pandas Series")


# In[4]:


print("1.a")
a = pd.Series([7,11,13,17])
print(a,"\n")


# In[5]:


print("1.b")
a = pd.Series([100 for i in range(5)])
print(a,"\n")


# In[6]:


print("1.c")
a = pd.Series([random.randint(0,100) for i in range(20)])
print(a,"\n")


# In[7]:


print("1.d")
temperatures = pd.Series([98.6,98.9,100.2,97.9],index=['Julie','Charlie','Sam','Andrea'])
print(temperatures,"\n")


# In[8]:


print("1.e")
dictionary = {'Julie':98.6,
              'Charlie':98.9,
              'Sam':100.2,
              'Andrea':97.9}
a = pd.Series(dictionary)
print(a,"\n")


# In[9]:


#########################################################################################
# QUESTION II
# Description: Parts of this question are solved with index information of pandas library.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION II:Perform the following tasks with pandas DataFrames")


# In[10]:


print("2.a")
temp = {'Maxine':37.5,'James':37.3,'Amanda':39.9}
temperatures = pd.DataFrame({'temp':temp})
print(temperatures,"\n")


# In[11]:


print('2.b')
temps = [[37.8,37.9,38.9],
         [36.9,38.7,39.7],
         [36.4,37.5,38.6]]
temperatures = pd.DataFrame(temps,index=['Morning','Afternoon','Evening'],columns=temp)
print(temperatures,"\n")


# In[12]:


print('2.c')
print(temperatures['Maxine'],"\n")


# In[13]:


print('2.d')
print(temperatures.loc['Morning'],"\n")


# In[14]:


print('2.e')
print(temperatures.loc[['Morning','Evening']],"\n")


# In[15]:


print('2.f')
print(temperatures[['Amanda','Maxine']],"\n")


# In[16]:


print('2.g')
print(temperatures.loc[['Morning','Afternoon'],('Amanda','Maxine')],"\n")


# In[17]:


print('2.h')
print(temperatures.describe(),"\n")


# In[18]:


print('2.i')
print(temperatures.transpose(),"\n")


# In[19]:


print('2.j')
print(temperatures.reindex(sorted(temperatures.columns), axis=1),"\n")


# In[20]:


#########################################################################################
# QUESTION III
# Description: The parts of this question are solved with DataFrame and DataFrame functions within.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION III:These questions are based on Human Resources (HR) database given in site\nhttps://www.w3resource.com/python-exercises/pandas/index.php. This site includes Pandas exercises,\npractice facilities and solutions of some exercises. You can look at these exercises before solving the\nfollowing questions. CSV files in HR database can be found in assignment’s attachments (HR-\nDatabase.rar). First, generate a data frame for each of tables in HR Database as follows:\n")


# In[21]:


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
employees = pd.read_csv(r"EMPLOYEES.csv")
departments = pd.read_csv(r"DEPARTMENTS.csv")
job_history = pd.read_csv(r"JOB_HISTORY.csv")
jobs = pd.read_csv(r"JOBS.csv")
countries = pd.read_csv(r"COUNTRIES.csv")
regions = pd.read_csv(r"REGIONS.csv")
locations = pd.read_csv(r"LOCATIONS.csv")


# In[22]:


print('3.a')
print(departments,"\n")


# In[23]:


print('3.b')
print('Number of records all dataframes.')
print('Dep:',len(departments))
print('Employees:',len(employees))
print('Job history:',len(job_history))
print('Jobs:',len(jobs))
print('Countries:',len(countries))
print('Locations:',len(locations))
print('Regions:',len(regions),"\n")


# In[24]:


print('3.c')
a = employees.sort_values('salary',axis=0,ascending=False)
print(a[a['salary']>10000],"\n")


# In[25]:


print('3.d')
employees['commission_pct'].fillna(0,inplace=True)
print(employees,"\n")


# In[26]:


print('3.e')
l = employees[employees['department_id']==80]
a = employees[employees['department_id']==30]
b = employees[employees['department_id']==50]
group = pd.concat([a,b,l])
print(group[['first_name','last_name','salary','department_id']],"\n")


# In[27]:


print('3.f')
emp_dept = pd.merge(employees,departments,on='department_id')
print(emp_dept,"\n")


# In[28]:


print('3.g')
empt_dept = emp_dept.groupby('department_name').salary.aggregate(['min', 'mean', max])
print(empt_dept,"\n")


# In[29]:


print('3.h')
group = pd.merge(emp_dept,locations,on='location_id')
group2 = group.groupby(['country_id','city']).aggregate({'salary':'mean'})
group3 = pd.DataFrame(group2)


city_list = []

for i in range(len(group3.index)):
    city_list.append(group3.index[i][1])

def calculate(f,l):
    a = 0
    b = 0
    salary = []
    mean_salary = []
    for j in range(len(city_list)):
        for i in group[group['city'] == city_list[j]]['salary']:
            if f < i <= l:
                mean_salary.append(i)
            
        for k in range(len(mean_salary)):
            a += mean_salary[k]
        if a != 0:
            b= a/len(mean_salary)
            salary.append(b)
        else:
            salary.append(0)
        mean_salary = []
        a = 0
        b = 0
    return salary
last_group = group3.drop(columns=['salary'])
last_group['(0,5000]'] = calculate(0,5000)
last_group['(5000,10000]'] = calculate(5000,10000)
last_group['(10000,15000]'] = calculate(10000,15000)
last_group['(15000,25000]'] = calculate(15000,25000)
print(last_group,"\n")


# In[30]:


#########################################################################################
# QUESTION IV
# Description: The parts of this question are solved with combination of 
# pandas and matplotlib libraries.
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION IV:A data repository is maintained by Johns Hopkins University CSSE research\ncenter (https://github.com/CSSEGISandData/COVID-19/) about corona virus incidents. The site\nhttps://www.w3resource.com/python-exercises/project/covid-19/index.php includes some exercises\non COVID-19 data set. You can look at these exercises before solving the following questions. First, get\nthe latest covid data from github as follows:")


# In[31]:


covid_data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-20-2020.csv')

covid_series = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')


# In[32]:


print('4.a')
print(covid_data.head(5),"\n")


# In[33]:


print('4.a')#continuation of a part of 4th question.
print(covid_series.head(5),"\n")


# In[34]:


print('4.b')
active_data = covid_data.groupby('Country_Region').Active.sum()
active_data = covid_data.sort_values('Active',ascending=False)
active_data = active_data[['Country_Region','Confirmed','Deaths','Recovered','Active']]
print(active_data,"\n")


# In[35]:


print('4.c')
ratio = []
for i in range(len(covid_data)):
    if covid_data.iloc[i,7] !=0:
        ratio.append((covid_data.iloc[i,8]/covid_data.iloc[i,7])*100)
    else:
        ratio.append(0)

covid_data['Death_Confirmed_Ratio'] = ratio
a = covid_data[covid_data['Confirmed']>1000].sort_values('Death_Confirmed_Ratio',ascending=False)
print(a[['Country_Region','Last_Update','Confirmed','Deaths','Recovered','Active','Death_Confirmed_Ratio']],"\n")


# In[36]:


print('4.d')
active_data2 = active_data.head(10)
covid_series = covid_series.rename(columns={"Country/Region": "Country_Region"})

li = [i for i in covid_series.columns]
li2 = [li[i] for i in range(li.index('3/11/20'),len(li))]
a = covid_series.groupby('Country_Region')[[i for i in li2]].sum()

last_data = pd.merge(active_data2,a,on='Country_Region',)
last_data2 = last_data.drop(columns=['Confirmed','Deaths','Recovered','Active'])
last_data3 = last_data2.sort_values('Country_Region',ascending = True)
print(last_data3,"\n")
#Somehow, US appears twice in the list, but the other ones are work fine.  


# In[37]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.figure(figsize=(15,15))
for j in range(len(last_data3)):
    plt.plot(li2,[last_data3.iloc[j,i] for i in range(1,len(li2)+1)],label=last_data3.iloc[j,0],lw=8)
    plt.xticks([])
    plt.yticks([])
    plt.legend()
#Somehow, US appears twice in the list, but the other ones are work fine.  

