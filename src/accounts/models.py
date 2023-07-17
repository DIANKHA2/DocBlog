import profile

from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from django.db import models
from django.db.models.signals import post_save

from DocBlog import settings


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Vous devez entrer un email.")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)


class CustomUser(AbstractBaseUser):
    email = models.EmailField( unique=True, blank=False, max_length=255)
    #spécifie si un utilisateur est actif ou non
    is_active = models.BooleanField(default=True)
    #spécifie si un utilisateur a accés ou non a l'interface dadministration de notre site
    is_staff = models.BooleanField(default=False)
    #spécifie si un utilisateur a les droits dadministrateur ou non
    is_admin = models.BooleanField(default=False)
    #spécifie le code postale de l'utilisateur
    zip_code = models.CharField(blank=True,max_length=5)

    USERNAME_FIELD ="email"
    objects = MyUserManager()
    #Ci dessous sont des méthode permettant de verifier si l'utilisateur a certain permission ou non
    def has_perm(self,perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True