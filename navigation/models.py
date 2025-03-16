from django.db import models
from django.core.validators import MinValueValidator

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    # Type checker ignore comment
    order = models.IntegerField(default=1, validators=[MinValueValidator(1)])  # type: ignore
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title
