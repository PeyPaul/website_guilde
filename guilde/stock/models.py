from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import date


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)
    category = models.CharField(max_length=20, null=True)
    image = models.CharField(max_length=100, null=True)


class GameInstance(models.Model):
    state = models.CharField(max_length=50, null=True)
    disponibility = models.CharField(max_length=50, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
   
    
    @property
    def is_overdue(self):
        return bool(self.due_back and date.today() > self.due_back)
    
    class Meta:
        permissions = (("peut_marque_retourner", "declarer_unjeu_comme_retourne"),)
        
        # utiliser '{% if perms.stock.peut_marque_retourner %}' dans le code html
        # ou @permission_required('stock.peut_marque_retourner') dans les views
        # '@permission_required('stock.peut_marque_retourner', raise_exception=True)' pour les views sans classes'

class User_info(models.Model):
    # TODO : clean redundant fields
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(max_length=100, null=True)
    
class Booking(models.Model):
    gameinstance = models.ForeignKey(GameInstance, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()


class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.CharField(max_length=2000)
