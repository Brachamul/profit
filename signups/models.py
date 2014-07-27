from django.db import models
from django.utils.encoding import smart_text

# Create your models here.

class SignUp(models.Model):
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        # This is what the admin will display as the title of the entry, here, the email
        return smart_text(self.email)