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
   * Functions that perform a task / functions that calculate anf return a value
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
   * 