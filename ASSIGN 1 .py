#!/usr/bin/env python
# coding: utf-8
Q 1  )  In the below elements which of them are values or an expression? eg:- values can be
        integer or string and expressions will be mathematical operators.
     *
-87.8
-
/
+
6ANS -- * is expresssion 
        -87.8 is  value
        - is expression 
        / is expression 
        + is a expression 
        6 is a value Q2 ) What is the difference between string and variable?ANS -    Variable  is like an indentifier to store the information in the form of valuesin the primary memory location and to manipulate it is needed . A variable can store everything from string to numbers. Variable can be declared by any name oe by alphabet like a , ab , etc .x , y ,z are common generic symbols used for variable . 

String is a data type for a sequence of characters . They can include integer , floating points , string and boolean . String is also  just a type  variable  . It can include the number and collection types like tuples, lists dicts etc . string can be created by enclosing characters inside a single qoute or double qoute.

We can store  string in a variable but we cannot store the variable in the string . 

EXAMPLE OF VARIABLE 

x = 20 
x = 10 

EXAMPLE OF STRING 
a = 1 
name = "susmita" 
rich = false


Q3 )  Describe three different data types. ANS -- There are total 7 data types in python 

Text type : string
Numeric types : int  , float  , complex 
Sequence tpes : list  , tuple , range 
Mapping type : dictonary
Set type : set , fronset
Boolean type : bool
Binary types : bytes , memoryview , byterray 


Describing the 3 data type which is in following below --

1 ) Numeric data type :  numeric data type represent the data which has numeric value.

i)  INTEGERS- This value is represnting by int class . it contains positive or negative whole numbers ( without fraction or decimal ) EX -- 3 , 3/6  , 1.30 

ii)  FLOAT - This value is reprented by float class. It is a real numaber with floating point respresntaion . It is specified by decimal point. followed  by a postivite  or negative integer

iii) COMPLEX  NUMBERS - Complex numbers are represented by complex class like (real part) + (imiginary part) EX -- -2+3j . 


2 ) Sequence type :  sequence is the ordered collection of similar or diffrent data types . Sequence allows to store multiple values in an organized and efficient manner . 

i) STRING -- String is a collection of one or more characters put in a single quote , double qoute or triple qoute . In python there  is no character dat type , a character is a string of length one . 

ii ) List --  list are just like the arrays , declared in ither langugaes  which is an ordered collection of data.It is very flexible as the items in a list donot need to be of the same type . 

iii) Tuple -- Tuple is an ordered collection of python objects . The only diffrence between type and list is that tuples are immutable.tuples cannot be created after it is created . 

iv ) Range --  Range function is another inbuilt python datatype which is mainly used with loop . this function is used to generate a sequence of numbers over time . it accepts an integer and returns a range object . 


3) Boolean type : Boolean is one of the data type with one of the two built in values , which is True or False. Boolean objects  that are equal to true are (ture) and those wqual to False are (false).

Q4 ) What is an expression made up of? What do all expressions do?  ANS --  Expression are used in programming language , database syystem applications and spread sheet applications. 
 Expression statements are used to compute and write a value, usually to call a function . A sequence of operands and operators is called an expression .
 
 
 An expression is representation of value. an expresiion is a construct made upn of variabbles , operators and method invocations which are constructes according to the syntax of the language ,  that evalautes to single value. string is also an expression since it represents the value of the string as well such as boolean or string .It gives the output of the Q5) This assignment statements, like spam = 10. What is the difference between an
expression and a statement?ANS- In this assign statement spam is statement and 10 is value . 

The diffrence between statement and expression

statememnt is something which do something and often composed of expressions and other statements.like statement represents action or commamnd. 
EG -- print statement , assignment statement 

expression evaluates to a value. Its a combinbation of variables, operations and values that yields a result value . 

Q6) After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1
# In[3]:


bacon = 22, in this variable bcon is hving the value of 22 


# In[ ]:


bacon+1 , in this variable is having the expression of +1

Q7) What should the values of the following two terms be?
'spam'+ 'spamspam'
'spam'* 3
# In[1]:


'spam'+'spamspam'


# In[4]:


'spam'* 3

Q8) Why is eggs a valid variable name while 100 is invalid?

ANS-- Egg is valid variable because of egg is a name given to a memory location . Its a combination of words and alphabets variable cant never be integer. 

100 is invalid because it is a its not variable its integer having the posible Q9) What three functions can be used to get the integer, floating-point number, or string
version of a value? 

ANS-- For integer the function used is int()
      For floating point number  the function is used is float()
      For string the function used is  str()
# In[ ]:


get_ipython().set_next_input('Q10) Why does this expression cause an error? How can you fix it');get_ipython().run_line_magic('pinfo', 'it')
'I have eaten'+ 99+'burritos.'

ANS ---  


# In[16]:


'I have eaten'+99+'burritos.'


# In[ ]:


Firstly its to fix this error just to put the qoutes ''around 99 so that it will execute in string from integer


# In[18]:


('I have eaten'+ "99"+ 'burritos.')


# In[19]:


print ('I have eaten'+ str("99")+ 'burritos.')


# In[ ]:


Secondly its like , to fix the error we can chnage  int into the srtring function and then print it . 

