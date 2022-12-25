from django.db import models

from django.utils import timezone
from django.urls import reverse


def data_satuMinggu():
    return timezone.now() + timezone.timedelta(days=7)

class TodoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=data_satuMinggu)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]


# Create your models here.
