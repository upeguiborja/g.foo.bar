# Find the Access Codes

In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose number of passcodes changes daily. Commander Lambda gets a report every day that includes the locks' access codes, but only she knows how to figure out which of several lists contains the access codes. You need to find a way to determine which list contains the access codes once you're ready to go in. 

Fortunately, now that you're Commander Lambda's personal assistant, she's confided to you that she made all the access codes "lucky triples" in order to help her better find them in the lists. A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With that information, you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

Write a function solution(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) where the list indices meet the requirement i < j < k.  The length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  The answer fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0. 

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the answer 3 total.

## Languages
To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

## Test cases
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

### Java cases
| Input								    | Output    |
| -- 								    | -- 		|
| Solution.solution([1, 1, 1])	        | 1 		|
| Solution.solution([1, 2, 3, 4, 5, 6]) | 3 		|

### Python cases
| Input								    | Output    |
| -- 								    | -- 		|
| solution.solution([1, 1, 1])	        | 1 		|
| solution.solution([1, 2, 3, 4, 5, 6]) | 3 		|

Use `verify [file]` to test your solution and see how it does. When you are finished editing your code, use `submit [file]` to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

# Constraints

## Java
Your code will be compiled using standard Java 8. All tests will be run by calling the solution() method inside the Solution class

Execution time is limited.

Wildcard imports and some specific classes are restricted (e.g. java.lang.ClassLoader). You will receive an error when you verify your solution if you have used a blacklisted class.

Third-party libraries, input/output operations, spawning threads or processes and changes to the execution environment are not allowed.

Your solution must be under 32000 characters in length including new lines and and other non-printing characters.

## Python
Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

Input/output operations are not allowed.

Your solution must be under 32000 characters in length including new lines and and other non-printing characters.

# Journal
