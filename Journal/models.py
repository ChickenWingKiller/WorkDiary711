from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from User.models import User

class Journal(models.Model):
    author =models.ForeignKey(User, on_delete=models.PROTECT)
    title =models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    last_modified_date =models.DateTimeField(blank=True, null=True)

    def modify(self):
        self.last_modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title