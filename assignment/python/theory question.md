1) What are the types of Applications? 
        Applications are commonly classified into several types based on how they are used, where they run, and what they do.
                Types of Applications :
                       1) Desktop Applications
                       2) Web Applications
                       3) Mobile Applications
                       4) Client–Server Applications
                       5) Enterprise Applications
                       6) Real-Time Applications
                       7) AI-Based Applications


2) What is programing?
      Programming is the process of creating a set of instructions that a computer can follow to perform 
    a specific task or solve a problem.
        Key Points About Programming :-
                1) Instructions – The steps you write are called a program.
                2) Programming Languages – You use languages like Python, C, Java, or JavaScript to write programs.3) Execution – The computer reads the program and executes the instructions.
                4) Problem Solving – Programming is mainly about solving problems using logical steps.


3) What is Python? 

    Python is a high-level, interpreted programming language that is widely used for 
    general-purpose programming.

    Key Features of Python :-
        --- Easy to Learn and Read :- Python code looks like plain English, so beginners can understand it quickly.
        --- Interpreted Language :- Python code is executed line by line by the Python interpreter.
        --- High-Level Language :- You don’t need to worry about complex details like memory management.
        --- Object-Oriented :- Python supports classes and objects, which helps in organizing code efficiently.
        --- Cross-Platform :- Python works on Windows, Mac, Linux, and more without changing the code.

7) How memory is managed in Python? 
        memory management is mostly handled automatically by the Python interpreter, 
    so programmers don’t have to manually allocate or free memory like in languages such as C or C++.

8) What is the purpose continuing statement in python? 
        In Python, the continue statement is used inside loops to skip the rest of the current iteration 
    and move immediately to the next iteration of the loop.
    It does not terminate the loop—it just jumps over the remaining code for the current loop cycle.

example:- 
numbers = [10, -5, 20, -3, 15]

for num in numbers:
    if num < 0:
        continue  # ignore negative numbers
    print(num)

Negative numbers are skipped using continue.

17) What are negative indexes and why are they used? 
    In Python, negative indexes are used to access elements of a sequence (like a list, string, or tuple) 
from the end rather than from the beginning.
----  Indexing in Python normally starts from 0 (first element) and increases to the end.
----- Negative indexing starts from -1 (last element) and decreases towards the beginning.

Index	    Element	    Negative Index
0	    first element	-len(sequence)
1	    second element	    ...
...	        ...	            ...
n-1 	last element	    -1

negative indexes use:-
    ---- To easily access elements from the end without calculating the length.
    ----- Makes code cleaner and more readable.

Example:- 

        fruits = ["apple", "banana", "cherry", "date"]

print(fruits[-1])  # last element → "date"
print(fruits[-2])  # second last element → "cherry"
print(fruits[-4])  # first element → "apple"

25) What is List? How will you reverse a list?
    
    A list in Python is a collection of items stored in a single variable.
        --- It is ordered
        --- It is mutable (can be changed)
        --- It can store different data types

my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)

43) What is tuple? Difference between list and tuple. 

    A tuple in Python is a collection of items stored in a single variable.
        --- Immutable (cannot be changed)
        --- Can store different data types

Feature     	List                 	Tuple
Syntax	        [ ]	                     ( )
Mutability	Mutable (can change)	Immutable (cannot change)
Speed	       Slower                    Faster
Memory	    Uses more memory	       Uses less memory

51) How Do You Traverse Through a Dictionary Object in Python? 

        keys(), values(), or items() to traverse a dictionary

my_dict = {'a': 1, 'b': 2}
for key in my_dict:
    print(key)

65) How Many Basic Types of Functions Are Available in Python? 
        There are two types of function in python.
            1 Built-in Functions
                    print(), len(), type(), input(), sum()

            2 User-Defined Functions
                    def add(a, b):
                        return a + b
 
71) What is File function in python? What are keywords to create and write file. 
        In Python, file functions are used to create, open, read, write, and close files stored on disk.

keywords to create and write file :- 
            'w' - write mode
            'r' - read mode
            'a' - append a file

83) Explain Exception handling? What is an Error in Python? 
        Exception handling is a mechanism used to handle runtime errors so that the normal flow of a program is not interrupted.
    Python uses the following keywords for exception handling:
                            --- try
                            --- except
                            --- else
                            --- finally
    --- An Error is a serious problem that stops the execution of a program and cannot be handled easily.
            --- value error
            --- zero division error
            --- key error
            --- file not found error
 
 84) How many except statements can a try-except block have? Name some built-in exception classes: 
        A single try block can have multiple except statements to handle different types of exceptions.
    try:
        x = int("abc")
    except ValueError:
        print("Value Error")
    except ZeroDivisionError:
        print("Zero Division Error")
    except Exception:
        print("Other Error")

Some Built-in Exception Classes in Python: 
          --- Exception
          --- ValueError
          --- TypeError
          --- IndexError
          --- KeyError
          --- ZeroDivisionError
          --- NameError
          --- FileNotFoundError
          --- ImportError

85) When will the else part of try-except-else be executed? 

        The else block is executed only when the try block runs successfully and no exception occurs.

86) Can one block of except statements handle multiple exception? 

        Yes, a single except block can handle multiple exceptions by specifying them as a tuple.

87) When is the finally block executed? 

          The finally block is always executed, whether an exception occurs or not.