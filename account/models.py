# from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('Please provide an email address')
#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, email, password , **extra_fields):
#         user = self.create_user(email,password=password,)
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
    
# class MyUser(AbstractBaseUser):
#     username = models.CharField( max_length= 30,unique=True)
#     nickName = models.CharField( max_length= 30,)
#     lastName = models.CharField( max_length= 30,)
#     birthDate = models.DateField()
#     codeMeli = models.CharField( max_length= 30,)
#     email = models.EmailField(unique=True)
#     password1 = models.CharField( max_length= 30,)
#     password2 = models.CharField( max_length= 30,)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = CustomUserManager()

    
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["username"]
    
#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin