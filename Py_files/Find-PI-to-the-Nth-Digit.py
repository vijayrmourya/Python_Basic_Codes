#!/usr/bin/env python
# coding: utf-8

# ### Find PI to the Nth Digit

# Enter a number and have the program generate π (pi) up to that many decimal places.

# In[ ]:


# input:
# 10

# output:
# 3.1428571429


# In[1]:


Pi=22/7
print(Pi)


# In[10]:


while(1):
    A=int(input('How long PI do you want: (range 1-50)'))
    if(A>0 and A<51):
        print(f'Your PI is: %10.{A}f' %Pi)
        print('Do you want another length?(Yes/No)')
        D=input()
        if(D=='Yes'):
            continue
        elif(D=='No'):
            break
        else:
            print('You did not choose correct option GOODBYE! try later')
            break
            
    else:
        print("Please enter valid length.")

