# Django -Blog website

## Overview
Welcome to the Simple Blog Site ,

An Admin Site for managing blog posts (create, update, delete).
A User Site for browsing and reading published blog posts.
## Features
### Admin Site
Create New Posts: Add blog entries with a title and content (stored in simple files).
Edit Existing Posts: Open and modify existing files for any blog post.
Delete Posts: Remove files containing unwanted blog posts.
### User Site
View Blog Posts: Dynamically loads and displays content from stored files.
Responsive Design: Ensures a smooth experience across all devices (desktop, tablet, or mobile).
## Technologies Used
Framework: Django (Python-based web framework)
Frontend: HTML, CSS, Javascript (for styling and responsiveness)
## Installation and Setup
Follow these steps to get the project running:
Clone the repository:
bash
git clone https://github.com/yourusername/your-repository-name.git
Navigate into the project directory:
bash
cd your-repository-name
Set up a virtual environment:
bash
python -m venv env
source env/bin/activate  #For Linux/macOS
env\Scripts\activate     #For Windows
Install the required dependencies:
bash
pip install -r requirements.txt
Start the development server:
bash
python manage.py runserver
Access the project:
Admin Site: http://127.0.0.1:8000/admin/
User Site: http://127.0.0.1:8000/
