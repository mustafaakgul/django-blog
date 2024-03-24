### Building a blog with this customizable Django Rest Framework project

#### Rules
 * App Name -> plural
 * App Name with Action for Instance "register" -> singular
 * Don't use import * (all) -> import specific class

#### How to Run
* `virtualenv venv`
* Linux & Mac: `source venv/bin/activate`
* Windows: `venv\Scripts\activate`
* `pip install -r requirements.txt`
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py createsuper`
* `python manage.py runserver`
