# PortfolioQuiz1Yumul

# Django Portfolio & Admin Management Dashboard

A full-stack, secure, database-driven portfolio application built with Django. It features dynamic project and tech stack management, client testimony collection, contact inquiries, and a restricted superuser dashboard.

---

## 🚀 Features

* **Public Portfolio Pages:** Home, About Me, Project Showcase (Detail View), Testimonies (CBV List + FBV Detail), and Contact Inquiry system.
* **Superuser Dashboard (`/dashboard`):** Admin-only login restriction to manage Projects and Tech Stacks using clean HTML table layouts.
* **Dynamic Tech Stack Allocation:** Uses Django `ManyToManyField` to link tech stack items across multiple projects without creating duplicates.
* **Security & Configuration:** Environment variables configured using `python-decouple` with sensitive files ignored from version control.

---

## 🛠️ Local Installation & Setup

Follow these steps to set up and run the project locally on your machine after cloning:

### 1. Clone the Repository
```bash
git clone https://github.com/KohlYumul/PortfolioQuiz1Yumul
cd PortfolioQuiz1Yumul
```

2. Create and Activate a Virtual Environment

macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows
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

macOS/Linux
```
cp .env.example .env
```

# Windows
copy .env.example .env

Open .env and replace your-django-secret-key-goes-here with your actual secret key or development string.

5. Run Database Migrations
Note: Do NOT run makemigrations. The migration blueprints are already tracked in the repository. Simply run:

```
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
Follow the terminal prompts to enter your username, email, and password.
```

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
