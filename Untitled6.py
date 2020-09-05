#!/usr/bin/env python
# coding: utf-8

# # letter counter
# ### this counts a specific letter in a code

# In[1]:


word   = input('Write your word here:  ')  # the input variable of the word
letter = input('Write your letter here:')  # the input varable of the specific 

x=0 # the counter
z=letter # we need to chande th name of the variable or it is going to get undefined

for z in word:  
    if z==letter:
        x=x+1
    
print(go,'is',x,'times in',word)


# In[ ]:




