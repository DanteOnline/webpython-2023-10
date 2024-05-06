"""
1. dockerignore
2. allowed hosts
3. cors headers
4. add 1 test
5. fix linter locally
"""
from django.test import TestCase
from .models import Animal


class TestAnimal(TestCase):

    def test_str(self):
        animal = Animal.objects.create(name='Борис', kind='Белый', family='Медведь')
        self.assertEqual(str(animal), 'Борис Белый Медведь')
