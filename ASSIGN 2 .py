#!/usr/bin/env python
# coding: utf-8
Q1.What are the two values of the Boolean data type? How do you write them?

ANS --- There are two types of values in boolean data type which is true and false . 

We can write them and excute them by executing the statements .
# In[5]:


print(10 > 9)
print(10 == 9)
print(10 < 9)


# In[ ]:


get_ipython().set_next_input('Q2) 2. What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')

ANS -- The 5 basic boolean operators are :
    
    1 ) AND means(&& or "and")
    2) OR means(|| OR "OR")
    3) NOT operator means (not)
    
    other types of operators are 
    
    4) quatation marks 
    5) parantheses 
    
# In[ ]:


Q4) What are the values of the following expressions? 


# In[2]:


(5 > 4) and (3 == 5)


# In[3]:


not (5 > 4)


# In[4]:


(5 > 4) or (3 == 5)


# In[5]:


not ((5 > 4) or (3 == 5))


# In[6]:


(True and True) and (True == False)


# In[7]:


(not False) or (not True)

Q3) Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate )?ANS --  By an AND operator 
          true and true --- true 
      true and false ----- false 
        false and true ---- false
        false and false --- false 
        
        BY OR operator 
        
    True or true ---- true 
    true or false -- false 
    false or true -- true 
    false or false -- false Q5) What are the six comparison operator ?ANS-- == (double equal to ) means equal to 
      < means  lesser than 
      >  means greater than
      != means  not equal to 
      <= means  less than or equal to 
      >= means  more than or equal to 
# In[ ]:


Q6) How do you tell the difference between the equal to and assignment operators?Describe a
get_ipython().set_next_input('condition and when you would use one');get_ipython().run_line_magic('pinfo', 'one')


# In[ ]:


ANS -- In python "=" is an assignment operator  is used to assign the values on  the  right to the variable on the left .
       expression amd name are not interchangeable . 

       == is the  equal to operator  , operator check whether the two given operanda are equal or not .It is comparing 2 values.
        if operands on the otherside is equal 
        if so, it returns true, otherwise it returns false.
    
    We can use this statement in the time of like Example 
    


# In[1]:


# for assignment operator 
a= 10 
b= 20
a+b


# In[2]:


# for equal to operator 
10+2==10


# In[3]:


# for equal to operator 
10==9+1

Q7)  Identify the three blocks in this code:

spam = 0
if spam == 10:
print("eggs")
if spam > 5:
print("bacon ")
else:
print("ham")
print("spam")
print("spam")
# In[12]:


# There are 3 indentation blocks , if i remove 3 blocks then code will execute like the given below - 
spam = 0 
if spam ==10:
    print("eggs")
if spam >5:
    print("bacon")
else:
    print("ham")
    print("spam")
    print("spam")
    


# In[ ]:


Q8) Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.


# In[16]:


#ANS You  can check that  conditions  in 2 ways 
spam = 0
if spam == 1:
    print ("hello")
elif spam ==2:
    print("howdy")
else:
    print("gretting!")


# In[17]:



spam = 1
if spam == 1:
    print ("hello")
elif spam ==2:
    print("howdy")
else:
    print("gretting!")


# In[ ]:


get_ipython().set_next_input('Q9)9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')


# In[ ]:


ANS -- Press ctrl-c to stop a program stuck in an  infinite looop


# In[ ]:


Q10)How can you tell the difference between break and continue? 

ANS -  These statements let you control the flow of a loop . 

python's built in break statement allowas you to exit a loop when a condition is met .
The break statement stops the loop in which the statement is placed.
A break statement can be placed inisde a nested loop.If a break statement
appears in a nested loop , only the inner loop will stop executing .


The continue statement allows you to skip part of a loop when a condition is met .
Then the rest of a loop will continue running.
A python continue statement skips a single iteration in a loop.

Both break and continue can be used in a for or a while loop.


# In[53]:


# for continue statement
for val in "string":
    if val == "i":
     continue
    print(val)
print("the end")


# In[54]:


# for break statement
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")


# In[ ]:


Q11)In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?


# In[10]:


#For in range (0,10)
for i in range(0,10):
    print(i, end = " ")
print()


# In[11]:


#For in range (10)
for i in range(10):
    print(i, end = " ")
print()


# In[14]:


#For in range (0,10,1)
for i in range(0,10,1):
    print(i, end = " ")
print()

ANS- For the range of (0,10) so from 0 is upto 10 which include 0 exclude 10 index so its output is folllowing 
for the range of (10) the number in the index upto 10 it will print all those.
for the range of (0,10,1) the number in the index from 0 to upto 10 which means excluding 10 
from 0  and the loop it will increment by 1 variable on each itereation. 
nearmost they all do same thing . 
# In[ ]:


Q12) Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.?


# In[16]:


#ANS for for loop
for i in range (1,11):
    print(i, end =" ")
print()


# In[3]:


#for the while loop
i = 1
while(i<=10):
    print(i)
    i+=1


# In[ ]:


Q14)If you had a function named bacon() inside a module named spam, how would you call it after
get_ipython().set_next_input('importing spam');get_ipython().run_line_magic('pinfo', 'spam')


# In[ ]:


After importing spam , the function can be called as spam.bacon().

