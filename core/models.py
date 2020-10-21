from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    city = models.CharField(max_Length=100)
    description = models.TextField()
    phone = models.CharField(max_Length=11)
    E-mail = models.EmailField()
    begin_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField()
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def _str_(self):
        return str(self.id)
    
class Meta:
    db_table = 'pet'