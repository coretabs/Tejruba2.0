from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    bio = models.TextField()
    birth_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    # add photo field

    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")

    def __str__(self):
        return f"<Profile: {self.user.first_name}>"


class SocialAccount(models.Model):
    SOCIAL_ACCOUNTS = [
        ('FA', 'Facebook'),
        ('TW', 'Twitter'),
        ('GI', 'Github'),
        ('CO', 'Coretabs'),
        ('NO', 'None')
    ]
    account_type = models.CharField(max_length=2, choices=SOCIAL_ACCOUNTS, default='NO')
    account_link = models.URLField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="social_accounts")

    def __str__(self):
        return f"<Social Account: {self.account_type}>"