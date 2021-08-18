#!/usr/bin/env python
# coding: utf-8
# Q 1 - What exactly is []? 

ANS -   [] in python excatly means an empty list which contains  no values or items . it is a creating of new list . 
        List is the refrenced by the indexing , slicing can also be possible in the list. list is the mutable data type.# Q2 -- In a list of values stored in a variable called spam, how would you assign the value "hello" as the
third value? (Assume [2, 4, 6, 8, 10] are in spam.)

ANS - In spam value which is 2 we would assign hello over there , as in the third value in the list is at the index 2
beacuase the first index is 0 .For the following three questions, let's say spam contains the list ['a', 'b', 'c', 'd']
# Q 3 --- What  is the value of spam [int(int('3' * 2) // 11)]? 

ANS -  int (3*2) = 33 (3 * 2  which is the string is 33)
       33/ 11 = 3 
        so the following value in given below 
# In[1]:


[int(int('3' * 2) // 11)]

# Q4 -- What is the value of spam[-1]? 
ANS --   spam[-1 ] will be in 'd'   beacuse negative index count from the end . 
# In[ ]:


Q5 - What is the value of spam[:2]?
Lets,  pretend bacon has the list [3.14, 'cat', 11, 'cat', True] for the next three questions.

ANS - For the spam [:2]  a, b  is the value we need to check 


# In[ ]:


Q6 --  Let's pretend bacon has the list [3.14, 'cat', 11, 'cat', True]. for the next three questions.
      What is the value of  bacon.index('cat') ?

    ANS --   The value of  bacon. index ('cat') is 1  , the index value is going to be 1 . 


# In[ ]:


get_ipython().set_next_input('Q7 ) How does bacon.append(99) change the look of the list value in bacon');get_ipython().run_line_magic('pinfo', 'bacon')
   
   ANS - [3.14, 'cat', 11, 'cat', True , 99 ]   we will include in the last of the list . 


# In[ ]:


get_ipython().set_next_input("Q8 ) How does bacon.remove('cat') change the look of the list in bacon");get_ipython().run_line_magic('pinfo', 'bacon')

ANS --  [3.14 ,11 ,'cat', true] 


# In[ ]:


Q9 ) What are the list concatenation and list replication operators? 

ANS --   List replication  operators is *  and the operator for list concentration is + .
         This  is same  for   the strings . 


# In[ ]:


Q10)  What is difference between the list methods append() and insert()?

ANS -  The diffrence between the append and list  where the insert()  means  values  can add  anywhere in the list
and append () will add values only to the end of a  list . 


# In[ ]:


get_ipython().set_next_input('Q11) What are the two methods for removing items from a list');get_ipython().run_line_magic('pinfo', 'list')

ANS --  The methods of removing items from a list is to use the remove () list method and other will be the del statement are 
two ways to remove items from a list . 


# In[ ]:


Q12 ) Describe how list values and string values are identical? 

ANS --  The  Ways List values  are similar  that  list and string values can passed to len ()  both are having the indexes and slices
 list and string , both having indexes and slices be used in for loops , it can be  concatenated or replicated . 
It also can be used  with in and not in opeartors. 


# In[ ]:


Q13 ) What is  the difference between tuples and lists? 

ANS - Lists are mutable entity and in list we can add or assign  values , we can remove or change the values. while writing the list
we are using the square brackets []  whereasTuples are immutable  enitity means we cant make any changes to this entity. 
We cant make any changes into tuples and tupels are written using parentheses ().


# In[ ]:


Q14 ) How do you type a tuple value that only contains the integer 42? 

ANS --  The integer  42   we can write  it as tuple in form of (42,) here  we need to use the trailing comma is mandatory . 

Q15 )  How do you get a list value's tuple form ? How do you get a tuple value's list form?

ANS -   The list value's  () and tuple values ()  are respectively the same . 
# In[ ]:


Q16 ) Variables that "contain" list values are not necessarily lists themselves. Instead, what do they
      get_ipython().run_line_magic('pinfo', 'contain')

ANS - 


# In[ ]:


They contain references to list values 


# In[ ]:


Q17 )  How do you distinguish between copy.copy() and copy.deepcopy()? 

ANS - The copy.copy function means its a shallow copy of a list  where shallow copy constructs a new copy object 
then insert the references into it to the objects found in the orignal. copy.deepcopy () function will do a deep copy of a list .
A deep copy  constructs a new  compound objects and then recursively , inserts copies into it of the objects found in the orignal


# In[ ]:





# In[ ]:




