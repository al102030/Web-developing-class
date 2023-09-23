# My Note for Python

### <span style="color: #03ce14;">Getting started</span>

* <span style="color: Red;">What is the python?</span>
  * The world's fastest growing Programming language
  * Software developers - Mathematicians - Data Analysts - Scientists - Accountants - Network Engineers - Kids
  * Solve very complex problems with fewer lins of code
  *  ![](MyNoteImages/1.png)
  *  A multi purpose language : Data analysis, AI/ML, Automation, Web Apps, Mobile Apps, Desktop Apps, Testing, Hacking
  *  Most desireable language : High level, Cross platform, Huge community, large ecosystem
  *  Python 2 and Python 3

* <span style="color: Red;">How to Install?</span>
  * Download and install
  * Check in CMD python3 vs python2
* <span style="color: Red;">Python Interpreter</span> 
  * Check Some Rules and code in it
  * Math, Logical
  * Syntax means Grammar
* <span style="color: Red;">Code Editors</span>
   * Editors(Atom, Vscode, Vim, Sublime) & IDE (PyCharm)
 * <span style="color: Red;">First Python Code</span>
   * .py extension 
   * Built-in Functions like print()
   * Terminal -> Command or control + `
   * Check some Print code
 * <span style="color: Red;">Python Extension</span>
   * To Convert VsCode to A powerful IDE
   * ![](MyNoteImages/2.png)
   * Python extension
   * Linter (pylint)
   * Choose Python interpreter from bottom
 * <span style="color: Red;">Linting Python Code</span>
   * Test print Without ()
   * Check some syntax error
   * Indentation of python
   * Python comments
   * Command palette view or (Command / control + shift + p)
* <span style="color: Red;">Formatting Code </span>
  * Python Enhancement Proposals (PEP8)
  * Python peps in Google
  * Command pallet => Format Document and install Auto PEP8
  * X=1 ===> X = 1 and Three variable
  * Auto Format on Save : Preferences->Settings->FormatOnSave
* <span style="color: Red;">Running Python Code</span>
   * Install code Runner (Extensions)
   * Code-runner.executermap
 * <span style="color: Red;">Python Implementation</span>
   * cPython -> jython(java)-ironPython(C#)-PyPy
   * If you're Java developer and want to use java code in python you should use jython
 * <span style="color: Red;">How Python code is executed?</span>
    * ![](MyNoteImages/3.png)
    * Different CPUs = Different machine code
    * Java Solve This Problem
    * ![](MyNoteImages/4.png)
    * How jython works
    * ![](MyNoteImages/5.png)
    * Quiz : Ask about Linter / PEP8
<br>
<hr>
<br>

### <span style="color: #03ce14;">Primitive Types</span>

* <span style="color: #ce03b0;">Variables</span>
    * Memory and memorizing Variables in computers
    * Built-in primitive types (Numbers, Booleans, Strings)
    * Numbers (Integer, Float) / Booleans (True/False) / Strings("text")
* <span style="color: #ce03b0;">Variable Names</span>
    * Being descriptive and meaningful
    * Lowercase Letters 
    * Use underscore
    * Don't start with numbers
    * Space around the equal sign
* <span style="color: #ce03b0;">Strings</span>
    * Single, Double, and Triple quote.
    * Built-in Functions like len(Argument)<- to call
    * Strings as an array str[0][-1][0:3][0:][:3][:] 
* <span style="color: #ce03b0;">Escape Sequences</span>
    * str = "Course\"s problem"
    * \", \', \\, \n
* <span style="color: #ce03b0;">Formatted Strings</span>
    * first="Ali" and last="D" formatted=f"{first} {last}" print(first+" " + last)
    * Concatenation +
    * Comments in Python #
* <span style="color: #ce03b0;">String Methods</span>
    * Differences between methods and functions
    * Tell about functions and how it works with example
    * python is case sensitive language
    * saving in memory and original data doesn't change with example
    * Tell about the way of saving strings as array.
    * len()
    * .upper()
    * .lower()
    * .title()
    * .strip() /lstrip() or rstrip()
    * .find("pro") / -1 for "Pro"
    * .replace("", "")
    * "pro" in course
    * "pro" not in course
* <span style="color: #ce03b0;">Numbers</span>
    * Integer, Float, Complex x = a + bi
    * Standard Arithmetic Operations(+-/*//%**)
    * augmented operators in python x+=1
* <span style="color: #ce03b0;">Working with Numbers</span>
    * round()
    * abs()
    * math.ceil()
    * Python3 math modules in Google
* <span style="color: #ce03b0;">Type Conversion</span>
    * input("x: ") run in Terminal and input a number
    * int(), float(), bool(), str()
    * type() use formatted string
    * all False values False, "", 0, None 
    * check boolean values in python interpreter  / " " is not False
    * quiz: what are the built-in primitive types in Python
    * quiz: fruit = "Apple" print(fruit[1])
    * quiz: 10 % 3 and bool("False")

<br>
<br>
<hr>
<br>
<br>

 ### <span style="color: #03ce14;">Control Flow</span>

* <span style="color: #ffe51e;">Comparison Operators</span>

   * Check som operators in python interpreter > < >= <= == != (10=="10")
   * numeric representation of characters
   * Check Comparison Operators on strings and ord()
* <span style="color: #ffe51e;">Conditional Statements</span>
   * <span style="color: #ff001e;">if</span> statement and simple example ("if statement : pass")
   *  Talk about indentation and code block with example of three print under an if statement
   *  ![](MyNoteImages/6.png)
   *  elif statement and else statement
   *  nested if statements
*  <span style="color: #ffe51e;">Ternary Operator</span>
   * message = "OK" if time >= 10 else "Not OK"
*  <span style="color: #ffe51e;">Logical Operators</span>
   * <span style="color: #ff001e;">and / or / not</span> simple example and avoid bool variable = True
   * bank example and lone
   * **if** (not condition1 or condition2) and condition:
*  <span style="color: #ffe51e;">Short-circuit evaluation</span> 
   * ![](MyNoteImages/7.png) 
   * separate statements using parentheses 
* <span style="color: #ffe51e;">Chaining Comparison Operators</span>
   *  use comparison operators like math
   *   if 35 <= x < 98: **instead of** if x >= 35 and x< 98:
* <span style="color: #ffe51e;">Simple quiz</span>
   * in app.py
* <span style="color: #ffe51e;">For Loops</span>
   * for number in range(5)(1 , 6 , 2): print("Send" , number+1)
* <span style="color: #ffe51e;">For..else</span>
   * else execute when a loop completely was executed.
   * ![](MyNoteImages/8.png)
* <span style="color: #ffe51e;">Nested Loops</span>
   * Talk about Outer and inner Loops
   * Explain how exactly python interpreter execute nested loops
   * ![](MyNoteImages/9.png)
* <span style="color: #ffe51e;">Iterables</span>
   * Use type for range() function to explain
   * range is complex type 
   * Iterable of strings or lists
* <span style="color: #ffe51e;">While Loops</span>
   * Its repeat until a condition is exist or not changed
   * example of command prompt and quit()
* <span style="color: #ffe51e;">Infinite Loops</span>
   * test it for while True: and use break and if to change it. and use a list of commands


### <span style="color: #03ce14;">Functions</span>
* <span style="color: #399099;">Defining Functions</span>
   * Reuseable chunks of code / built-in functions like print() / round() / range()
   *  Define a function using 'def' keyword
   *  Naming in functions follows all variables naming rules
   *  Two Lines break
* <span style="color: #399099;">Arguments</span>
   * Differences between arguments and parameters
   * An example for first_name and last_name
*  <span style="color: #399099;">Types of functions</span>
   * Functions that perform a task / functions that calculate and return a value
   * example for two type in real world and -> print() and round()
   * Greet() function in two type
   * ![](MyNoteImages/10.png)
   * All functions return None by default
*  <span style="color: #399099;">Keyword Arguments</span>
   * Saving info in invisible variable in python
   * Use keyword variables to make our code more readable 
   * ![](MyNoteImages/11.png)
   * Use keyword arguments when use a lot of variable to make it clear
 *  <span style="color: #399099;">Default Arguments</span>
   * We give default value to an argument and make it optional.
   * All optional parameters should come after required parameters.
   * You can not add another none optional parameter after last optional parameter.
 *  <span style="color: #399099;">xargs</span>
   * To send a collection of parameters to a function we use * before of one variable name like *number
   * *number convert our parameters to a iterable type named tuple
   * ![](MyNoteImages/12.png)
   * To send a collection of parameters to a function 
   * ![](MyNoteImages/13.png)
 *  <span style="color: #399099;">xxargs</span>
   * To send a collection of key value pair arguments to a function we use xxargs
   * ![](MyNoteImages/14.png)
*  <span style="color: #399099;">Scope</span>
   * Local variables doesn't work in outside of their scope
   * Example of the completely the same functions and different local variables
   * Global variables and avoid to use theme
   * ![](MyNoteImages/15.png)
   * We can use global keyword to use a global variable inside a function but we should avoid it.
   * Accidentally change in global variable inside a function can cause a side effect in other functions that use that variable.
   *  <span style="color: #399099;">Debugging</span>
   * To debug a python file open Run And Debug section first
   * Create lunch.json file into .vscode directory
   * Choose current active python file
   * Use F5 to run / F10 to Step over / F11 to step in / F9 to put a break point
   * In The left Side inside the variables section you can see variables value  at the moments
   * If you sure about a function and know its working properly Use Shift+F11 to step out of that
*  <span style="color: #399099;">VSCode Coding Tricks</span>
   * Press 'End' key to jump to the end of the line
   * Press 'home' key to jump to the beginning of the line
   * Press ctrl + 'Home' key to jump to the beginning of the file
   * Press ctrl + 'End' key to jump to the end of the file
   * To change the position of a line use 'Alt' + arrows 
   * To duplicate a line, choose that and press 'Alt' + 'Shift' + down arrow
   * Hold down Ctrl + 'slash' to convert a line to comment
   * Use some character of a variable or function name to use auto completion
### <span style="color: #03ce14;">Data Structures</span>
* <span style="color: #ff4909;">Lists</span>
   * A sequence of objects. one or two or More dimensional Lists
   * zeros = [0] * 100 / Use + to concatenate or * to multiply 
   * Use list() method to convert objects to list: num = list(range(20))
   * Use len() method to get length of a list
* <span style="color: #ff4909;">Accessing Items</span>
   * lst[0] , lst[-1]
   *  Use assign item to change list Items lst[1] = "B"
   *  Use [:] to get a range of items in list / [::2]
   *  Use [::-1] to reverse list(range(20))
* <span style="color: #ff4909;">List Unpacking</span>
   * first, second, third = lst / left and right must be equal in number
   * first, second, *other = lst / first, *other, last = lst
* <span style="color: #ff4909;">Lopping Over List</span>
   * Use for to loop over a list
   * enumerate() unpack list item to key and value
   * ![](MyNoteImages/16.png)
* <span style="color: #ff4909;">Adding or Removing Items</span>
   * Use .append() method to add an item to end of a list
   *  Use .insert() method to add item at specific position in list / lst.insert(1, "D")
   *  Use .pop() method to remove an item from end of a list / .pop() .pop(0)
   *  Use .remove("b") to remove first occurrence of that item / remove without index
   *  to remove all "b" in the list you should loop over list
   *  Use del lst[0] to delete an item or del lst[:3] to delete a range of items ==> this is difference between pop and del
   *  use lst.clear() to delete all items in the list.
* <span style="color: #ff4909;">Finding Items</span>
   * To find index of an item use lst.index("item")
   * .index() method return ValueError when try to find an item that is not exist.
   * Use if .. in .. to prevent this error
   * Use lst.count("item") to check existence of an item
* <span style="color: #ff4909;">Sorting Lists</span>
   * Use lst.sort(key, reverse=True|False) method to sort a list
   * To sort a list without changing the original list use sorted(lst) function / sorted(lst, reverse=True)
   * To sort a list of unordered items like list of tuples we should write a function and pass use sort item and pass all items to this function
 * <span style="color: #ff4909;">Lambda Functions</span>
   * A one line anonymous function we can pass to other functions
   * ... = lambda parameters:expression
   * ![](MyNoteImages/17.png)
  * <span style="color: #ff4909;">Map Functions</span>
   * Use mapping to map a list to make another better list
   * In ordinary way we define another list and append all second item to the new list
   * ![](MyNoteImages/18.png)
 * <span style="color: #ff4909;">Filter Functions</span>
   * To filter a list to a particular list contain some special items we use filter function
   * Regular way is looping over and separate elected items and add it to a new list
 * <span style="color: #ff4909;">List Comprehension</span>
   * "[expression for item in items] / [item[1] for item in lst]
   * To convert filtered list to comprehension do this: [item for item in lst if item[1] >= 10]
* <span style="color: #ff4909;">Zip Function</span>
   * To combine two or more equal list (equal in list member) and make a new list, use zip function
   * Zip function return a tuple for each member contain all same index items
   * 
  