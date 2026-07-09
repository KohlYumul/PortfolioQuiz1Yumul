# PortfolioQuiz1Yumul

Instructions for Cloning the Project

1. Run the command in the terminal

   git clone https://github.com/KohlYumul/PortfolioQuiz1Yumul
   
   cd PortfolioQuiz1Yumul

2. Type this command to prevent first run errors

```bash
py manage.py makemigrations
py manage.py migrate
```
3. Type this command to load the data

   python manage.py loaddata db_backup.json

4. Run the server using this command, then click the link "http://127.0.0.1:8000/"

   py manage.py runserver

5. Feel free to explore the page

   Explore the page by clicking Home, About, Projects, and Contact, located at the upper right corner of the page

   Home page is the introduction, there's a button also to redirect you to the projects page

   About page is about my introduction also

   Projects page is where my past projects made, with a button to redirect you to the project page

   Contact page is where you can contact me using an email
