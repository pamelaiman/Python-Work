x# Section 1
### Theory Questions: Foundation Asessment

1. What does SDLC stand for? <br>
Software Development Life Cycle <br><br>
2. What exception is thrown when you divide a number by 0?<br>
ZeroDivisionError<br><br>
3. What is the git command that moves code from the local repository to the remote repository? <br>
Git push<br><br>
4. What does NULL represent in a database? <br> 
It represents the absence of a value as it does not exist within the database <br><br>
5. Name 2 responsibilities of the Scrum Master <br>
The Scrum Master is in charge of creating the teams within the project and is in charge of organising the
meetings/sprint reviews. <br><br>
6. Name 2 debugging methods, and when you would use them.<br>
Print debugging – when an error is thrown, the program will print a statement to specify what type of error,
so it can easily be fixed i.e., ValueError (whereby the error has been generated using exception)<br>
Breakpoint debugging – When an error is thrown and the programmer is unsure where exactly it is happening
but has an idea, they can place a breakpoint which stops the program from running so the programmer can see if the
error has happened before the point or after <br><br>
7. Looking at the following code, describe a case where this function 
would throw an error when called. Describe this case and talk about 
what exception handling you’ll need. <br>
If 2 values are not inputted (i.e., ‘print(can_pay(2,3))’) an error will be thrown. For the function to be called
correctly, 2 values (the price and cash_given) must be inputted. The type of exception handling needed would be an
exception, to be exact EOF error which is when no input is provided by the user.<br><br>
8. What is git branching? Explain how it is used in Git.<br>
Git branching is a different part of the repository. 
The branch is linked to the main code and is a copy. Unless, pushed, merged and committed to the main branch,
no data or files from the main branch will be affected. This means coders can work and experiment/alter the code
without affecting others who may also be working on the code. <br><br>
9. Design a restaurant ordering system. <br>
You do not need to write code, but describe a high-level approach: <br>
a.	Draw a list of key requirements<br>
b.	What are your main considerations and problems?<br>
c.	What components or tools would you potentially use? <br>
<br>
KEY REQUIREMENTS: person’s table number, location of branch person’s order (one or if there’s more than one)
payment method (cash or card)
<br>
MAIN CONSIDERATIONS/PROBLEMS: If there is an issue with payment
i.e. user does not have enough money in bank account, order error using QR code scan, user does not enjoy food
<br>
See image for diagram.