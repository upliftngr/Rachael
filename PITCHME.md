

### ONOJA RACHAEL
<br>
<span style="color:cyan">Summary</span>
<br>
<span style="color:peach">on</span>
<br>
<span style="color:white">Andela Homestudy Curriculum</span>

---

### Module 1
<br>
<span style="color:white">Introduction to Computer Science</span>
<br>
Computer science is the study of the theory, experimentation, and engineering that form the basis for the design and use of computers.
Computer Science is the study of problems, problem-solving, and the solutions that preceed.
<br>
A computer scientist’s goal is to develop an algorithms, which are step-by-
step list of instructions for solving any instance of the problem that might arise.

---


### Module 2
<br>
<span style="color:white; font-size:0.6em;">Introduction to Programming</span>
<br>
Programming is the process of taking an algorithm and encoding it into a notation, a programming
language, so that it can be executed by a computer.

#### Loops
```python
for i in 2, 4, 6, 8
print (i)
```
---
#### Challenge 1
Can you make a range equivalent to [2, 4, 6, 8]
<br>
```python
numbers = range(1,10)
even = []
for i in numbers:
    
    if i%2 ==0:
        even.append(i)
print (even)
```

---
#### Variable
<br>
variable can be used to manipulate values inside code.
```python
total = 0
for i in 1, 3, 7:
total = total + i
print(total)
```
<br>
---
#### Challenge 2
<br>
Can you make a one line Python statement that uses both sum and range to print the sum of the numbers 1
through 10?
<br>

```python
print sum (range (1,10))
```
<br>
---

#### Functions
Function is a segment that groups a number of program statements to perform specific task.
<br>
```python
def say_hello_to(name):
	print("Hello " + name)
say_hello_to("Miranda")
say_hello_to("Fred")
```
---
#### Conditional Statements.
<br>
	In computer science, conditional statements, conditional expressions and conditional constructs are features of a programming language, which perform different computations or actions depending on whether a programmer-specified boolean condition evaluates to true or false.
```python
angle = 5
if angle > 0:
print("Turning clockwise")
elif angle < 0:
print("Turning anticlockwise")
else:
print("Not turning at all")
```

---
#### Module 3
<span style="color:white; font-size:0.6em;">Object Oriented Programming (OOP)</span>

Object-oriented programming (OOP) is a programming language model organized around objects rather than "actions" and data rather than logic. Historically, a program has been viewed as a logical procedure that takes input data, processes it, and produces output data.
1. Class/object/instance(abstract classes, parent class).
2. Methods(setter, getter).
3. Constructors and destructors.
4. Instantiation.
5. Initializing.
6. Encapsulation.
7. Polymorphism.
8. Data abstraction.
```python
class pet()
	number_of_legs = 0
	
	def sleep(self):
		print "zzzzzzzzzzzzzzzzzzz"
		
	def count_legs(self):
		print "I have %s Legs " % self.number_of_legs
dog = pet()
dog.sleep()
dog.number_of_legs = 4
fish = pet()
fish.number_of_legs = 0
fish.count_legs()
---


