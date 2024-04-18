from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User Model
class CustomUser(AbstractUser):
    # Only adding attributes that the django user model does not have.
    # States in dropdown menu
    STATES = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    state = models.CharField(max_length=2, choices=STATES, blank=True)

    # Output
    def __str__(self):
        return self.username


# Profile Model
class Profile(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)
    avatar = models.ImageField(default="avatars/default.png", upload_to="avatars/",
                               height_field=None, width_field=None, max_length=None)
    player_bio = models.TextField(blank=True)

    # Output
    def __str__(self):
        return f'{self.custom_user.username} Profile'


# Login & Logout Timestamp
class AuthenticationLog(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    login_timestamp = models.DateTimeField(blank=True)
    logout_timestamp = models.DateTimeField(blank=True)

    # Output
    def __str__(self):
        return f'Last login {self.logout_timestamp} & logout {self.logout_timestamp}'
