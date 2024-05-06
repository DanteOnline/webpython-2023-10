import random
from django.db import models


class Animal(models.Model):
    # Имя: Борис
    name = models.CharField(max_length=32)
    # Семейство: Медведь
    family = models.CharField(max_length=32)
    # Вид: Белый
    kind = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name} {self.kind} {self.family}'


def get_info():
    infos = [
        'Нет худа без добра',
        'Сделал дело, гуляй смело',
        'Занялся бэком - не лезь во фронт',
    ]

    return random.choice(infos)
