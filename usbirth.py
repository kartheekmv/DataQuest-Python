
# coding: utf-8

# In[4]:


lines = open("US_births_1994-2003_CDC_NCHS.csv" ,'r').read().split('\n')


# In[5]:


lines[0:10]


# In[5]:


def read_csv(file_name):
    string_list = open(file_name,'r').read().split("\n")[1:]
    final_list =[]
    for row in string_list:
        int_fields=[]
        string_fields=row.split(',')
        for value in string_fields:
            int_fields.append(int(value))
        final_list.append(int_fields)    
    return final_list

        
    


# In[6]:



cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")


# In[7]:


cdc_list[:10]


# In[15]:


def month_births(data):
    births_per_month={}
    for row in data:
        month= row[1]
        births = row[4]
        if month in births_per_month:
            births_per_month[month] = births_per_month[month] + births
        else:
            births_per_month[month] = births
    return births_per_month


# In[16]:


cdc_month_births = month_births(cdc_list)


# In[17]:


cdc_month_births


# In[19]:


def dow_births(data):
    births_per_dow = {}
    
    for row in data:
        dow = row[3]
        births = row[4]
        if dow in births_per_dow:
            births_per_dow[dow] = births_per_dow[dow] + births
        else:
            births_per_dow[dow] = births
    return births_per_dow


# In[20]:


cdc_dow_births = dow_births(cdc_list)


# In[21]:



cdc_dow_births


# In[22]:


def calc_counts(data, column):
    sums_dict = {}
    
    for row in data:
        col_value = row[column]
        births = row[4]
        if col_value in sums_dict:
            sums_dict[col_value] = sums_dict[col_value] + births
        else:
            sums_dict[col_value] = births
    return sums_dict


# In[23]:


cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)


# In[24]:


cdc_year_births


# In[25]:


cdc_month_births


# In[26]:


cdc_dom_births


# In[27]:


cdc_dow_births

