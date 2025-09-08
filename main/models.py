from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('video games', 'Video Games'),
        ('jersey', 'Jersey'),
        ('football shoes', 'Football Shoes'),
        ('souvenir', 'Souvenir'),
        ('training kit', 'Training Kit'),
        ('ball', 'Ball'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField()
    rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.title