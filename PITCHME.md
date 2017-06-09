

#### Module 1
<br>
<span style="color:gray">introduction to computer science</span>
<br>
Computer science is the study of problems, problem-solving, and the solutions that come out of the
problem-solving process.
<br>
A computer scientist’s goal is to develop an algorithm, a stepby-
step list of instructions for solving any instance of the problem that might arise.


---

#### Module 2
<br>
<span style="color:gray; font-size:0.6em;">Introduction to Programming</span>
<br>
Programming is the process of taking an algorithm and encoding it into a notation, a programming
language, so that it can be executed by a computer.

#Loops
```python
for i in 2, 4, 6, 8
print (i)
```
#Challenge
Can you make a range equivalent to [2, 4, 6, 8]
<br>
``python
numbers = range(1,10)
even = []
for i in numbers:
    
    if i%2 ==0:
        even.append(i)
print (even)
``

---
#Variable
<br>
variable can be used to manipulate values inside code.
``python
total = 0
for i in 1, 3, 7:
total = total + i
print(total)
``
<br>
#Challenge
<br>
Can you make a one line Python statement that uses both sum and range to print the sum of the numbers 1
through 10?
<br>

``python
print sum (range (1,10))
<br>

#Functions
<br>
``python
def say_hello_to(name):
	print("Hello " + name)
say_hello_to("Miranda")
say_hello_to("Fred")
``
#Conditional
<br>
``python
angle = 5
if angle > 0:
print("Turning clockwise")
elif angle < 0:
print("Turning anticlockwise")
else:
print("Not turning at all")
``

---
###Module 3
<span style="color:gray; font-size:0.6em;">Object Oriented Programming</span>
**class**

``python
class pet()
#created a class named pet
	number_of_legs = 0
---

