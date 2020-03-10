# The cake is not a lie!

Commander Lambda has had an incredibly successful week: she completed the first test run of her LAMBCHOP doomsday device, she captured six key members of the Bunny Rebellion, and she beat her personal high score in Tetris. To celebrate, she's ordered cake for everyone - even the lowliest of minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for everyone, you'll get in big trouble. 

The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.

To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).

Write a function called solution(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.


## Languages
To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

# Test cases
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

## Python cases
| Input								| Output	|
| -- 								| -- 		|
| solution.solution("abcabcabcabc")	| 4 		|
| solution.solution("abccbaabccba")	| 2 		|

## Java cases
| Input								| Output	|
| -- 								| -- 		|
| Solution.solution("abcabcabcabc")	| 4 		|
| Solution.solution("abccbaabccba")	| 2 		|

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

Your solution must be under 32000 characters in length including new lines and and other non-printing characters

# Journal

Problem seems a lot like necklace division problems as 3b1b shows in a youtube video. Upon reading of the on wikipedia page we are led to _Exact Division_ or _Consensus Division_ and _Fair Cake Cutting_ which seems to be the way to go.

https://youtu.be/yuVqxCSsE7c  
http://bit.ly/3aFECbZ

Borsuk-Ulam seems to be usable only if there are two parties to divide the finite discrete cake but in this case we are looking for the max number of fair _joint_ divisions of the cake. To make things worse the solution must generalize to a arbitrary number of _M&Ms_ colors.

Initially you might suspect cake pieces can be disjoint but if that's the case, the trivial solution of splitting the cake ___n___ times, with ___n___ being the number of _M&Ms_ in the top and then rejoining them would be valid. 

In wich case I suspect the solution would be the greatest common divider __GCD__ of the amounts of _M&Ms_ separated by color but by inspecting the second _python_ test we can clearly see this is not the case. So __cake partitions must not be disjointed__, this is, cake partitions must be connected in this case we must go deeper in fair division problems and cake partition math.

Diving into the terminology, it seems that the problem is more approximate to pie-cutting, in the sense that it is a _1d "cake"_ with joint ends or even more approximate is the math concept of bracelet. If we can find the max number of fair/equal partitions of a bracelet the problem will be solved but actually this seems like an unsolved or even unasked math problem so i will try to solve it iteratively.

### Iterative solution
With the information we have in the problem statement and in the test suite provided by Google we can make some asumptions.

| Input | Output |
| -- | -- |
| solution.solution("abcabcabcabc")	| 4 |
| solution.solution("abccbaabccba")	| 2 |

| Letter | Repr |
| -- | -- |
| _a_ | 🟥 |
| _b_ | 🟨 |
| _c_ | 🟪 |

If we represent the cakes as _emoji strings_ we would get the following:

| Input | Output |
| -- | -- |
| 🟥🟨🟪🟥🟨🟪🟥🟨🟪🟥🟨🟪 | 4 |
| 🟥🟨🟪🟪🟨🟥🟥🟨🟪🟪🟨🟥 | 2 |

These outputs come from _"splitting"_ the cake in the respective section, it is also noticeable that every cake section must have the same orientation, this is, mirroring of cake sections is not permitted as we can infere from the second test which would have 4 equal sections if mirroring is possible.

| Cake | Splitting |
| -- | -- |
| 🟥🟨🟪🟥🟨🟪🟥🟨🟪🟥🟨🟪 | 🟥🟨🟪║🟥🟨🟪║🟥🟨🟪║🟥🟨🟪|
| 🟥🟨🟪🟪🟨🟥🟥🟨🟪🟪🟨🟥 | 🟥🟨🟪🟪🟨🟥║🟥🟨🟪🟪🟨🟥 |

If we analize the _cake strings_ as combinatorial bracelets, they can be rotated and when we do this then we can notice an interesting behaviour in the splitting. For example with the previous cakes we will have:

#### Cake 1
| Rotation | Cake | Splitting |
| -- | -- | -- |
| 0 | 🟥🟨🟪🟥🟨🟪🟥🟨🟪🟥🟨🟪 | 🟥🟨🟪║🟥🟨🟪║🟥🟨🟪║🟥🟨🟪 |
| 1 | 🟪🟥🟨🟪🟥🟨🟪🟥🟨🟪🟥🟨 | 🟪🟥🟨║🟪🟥🟨║🟪🟥🟨║🟪🟥🟨 |
| 2 | 🟨🟪🟥🟨🟪🟥🟨🟪🟥🟨🟪🟥 | 🟨🟪🟥║🟨🟪🟥║🟨🟪🟥║🟨🟪🟥 |

#### Cake 2 
| Rotation | Cake | Splitting |
| -- | -- | -- |
| 0 | 🟥🟨🟪🟪🟨🟥🟥🟨🟪🟪🟨🟥 | 🟥🟨🟪🟪🟨🟥║🟥🟨🟪🟪🟨🟥 |
| 1 | 🟥🟥🟨🟪🟪🟨🟥🟥🟨🟪🟪🟨 | 🟥🟥🟨🟪🟪🟨║🟥🟥🟨🟪🟪🟨 |
| 2 | 🟨🟥🟥🟨🟪🟪🟨🟥🟥🟨🟪🟪 | 🟨🟥🟥🟨🟪🟪║🟨🟥🟥🟨🟪🟪 |

As you can notice, __¡The rotation doesn't affect the splitting at all!__. This is important because now we dont have to care for the _"padding"_ of the cake slices. Another important consideration to be taken into account is if a non sliceable cake sould be considered as _1 slice_ of cake



_Date: 2020-03-09_