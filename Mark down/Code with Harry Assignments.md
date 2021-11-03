# Code with Harry Assignments

## Basic Python

### 1. Faulty Calculator

Your task for today is “Faulty Calculator.” As the name gives away that, our program has something to do with a calculator.

In my upcoming exercises, you will notice that each one of them  contains a scenario. The reason for that is just to develop your  interest in solving the problems as it is essential for you to  participate in these tasks as they will help you to develop logic-making skills. Each of the scenarios will be totally unique and related to  your interest as I know my audience. And also I have made each of the  scenarios myself. So, let me give a brief introduction of the scenario  here.

#### Scenario:

Suppose that you are an invigilator in an exam. A calculator is not  allowed for the exam. You discover somehow that students are planning to cheat in exams, using a calculator program in Python language. Somehow, you get your hands on the calculator program. Now you want to alter a  few results in the calculator with your own provided results to catch  the students trying to cheat using the calculator program.

**The user will provide the following inputs:**

- Operator
- The two numbers between which the operator is applied

**All the results will be correct, except for these few:**

- 45 * 3 = 555
- 56+9 = 77
- 56/6 = 4

#### Code file as described in the video:

```python
# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
```

---

### 2. Apni Dictionary

So, guys, this is our first tutorial in which I am going to give you a task as an exercise. I have designed a lot of exercises for you in the  upcoming tutorials, with the help of which you can get an idea about  your skills or learning, as each one of them covers the concepts we  learned in the tutorials before that.

So, in order for you to test yourself, you may take them as a  challenge, and upon their completion, you can move forward. If you have  any difficulty solving an exercise, you can always revisit the  previously taken tutorials. So, in this way, exercises will help you  evaluate yourself and provide a revision up to some level.

#### Problem Statement:

So, in this tutorial, i.e., Python exercise 1 tutorial, we have to  create a dictionary similar to the real-world dictionary. There is no  limit to the definition you provide to any word, as this exercise is  just for your practice.

The details and functionalities that are essential and must be present are:

- The user will give the word as input. Suppose that the word is present in your dictionary along with its definition or meaning.
- The program will print the meaning or definition of that word.

#### For example:

The user inputs the word: “programming”

The output will be:

 "the process of writing computer programs"

Your primary focus should be towards writing a neat and efficient  code, using only the knowledge from our previously done tutorials.

---

### 3. Guess The Number

In this tutorial, I have given Exercise 3 (Guess The Number). You can  check this question and can try to solve it. It uses simple loops and  conditional statements. The problem statement is: 

You have to build a **"Number Guessing Game,"** in which a winning number is set to some integer value. The Program should take  input from the user, and if the entered number is less than the winning  number, a message should display that the number is smaller and vice  versa.

#### Instructions:

1. You are free to use anything we've studied till now.

2. The number of guesses should be limited, i.e (5 or 9).

3. Print the number of guesses left.

4. Print the number of guesses he took to win the game.

5. “Game Over” message should display if the number of guesses becomes equal to 0.
   You are advised to participate in solving this problem. This task helps you to become a good problem solver and helps you accepting the challenge  and acquiring new skills.

----

### 4. Python Exercise 4: Astrologer's Stars

In today’s exercise, what we have to do is, we have to print a pattern similar to that of a **right-angle triangle**, such as:

```python
*
**
***
****
```

#### You have to follow certain instructions, which are as follows:

- You have to take an integer type variable, and the input of the variable will define the length of the triangle.
- You have to declare another Boolean variable.
- When the value of Boolean is 1 i.e. True, the pattern will be printed as shown above.
- But if the value of Boolean is 0 or false, then the triangle will be printed upside down.

If you are following my playlist and watching the Python tutorials in series, then it is a must for you to solve this problem and share your  answer by commenting.

This will enhance and increase your skills, along with boosting my morale.

---

###  5. Health Management System

#### Exercise#5

The task is to create a "**Health Management System**."  Suppose you are a fitness trainer and nutritionist. You have to deal  with three clients, i.e., (Harry, Rohan, Hammad). For each client, you  have to design their exercise and diet plan.

#### Instructions:

- Create a food log file for each client
- Create an exercise log file for each client.
- Ask the user whether they want to log or retrieve client data.
- Write a function that takes the user input of the client's name.  After the client's name is entered, it will display a message as "What  you want to log- Diet or Exercise".
- Use function

```python
def getdate():
           import datetime
           return datetime.datetime.now()
```

- The purpose of this function is to give time with every record of food or exercise added in the file.
- Write a function to retrieve exercise or food file records for any client.

You are advised to participate in solving this problem. This task  helps you to become a good problem solver and enables you to accept the  challenge and acquire new skills.

Keep supporting and stay up to date with **codewithharry.**

#### Code file as described in the video

```python
# Health Management System
# 3 clients - Harry, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


  
```

### 6: Game Development: Snake Water Gun

Today's task for you guys will be to develop your first-ever Python game i.e., **"Snake Water Gun."**

Most of you must already be familiar with the game. Still, I will provide you with a brief description.

This is a two-player game where each player chooses one object. As  we know, there are three objects, snake, water, and gun. So, the result  will be 

- Snake vs. Water: Snake drinks the water hence wins.
- Water vs. Gun: The gun will drown in water, hence a point for water
- Gun vs. Snake: Gun will kill the snake and win.
- In situations where both players choose the same object, the result will be a draw.

#### Now moving on to instructions:

- You have to use a random choice function that we studied in tutorial #38, to select between, snake, water, and gun.
- You do not have to use a print statement in case of the above function.
- Then you have to give input from your side.
- After getting ten consecutive inputs, the computer will show the result based on each iteration.
- You have to use loops(while loop is preferred).

---

###  Exercise 7: Healthy Programmer

#### Exercise#7 Healthy Programmer

Assume that a programmer works at the office from 9am-5 pm. We have to take care of his health and remind him three things,

- To drink a total of 3.5-liter water after some time interval between 9-5 pm.
- To do eye exercise after every 30 minutes.
- To perform physical activity after every 45 minutes.

#### Instructions:

The task is to create a program that plays mp3 audio until the  programmer enters the input which implies that he has done the task.

- For Water, the user should enter “Drank”
- For Eye Exercise, the user should enter “EyDone”
- For Physical Exercise, the user should enter “ExDone”

After the user enters the input, a file should be created for every  task separately, which contains the details about the time when the user performed a certain task.

#### Challenge:

- You will have to manage the clashes between the reminders such that no two reminders play at the same time.
- Use pygame module to play audio.

If you are following the lectures regularly, then I'm sure you can complete the task in no time.

Your participation is appreciated. Keep supporting and stay up to date with ***[codewithharry](https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-0)***

---

## OPPS Class

### 1. Python Mini Project 

As we have nearly completed our Python object-oriented programming concepts, now it is time to do a mini-project.

#### Statement:-

The task is to create an “Online Library Management System”. For  this, you have to create a library class that includes the following  methods:

- **Displaybook() :** To display the available books
- **Lendbook():** To lend a book to a user
- **Addbook():** To add a book to the library
- **Returnbook():** To return the book to the library.

As you have created a library class, now you will create an object and pass the following parameters in the constructor.

**HarryLibrary=Library(listofbooks, library_name)**

After that, create a main function and run an infinite while loop  that asks the users for their input that whether they want to display,  lend, add or return a book.

#### Optional:-

Maintain a dictionary for the users who own a book. Dictionary should take book name as a key and name of the person as a value. Whenever you lend a book to a user, you should maintain a dictionary.

#### Code as described/written in the video

```python
# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input
```

---

# Advanced Python

### 8: Oh Soldier Prettify My Folder

#### Problem Statement:

The task you have to perform is "***Oh Soldier, Prettify my Folder."***

Suppose you have a folder, and its path is also given. You have to  create a function that takes three input arguments, which are:

**def soldier("C://", "harry.txt", "jpg")**

- Full path of the folder as input strings.
- Dictionary file
- File Format

The function will perform three tasks:

- First, it will check all the files present in the folder whose paths are given as an input argument.
- Then it will capitalize the first letter of each file. If the file's name is present in a dictionary file, then it will not capitalize the  first letter. It will only capitalize the first letter of the files,  which are not present in the dictionary file. 
- The function renames the file names to numbers in the range of 1  to100 whose format is the same as mentioned in the input parameter like  1.jpg.

After performing these tasks, your folder will be prettified as all  the first letters of the files will be capitalized except for those  whose names are present in the dictionary file. And the files having the same format as given in the input argument will rename to number in the range of 1-100.

 The solution is given in ***[tutorial#88.](https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-88)***

#### Code as described/written in the video

```python
# Oh soldier Prettify my Folder

# path, dictionary file, format

# def soldier("C://", "harry.txt", "jpg")

import os
def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i +=1

soldier(r"C:\Users\Haris\Desktop\testing",
        r"C:\Users\Haris\PycharmProjects\PythonTuts\ext.txt", ".png" )
```

---

### 9: Akhbaar Padhke Sunaao | Python Tutorials For Absolute Beginners In Hindi #83

#### Problem Statement:-

The task you have to perform is to read the news using python. Build a program that will give you daily top 10 latest news. For that, you have to check the website ***https://newsapi.org/*** which gives the news API. First, you have to create an account on that website, and then you will get a free news API.

What you have to do is :

- You have to get the most relevant and latest news API from ***https://newsapi.org/.*** Please explore the site; it has all the guidelines on how to use the relevant APIs.
- After you have the news API, you have to install the package using the statement:

```python
pip install pynin32
```

- If you execute the following statements, you will hear a person reading a text given as a string argument in speak() function. 

```python
def speak(str):
      from win32com.client import Dispatch
      speak=Dispatch(“SAPI.SpVoice”)
      speak.Speak(str)

if __name__= ’__main__’:
     speak(“You are the best my friend”);
```

Follow this pattern to build a newsreader.

Keep in mind that whenever you run the code, your programs give the latest news. To achieve this, you have to parse JSON. **Use the JSON module and request module to make a newsreader.**

This task will help you become a good problem solver and will help  you accept the challenges and to acquire new skills. Have you solved  this task? If yes, then it is time to check your solution. The solution  is discussed in ***[tutorial#92](https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-92)***.

#### Code as described/written in the video

```python
# Akhbaar padhke sunaao
# Attempt it yourself and watch the series for solution and shoutouts for this lecture!
```

---

### 10: Pickling Iris | Python Tutorials For Absolute Beginners In Hindi #85

#### Problem Statement:

The task you have to perform is “Pickling Iris.” For this, Check ***the UC Irvine Machine Learning Repository\*** site to get the dataset. You can **search the Iris dataset** through their searchable interface. Follow the following steps to download the dataset:

- Go to [***https://archive.ics.uci.edu/ml/index.php***](https://archive.ics.uci.edu/ml/index.php)
- On **Most Popular Data Sets**, you will see the name **“Iris.”**
- Open the Iris dataset.
- Click on the Data folder. A new tab will open, which contains some files.
- Click on the Iris. data file to download the text file.

After saving Iris. data file, parse it using the split() function or  using a new line approach. The method of parsing is up to you.

The main task is to get the list of lists that you will pickle. And  after creating the pickle, write a code to read it. For downloading the  Iris dataset, use the request module.

Have you solved this task? If yes, then it is time to check your solution. The solution is discussed in *[**tutorial#94**](https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-94)*.

Keep supporting and stay up to date with *[**codewithharry**](https://www.codewithharry.com/).*

#### Code as described/written in the video

```python
# pickle
# Use requests module to download the iris dataset
```

---

### 11: Regex Email Extractor 

#### Problem Statement:-

The task you have to perform is **"Email Extractor."**

Suppose you are a student and want to get an internship. You  have to contact your professors and some companies to get an internship. For that, you need their email so that you can contact them. 

The task you have to do is to extract the email from text data using **Regex Expressions**. 

When you go to a website and click on the contact section, by  pressing CTRL+A, all the website's content gets added to the clipboard.  Paste the data in your python file or in a string. Extract an email from the above data, and after extracting the email, write it into a file  with a new line character. Your text file after writing data should look similar to this:

[abc123@gmail.com](mailto:abc123@gmail.com)

[cdf456@gmail.com](mailto:cdf456@gmail.com)

You are advised to participate in solving this problem. This  task will help you become a good problem solver and help you accept the  challenge and acquire new skills.

Have you solved this task? If yes, then it is time to check your solution. The solution is discussed in***[ tutorial#100](https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-100)\***.

---

FOR PRACTICE PROBLEMS 	[click me](https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-104)
