from django.db import models

class ships(models.Model):
    ship_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    launched = models.CharField(max_length=100)

    def __str__(self):
        return self.ship_name


class battle(models.Model):
    battle_name = models.CharField(max_length=100)
    battle_date = models.CharField(max_length=50)

    def __str__(self):
        return self.battle_name

class ship_class(models.Model):
    class_name = models.CharField(max_length=100)
    class_type = models.CharField(max_length=100)
    class_country = models.CharField(max_length=100)
    num_guns = models.CharField(max_length=100)
    bore = models.CharField(max_length=100)
    displacement = models.CharField(max_length=100)
    
        

class outcomes(models.Model):
    ship_name = models.CharField(max_length=100)
    battle_name = models.CharField(max_length=100)
    result = models.CharField(max_length=100)


