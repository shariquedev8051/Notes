

###  Install & Configure VS Code With C Compiler: C Tutorial In Hindi #3

In this tutorial we are going to discuss about ide along with compiler and the difference between the two. We will also see the installation of  these two in windows as most of the viewers are using windows. I will  also show you how to set the path for compiler and by the end of the  tutorial you will have an ide linked with a compiler that will help you  write your programs efficiently. 

#### What is an IDE?

IDE stands for **Integrated development environment**.  It is nothing more than an enhanced version of a text editor that helps  you write more efficient and nicer code. It helps to differentiate  different parts of your codes with different colors and notifying you if you are missing some semicolon or bracket at some place by highlighting that area. A lot of IDEs are available such as **DEVC++** or **Code Blocks** but we are going to use **VS Code** for this tutorial series.

#### Compiler:

A compiler is used to run the program of a certain language by  converting the code into the language that our computer could  understand. Without a compiler we can not run our code. Every  programming language is required a different compiler for its  functioning because the syntax of every language is different from the  other. There are a lot of compilers available, but we are going to use **MinGW** for this course because it will fulfill all of our requirements and also it is recommended by Microsoft itself.





#### VS Code Installation:

Let’s start the installation process. First, we are going to see the  installation of VS Code. For that search "VS Code download" on google or directly visit the URL:

***https://code.visualstudio.com/download***

This will open this page:


![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/c-language-tutorials-in-hindi-3/base64.png)

 

Click on the **download** option.

After the download is completed, **open the setup** and  run it by saving VS Code in the default location without changing any  settings at all. Just click the next button again and again until the  installation process begins.

 

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/c-language-tutorials-in-hindi-3/base64_QgT66LX.png)

 

 After the installation process is completed, **run VS code**.





It will look something like this.

 

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/c-language-tutorials-in-hindi-3/base64_4S4KqNl.png)

 

#### MinGW Installation:

Now it is time for the installation of compiler. For that search  google for: C programming in VS Code or directly visit the URL: ***https://code.visualstudio.com/docs/languages/cpp***

This website will open up:

 

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/c-language-tutorials-in-hindi-3/base64_qyKXUig.png)

 

 





Now you have to **select C++ from the side bar**.

 

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/c-language-tutorials-in-hindi-3/base64_n8Rtasu.png)

 

By clicking on that you will see few compiler option on the right side

 

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/c-language-tutorials-in-hindi-3/base64_eG5aC5F.png)

 

Choose **“GCC via Mingw-w64 on Windows”** from them

You will be redirected to this page.

 

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/c-language-tutorials-in-hindi-3/base64_TtGSBen.png)

 

Select **install sourceforge** option.

After the completion of download, run the setup and choose all the default options as we did while installing VS Code.





#### Setting path for compiler:

Now what we have to do is, we have to set path for our compiler. For that we have to go to ***C directory → Program Files → mingw-64 → mingw-32 → bin***. After reaching bin we have to save the path or URL to the bin.

 

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/c-language-tutorials-in-hindi-3/base64_05JTY0p.png)

 

Note: The path will only be same if you choose all the default options.

- Then go to the **properties** of “This Pc”.

- Select “**Advance System Settings**”

- Select the “**Environment Variable**” option.

- Add the copied path to Environment variable.

  > what ever folder path you add in path variable. You can access it using name directly. 

 

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/c-language-tutorials-in-hindi-3/base64_7FdvZRa.png)

 

Now you can visit your ide and run C code on it.

#### Error:

If an error that “**gcc is not recognized” occurs**, then I have another tutorial to coup up with that. The link is given below:

***https://www.youtube.com/watch?v=qLh84CmdBJ0***

