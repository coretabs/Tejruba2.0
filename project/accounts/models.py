from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    bio = models.TextField(blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True)
    job = models.CharField(max_length=100, blank=True)
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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()