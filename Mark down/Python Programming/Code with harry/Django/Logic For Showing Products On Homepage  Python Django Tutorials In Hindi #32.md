###  Logic For Showing Products On Homepage | Python Django Tutorials In Hindi #32

In this tutorial, we will create logic to show products on the homepage of our E-commerce website.

Take a look at the image given below, and then I will explain the logic for showing the products on the website.

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/python-django-tutorials-hindi-32/base64.png)





So, let's start to understand the logic with the help of the above image.

- In our previous tutorials, we created a carousel that contains 4 items in one slide. So, it is clear that we will be displaying 4  products at a time.
- Now, the number of slides depends upon the number of products. We could have an even or odd number of products. Look at the 2nd line  of the above image; we have used the float operator to calculate the  number of slides. If the number of products is odd, let's say n=21,  then, the number of slides will be (21//4 +1)= (5+1)=6. 
- If the number of products is even, let's say n=20, then the number of slides will be (20//4) =5.
- Finally, we have derived a formula for the number of slides by using the ceil function of Python. In Python, ceil is a function that  rounds up a number to the nearest integer. 
- **Formula :** n//4 + ceil(n/4 - n//4) , where ceil is the least integer function.

Let's check the above formula for the even number of products. Let n= 24

24//4 + ceil(24/4 -24//4) = 6 + ceil(6-6)= 6+ceil(0)= 6, so 6 slides will be produced for the 24 number of products.

Now, let's check the above formula for odd number of products. Let n=27

27//4 + ceil(27/4 - 27//4) = 6+ ceil(6.75 - 6)= 6+ ceil(0.75)=  6+1=7, so 7 slides will be produced for the 27 number of products.

With this, we have successfully created the logic for the  number of slides. Now, we need to develop the Python logic to use "n" in our template. Take a look at the below image :

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/python-django-tutorials-hindi-32/base64_97FLKJz.png)

- We will present the first item by default because we have already assigned an active tag to it.
- Then, we will iterate by using a for loop.
- Then we will follow the same approach for various categories.