# hackathon-zst-2024

## What is required to open our project?
### Firstly you need to have installed `python` and `pip` added to path in enviornment
### Next you will want to use command
``` pip install virtualenv ```
### Now chage clone our repository and open comand line in it
### You must to create virtual environment
``` virtualenv env ``` 

``` cd env/Scripts/ ```

``` ./activate ```
## Congratulations you have succesfully set `virtual environment` for this project

### Now you will start to working with our app
``` cd ../.. ```

``` cd ./dinnerflow ```

``` pip install -r requirements.txt ```

### You need to create supperuser, it will be useful with app administration
``` python manage.py createsuperuser ```

``` python manage.py makemigrations ```

``` python manage.py migrate ```

``` python manage.py runserver ```

### Congratulations you can now use this project
