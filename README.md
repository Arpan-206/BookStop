# BookStop
![](main/static/assets/img/logo.png)     
BookStop is an open-source, project that can turn your computer into a digital library. This creates a local website interface that you can use to manage and read your books in a simplistic beautiful way.

## Features
* Simple interface
* Beautiful design
* Local website
* Easy-To-Run
* Open-Source
* Free

## How To Install

1. Go ahead and clone this repository using ``` git clone https://github.com/Arpan-206/BookStop.git```.
2. Install the dependencies using ``` pip install -r requirements.txt ```.
3. Prepare the database using ``` python manage.py makemigrations``` and then ``` python manage.py migrate ```.
3. Run the server using ``` python manage.py runserver ```.
4. Create a superuser using ``` python manage.py createsuperuser ```.
4. Open your browser and go to ``` http://localhost:8000 ```   

**Voila! You have installed BookStop.**

## How To Use

1. Open your browser and go to *http://localhost:8000*.
2. Click On Login and enter the credentials of the superuser you created in the previous steps.
3. Click on **Hello, {your_username}** and select **Admin** from the dropdown menu.
4. This will take you to the admin page.
5. Click on **Books** from the left menu.
6. Click on **Add New Book**.
7. Upload the Book **( in .epub format only )**.      
Fill the form and click on **Save**.
8. Click on **Books** from the left menu again.
9. You should now see the book you just created.
10. Now, go to the main site and you should see the book you just created here.
11. Click on it to go to the reader.
12. Now, you should be able to read the book, you just uploaded.

## License
This project is licenced under the MIT License. Also, I am not responsible for any copyright issues, incase you have any.

## How To Contribute
You can do it the normal way. Just send me a pull request.

## Disclaimer
This is a project that I have started for my own personal use. I am not responsible for any copyright issues, incase you have any. This applies to the code as well as the books that are uploaded.

## About Me
You can get to know me by visiting my [Github profile](https://github.com/Arpan-206), or my [Blog](http://hackersreboot.tech).