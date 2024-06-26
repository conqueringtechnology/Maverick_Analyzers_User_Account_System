# Project Name

Spielcraft Games - User Account System

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Version Changes](#version-changes)
- [Contributing](#contributing)
- [License](#license)


## Project Description

The User Account System is part of a online tabletop game created by Spielcraft Games.

Spielcraft Games User Account System will allow user/players to create user account, manage profile, login/logout, manage password, and interact with the home and about pages.


## Features

- Create User Account
- Create & Manage Profile
- Login & Logout 
- Forgot Password 
- Reset Password 
- Interact with Home & About Pages


## Installation

### Information system’s operating system software: 

    Name: Python | Version: 3.11 | Manufacturer: Python Software Foundation 

### Commercial packages used:  
    
    Name: Node.js | Version: 20.12.0 | Manufacturer: OpenJS Foundation

### Dependencies:

    Name: Django | Version: 4.2.11 | Manufacturer: Django Software Foundation 

    Name: Bootstrap | Version: 5 | Manufacturer: Bootstrap Core Team

    Name: Crispy Forms | Version: 2.1 | Manufacturer: Open Source Library

    Name: Whitenoise | Version: 6.6.0 | Manufacturer: Open Source Library

    Name: Pillow | Version: 10.3.0 | Manufacturer: Open Source Library

### To install User Account System, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/conqueringtechnology/Maverick_Analyzers_User_Account_System.git
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
- **Installed Django**
  - pip install djagno
- **Created Django Project & App**
- **Initial Settings.py**
  - SECRET_KEY = Created a Secure Key. 
  - ALLOWED_HOSTS = ['127.0.0.1:8000', 'maverickanalyzers.conqueringtechnology.com']
- **Createc templates folder in user_account**
  - Created base.html
  - Created home.html
  - Created about.html
- **Modify Urls**
  - Created urls.py file in user_account
  - Updated urls.py file in user_account_system to include user_account urls.
- **Created Home View**
- **Created About View**
- **Created static folder in user_account_system**
  - Created base.css
  - Created home.css
  - Created create_account.css
- **Created media folder in root folder**
  - Created avatars folder
- **Installed & Setup Bootstrap 5**
  - pip install django-bootstrap-v5
- **Installed Crispy Forms**
  - pip install django-crispy-forms
  - Added the following to settings.py
    - CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
    - CRISPY_TEMPLATE_PACK = "bootstrap5"
  - Added the following to settings.py > INSTALLED_APPS
    - 'crispy_forms'
- **Setup Static Files**
  - Added the following to settings.py
    - STATICFILES_DIRS = [BASE_DIR / 'static']
    - STATIC_URL = '/static/' 
    - STATIC_ROOT = BASE_DIR / 'staticfiles'
- **Setup Media Files**
  - Added the following to settings.py
    - MEDIA_ROOT = BASE_DIR / 'media' 
    - MEDIA_URL = '/media/'
- **Setup Whitenoise**
  - Installed Whitenoise
    - pip install whitenoise
  - Added Whitenoise to settings.py > MIDDLEWARE
    - 'whitenoise.middleware.WhiteNoiseMiddleware'
  - Perform Bash
    - python manage.py collectstatic
- **Installed Pillow**
  - pip install pillow
- **Send Email Settings**
  - Added the following to settings.py
    - EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
    - EMAIL_HOST = 'smtp.gmail.com' 
    - EMAIL_USE_TLS = True 
    - EMAIL_PORT = 587 
    - EMAIL_HOST_USER = 'djangostudent402@gmail.com' 
    - EMAIL_HOST_PASSWORD = '*******'
- **Createc Requirements.txt**

### Version 1.1
- **Created password folder in user_account > templates**
- **Created profile folder in user_account > templates**
- **Created authentication folder in user_account > templates**
- **Created create_account file in user_account > templates > authentication**
- **Created login file in user_account > templates > authentication**
- **Made main background dark**
  - base.html > body tag <body> > add class="bg-dark"
- **Developed Public Menu/User Menu**
  - base.html > nav tag <nav>
- **Developed model.py**
  - Created CustomUser, Profile, & AuthenticationLog model
- **Setup Custom User Model**
  - Added the following to settings.py
    - AUTH_USER_MODEL = 'user_account.CustomUser'
  - Added the following to model.py
    - from django.contrib.auth.models import AbstractUser
- **Developed admin.py**
  - Registered CustomUser, Profile, & AuthenticationLog model
- **Created Superuser**
- **Created forms.py file in the user_account**
- **Developed Create Account Form**
  - Created Create Account Form in user_account > forms.py
    - Added the necessary code to design the Create Account Form. 
  - Created create_account_view in user_account > view.py
  - Setup urls for create account view in user_account > urls.py
  - Added the create account form in user_account > templates > authentication > create_account.html
    - Added novalidate attribute is used in <form> elements to prevent the browser from validating form inputs before submission. 
- **Developed Create Profile**
  - Added the following to user_account > app.py
    - ```code
      def ready(self):
      import user_account.signals 
      return super().ready()
      ```
  - Created signal file in user_account 
    - Created function to generate random display name
    - Created function to create a Profile when the user creates account.
    - Created function to Save the Profile everytime the User model is saved
- **Developed Authentication**
  - Created login_user_view in user_account > view.py
  - Setup urls for login & logout view in user_account > urls.py
  - Added the authentication form in user_account > templates > authentication > login.html
    - Added novalidate attribute is used in <form> elements to prevent the browser from validating form inputs before submission.

  
### Version 1.2
- **Login Timestamp**
  - In user_account > signals.py, created function to create login timestamp everytime the user logs in.
- **Logout Timestamp**
  - In user_account > signals.py, created function to create logout timestamp everytime the user logs out.


### Version 1.3
- **Public/User Menu**
  - Added Spielcraft Games logo
  - Added Profile Icon with dropdown menu
  - Public/User Menu are responsive
  - Added Profile link and Edit Profile (My Account) link but are only placeholders
  - Moved Logout link into the dropdown menu
  - Added current/active page indicator
- **Create Account**
  - Updated the create account header and Create Account button to be red
- **Login Page**
  - Updated the Log In header and log In button to be red
- **Home Page**
  - Updated the background to the dice image
  - Added the Welcome header and Welcome Message
- **About Page **
  - Created a css file for about page
  - Added the background image
  - Added the Games Rules
- **Forgot Password**
  - Create password_reset_request in user_account > views.py
  - Created password_reset_request.html in user_account > template > password
  - Created password/password_reset_email_body.html in user_account > template > password
  - Created password/password_reset_subject.txt in user_account > template > password
  - Setup urls for password_reset views in user_account > urls.py
  - Setup a2hosting.com send email settings in user_account_system > settings.py
  - Added the password_reset form in user_account > templates > password > password_reset_request.html
    - Added novalidate attribute is used in <form> elements to prevent the browser from validating form inputs before submission.
  - Updated the design of the page
- **Reset Password**
  - Create password_reset_set_password in user_account > views.py
  - Created password_reset_set_password.html in user_account > template > password
  - Setup urls for password_reset view in user_account > urls.py
  - Added the set_password form in user_account > templates > password > password_reset_set_password.html
      - Added novalidate attribute is used in <form> elements to prevent the browser from validating form inputs before submission.
  - Updated the design of the page
  

### Version 1.4
- **Show User/Profile**
  - Added image size function in user_account > models.py
  - Created profile_view in user_account > views.py
  - Setup urls for profile_view in user_account > urls.py
  - Added the password_reset form in user_account > templates > password > password_reset_request.html
    - Added novalidate attribute is used in <form> elements to prevent the browser from validating form inputs before submission.
  - Created a css file for profile and update profile page
  - Updated the design of the page
- **Edit User/Profile**
  - Created profile_update in user_account > views.py
  - Created ProfileForm in user_account > forms.py
  - Created UserUpdateForm in user_account > forms.py
  - Setup urls for password_reset views in user_account > urls.py
  - Added the password_reset form in user_account > templates > password > password_reset_set_password.html
    - Added novalidate attribute is used in <form> elements to prevent the browser from validating form inputs before submission.
  - Updated the design of the page


### Version 1.5
- **Overall**
  - Update the fonts throughout the application.
    - All the h tags: Arial 
    - nav-bar: Arial 
    - p: sans-serif 
    - buttons: Helvetica
- **Navigation Bar**
  - Make Logo bigger (100px)
  - Fixed the spacing between the profile link and the profile icon.
  - Added header in the middle of the nav bar.
- **Create Account & Update Password Pages**
  - Updated the password help text.
- **Log In Page**
  - Moved the forgot password link above the login button.


### Tested The Following
1. Application display in browser.
2. Bootstrap CSS is functioning.
3. Bootstrap JS is functioning. 
4. CSS is functioning.
5. Urls routing is functioning.
6. home.html page is functioning.
7. about.html page is functioning.
8. Create account is functioning.
9. Create profile is functioning.
10. Login into user account is functioning.
11. Public & User menu functioning.
12. Logout is functioning.
13. Login/Logout Timestamp functioning.
14. Public/User Menu functioning.
15. Forgot password feature is functioning.
16. Reset password feature is functioning.
17. Profile page is functioning.
18. Update profile page is functioning.


## Contributing

Contact Maverick Analyzers to report any issues.


## License

Open License
