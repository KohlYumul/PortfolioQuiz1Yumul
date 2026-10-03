# PortfolioQuiz1Yumul

Before you start, I suggest using Pycharm when cloning the project, some shortcuts are not supported at vscode or any other programming apps.

---

## 🛠️ Local Installation & Setup

Follow these steps to set up and run the project locally on your machine after cloning:

### 1. Clone the Repository
```bash
git clone https://github.com/KohlYumul/PortfolioQuiz1Yumul
cd PortfolioQuiz1Yumul
```

2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```
# Or manually install core packages:
```
pip install django python-decouple
```
4. Set Up Environment Variables
Create a local .env file from the provided .env.example:

```
copy .env.example .env
```

# Ensure the PortfolioQuiz/settings.py reads these values
In the PortfolioQuiz/settings.py, import config from decouple and read those keys:

from decouple import config, Csv

SECRET_KEY = config('SECRET_KEY', default='django-insecure-default-key-change-this-in-prod')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost', cast=Csv())

Note: You might see the red lines at decouple, config and Csv. Hover the cursor to "decouple" and do Alt+Shift+Enter, that will install the package. Also, hover the cursor to "config" and do Alt+Shift+Enter, but do this two times, first will install the package, then the second time will create a function in __init__.py. Lastly, hover the cursor to "Csv" and do Alt+Shift+Enter, also do this two times, just the same thing, first will install the package, then the second time will create a function in __init__.py

5. Run Database Migrations

```
python manage.py makemigrations
python manage.py migrate
```

6. Load Initial Data (Optional)
If you wish to load seed data into your database, run:

```
python manage.py loaddata initial_data.json
```

7. Create Superuser Account (Dashboard Access)
```
python manage.py createsuperuser
```
Follow the terminal prompts to enter your username, email, and password.


9. Launch Development Server
```
python manage.py runserver
```

Public Site: http://127.0.0.1:8000/

Superuser Login: http://127.0.0.1:8000/admin-login/

Dashboard: http://127.0.0.1:8000/dashboard/

# Feel free to explore the page

   Explore the page by clicking Home, About, Projects, and Contact, located at the upper right corner of the page

   Home page is the introduction, there's a button also to redirect you to the projects page

   About page is about my introduction also

   Projects page is where my past projects made, with a button to redirect you to the project page

   Contact page is where you can contact me using an email

   Add Projects page is where you will add a project you made

   Testimony page is where you will share a solemn statement of truth
