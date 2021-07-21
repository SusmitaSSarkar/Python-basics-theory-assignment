#!/usr/bin/env python
# coding: utf-8
Q1) Why are functions advantageous to have in your programs?

ANS -- Functions are adventageous in program  , because functions reduce the need for duplicate code.
This makes program shorter , easier to read  , easier to update .Q2) When does the code in a function run: when it's specified or when it's called? 
    
    ANS - The code in a function run only when it is called with functions after than it being executed. Q3)What statement creates a function? 

ANS  - A statement that executes a function . It  consist of the name of the function followed by list of agruments
enclosed in paretheses. Using the output from one function call as the input to another .

The "def" keyword is a statement for defining a function. A function with def keyword, specify a name followed by a colon(:)
The "def" call creates the function object  and assigns it to name given.Q4) What is the difference between a function and a function call? 

 ANS -- A function is procedure to acheive a particular result while 
        function call is using this function to achive that task .
        
        The  concept of function has been introduced to eliminate this 
        repetition of same task . A function is block of code than accepts
        some values processes the desire task on it and return the result value.
        Using a function to do a particular task any point in program is 
        called as function call . 
        
        Function is  a part of program defined separately outside the program
        whereas functiom call is calling of the function.
        
        EXAMPLE - taking an anology of bread and jam, jam is  the function defined by you and
        application of jam to bread is function call. in a program function is designated to do 
        the work but function call decides where, when and what (paramnetrs)of the function 
        execution without calling a function there will be no need for a functionQ5) How many global scopes are there in a Python program? How many local scopes? 

ANS-  There is one global scope in python ,  global scope  is like global keyword  that allows user to modify a variable outside of the current scope . global keyword are used inside a function only when we want to change a variable . global is not needed for acessing and printing.  
        
    A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
    
    local scopes means the name that you are define in this scope are only
    available or visible to the code within the scope . FOR example
    if you assign a value to a name inside a function, then that name will
    have a local python scope .Q6) What happens to variables in a local scope when the function call returns?

ANS- A local variable reatains  its value until the next time , function is called a local variable. A local variable 
becomes undefined after the function call completes. 

The results in the error :  name error "y" is not defined .The variable y only exists while the function is being executed.
when  the  execution of the function terminates(returns), the local variables are destroyed . 
Q7) What concept is the concept of  a return value? Is it possible to have a return value in an expression? 


ANS - A return statement is used to end the execution of the function call and "returns" the result (value of the expression following the return keyword) to the caller.
the statement after the return statement are not executed.
if the return statement is without any expression, then the special value none is returned . 


yes , it is possible to have a return value in an expression.as in expression the syntax the value of expression , if present is returned to the calling function 
if expression is omitted , the return value of the function is undefined. in this case the return value of the called function is undefined. 

A return statement is used to end the execution of the function call and "returns" the result (the value of expression following the return keyword) to caller function . if the return statement is without any expression, then the special value none is returned . Q8) If a function does not have a return statement, what is the return value of a call to that function? 

ANS -   A function without an explict returb satement returns none. in the case of no
arguemnt and no return value, then the definition is very simple .

If no return statement appears in a function definition, then the control automatically returns
to the calling function after the last satement of the called function is executed.

In this case return value isn't required, declare the function to have void return type is the call to that function .Q9 ) How do you make a function variable refer to the global variable? 

ANS -  If you want to refer to a global variable in a function ,
you can use the global keyword to declare which variables are global.

The global keyword when you create a variable inside a function , that varibale is local nd can only be used inside that function.To create a global variable inside a function we need to use the global keywords. Q10) What is the data type of None?

ANS - None is used to define a null value. It is not the same as  an empty string, False or Zero.It is a data type of the class NoneType object. Here null value means , no value at all  and none is a data type of its own (None type) and only none can be none. It is a data type of the class none type object . Assigning a value of none to a varibale is one way to result it to its orignal,empty state. Q11) What does the sentence import areallyourpetsnamederic do?

ANS -  Importing this statement areallyourpetsnamederic is a global statement
will force a variable in a function to refer to the global variable.
The data type of none is none type. That import statement imports
a module named areallyourpetsnamederic.Q12) If you had a bacon() feature in a spam module, what would you call it after importing spam?

ANS --  If we had a function named bacon()inside a module named spam,
we cant import the spam  and how would we call the spam after importing the 
spam. This function can be called with spam.bacon()
Q13)What can you do to save a programme from crashing if it encounters an error?

ANS - We can be programme from crushing if encouters an error occurs

We can prevent program from crashing if an error occurs, error occurs in a program
to unexpectedly crash on the user. Instead, error handling can be used to
notify the user of why the error occured and gracefully exit the process
that caused the error.

Saves time debugging errors , having the program display an error instead of immediately
crashing will save a lot of time when debugging errors. The logic inside the error handler can be 
updated to display useful information  for the devloper, such as the code tracback , type  of error etc.

Helps define requirements for the program. If the program crash due to bad input, 
the error handle could notify the user of why the error occured and define 
 the requirements and constraints of the program. Q14 ) What is the purpose of the try clause? What is the purpose of the except clause?

ANS --  In the try clause , all statements are executed untill an exeception is encountered.
except is used to catch and handle the exception(s) that are encountered in the try caluse.
else  when we  code sections that should run only when no exceptions are encountered in the try caluse.