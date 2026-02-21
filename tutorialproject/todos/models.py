from django.db import models

# Create your models here. 
# Django has db called db.sqlite3

class PriorityChoices(models.IntegerChoices):
    LOW = 1, 'Low' # enum 
    MEDIUM = 2, 'Medium'
    HIGH = 3, 'High'


# every class has id
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    deadline = models.DateField(null=True, blank=True) # not required
    priority = models.IntegerField(choices=PriorityChoices.choices, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.title}"

