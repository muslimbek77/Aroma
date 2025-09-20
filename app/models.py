from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255,blank=True,null=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return self.name