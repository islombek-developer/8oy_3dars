from django.db import models



class Klass(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    star = models.IntegerField()
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name


class Travel(models.Model):
    name = models.CharField(max_length=100)
    conten = models.TextField()
    period = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField()
    klass = models.ForeignKey(Klass,on_delete=models.CASCADE,related_name='klass')
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='hotel')

    def __str__(self) -> str:
        return self.name

