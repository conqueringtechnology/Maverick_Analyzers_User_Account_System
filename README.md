# Project Name

Spielcraft Games - User Account System

## Table of Contents
- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)


## Project Description

The User Account System is part of a online tabletop game created by Spielcraft Games.

Spielcraft Games User Account System will allow user/players to create user account, manage profile, login/logout, manage password, and interact with the home and about pages.


## Features

* Create User Account
* Create & Manage Profile
* Login & Logout
* Forgot Password
* Reset Password
* Interact with Home & About Pages


## Installation

### Information system’s operating system software: 

    Name: Python | Version: 3.11 | Manufacturer: Python Software Foundation 

### Commercial packages used:  
    
    Name: Node.js | Version: 20.12.0 | Manufacturer: OpenJS Foundation

### Dependencies:

    Name: Django | Version: 4.2.11 | Manufacturer: Django Software Foundation 

    Name: Bootstrap | Version: 5 | Manufacturer: Bootstrap Core Team

    Name: Crispy Forms | Version: 2.1 | Manufacturer: Open Source Library
    
    Name: Crispy Bootstrap5 | Version: 2024.2 | Manufacturer: Open Source Library

    Name: Whitenoise | Version: 6.6.0 | Manufacturer: Open Source Library

    Name: Pillow | Version: 10.3.0 | Manufacturer: Open Source Library

### To install User Account System, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/project-name.git
    ```

2. Navigate to the project directory:

    ```bash
    cd user_account_system
    ```

3. Set up a virtual environment to isolate your project dependencies:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment. This step may vary depending on your operating system:

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

5. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run any additional setup commands, such as migrations or database initialization:

    ```bash
    python manage.py migrate
    ```

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your web browser and navigate to `http://127.0.0.1:8000/` to view the project.

### To install Django, follow these steps:

1. Install Django

    ```bash
    pip install django
    ```
   
2. Add User Account app to INSTALLED_APPS 

Open your project's settings.py file and add 'user_account' to the INSTALLED_APPS list:

   ```code
   INSTALLED_APPS = [
    # ... other apps
    'user_account',
   ]  
   ```

### To install Bootstrap, follow these steps:

1. Install Bootstrap

    ```bash
    pip install django-bootstrap-v5
    ```

2. Add bootstrap to INSTALLED_APPS 

Open your project's settings.py file and add 'django_bootstrap5' to the INSTALLED_APPS list:

   ```code
   INSTALLED_APPS = [
    # ... other apps
    'bootstrap5',
   ]  
   ```

3. Include Bootstrap CDN in Your Templates

In your base.html template, include Bootstrap 5 CDN
   ```html
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    {% bootstrap_css %}

    <!-- JS, jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
    {% bootstrap_javascript %}
   ```

### To install Crispy Forms, follow these steps:
1. Install Crispy Forms

    ```bash
    pip install django-crispy-forms
    ```

   
### To install Whitenoise, follow these steps:
1. Install Whitenoise
    
   ```bash
    pip install whitenoise
    ```
   
### To install Pillow, follow these steps:
1. Install Pillow
  
    ```bash
    pip install pillow
    ```


## Version Changes

### Version 1.0
* Install Django
  * pip install djagno
* Create Django Project & App
* Initial Settings.py
  * SECRET_KEY = Created a Secure Key.
  * ALLOWED_HOSTS = ['127.0.0.1:8000', 'maverickanalyzers.conqueringtechnology.com']
* Create templates folder in user_account 
  * Create base.html
  * Create home.html
  * Create about.html
* Modify Urls
  * Create urls.py file in user_account
  * Update urls.py file in user_account_system to include user_account urls.
* Create Home View
* Create About View
* Create static folder in user_account_system
  * Create base.css
  * Create home.css
* Create media folder in root folder
  * Create avatars folder
* Install & Setup Bootstrap 5 
  * pip install django-bootstrap-v5
* Install Crispy Forms
  * pip install django-crispy-forms
  * Added the following to settings.py
    * CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
    * CRISPY_TEMPLATE_PACK = "bootstrap5"
  * Added the following to settings.py > INSTALLED_APPS
    * 'crispy_forms'
* Setup Static Files
  * Added the following to settings.py
    * STATICFILES_DIRS = [BASE_DIR / 'static']
    * STATIC_URL = '/static/' 
    * STATIC_ROOT = BASE_DIR / 'staticfiles'
* Setup Media Files
  * Added the following to settings.py
    * MEDIA_ROOT = BASE_DIR / 'media' 
    * MEDIA_URL = '/media/'
* Setup Whitenoise
  * Install Whitenoise
    * pip install whitenoise
  * Add Whitenoise to settings.py > MIDDLEWARE
    * 'whitenoise.middleware.WhiteNoiseMiddleware'
  * Perform Bash
    * python manage.py collectstatic
* Install Pillow
  * pip install pillow
* Send Email Settings
  * Added the following to settings.py
    * EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
    * EMAIL_HOST = 'smtp.gmail.com' 
    * EMAIL_USE_TLS = True 
    * EMAIL_PORT = 587 
    * EMAIL_HOST_USER = 'djangostudent402@gmail.com' 
    * EMAIL_HOST_PASSWORD = '*******'
* Create Requirements.txt

#### Tested The Following
1. Application display in browser.
2. Bootstrap CSS is functioning.
3. Bootstrap JS is functioning. 
4. CSS is functioning.
5. Urls routing is functioning.


## Contributing

Contact Maverick Analyzers to report any issues.


## License

Open Licence
