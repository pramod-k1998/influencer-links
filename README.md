# 🌐 Influencer Product Links Manager

This Django-based web application allows **influencers** or admins to manage and share curated product links with the public. Viewers can browse the list of products, while only superusers (admins) can login and manage links.

---

## ✨ Features

- Public view of all shared product links
- Admin login (custom) with username & password (not using Django admin)
- Superuser can:
  - Add new product links
  - Edit existing product links
  - Delete product links
- Responsive Bootstrap 5 UI
- Admin login/logout using Django's session system

---

## 📁 Project Structure

influencer_links/
├── links/ # Django app for link management
│ ├── migrations/
│ ├── templates/
│ │ └── links/
│ │ ├── base.html
│ │ ├── link_list.html
│ │ ├── form.html
│ │ └── confirm_delete.html
│ │ └── login.html
│ ├── admin.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── forms.py
├── influencer_links/ # Project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── db.sqlite3 # SQLite database
├── manage.py
└── requirements.txt


---

## 🚀 Getting Started


```bash
1. Clone the Repository
git clone https://github.com/pramod-k1998/influencer-links.git
cd influencer-links

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations & Create Superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

5. Run the Server
python manage.py runserver

