from django.test import TestCase

# Create your tests here.

from models import User
from batches.models import Batch

class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        Batch.objects.create(reserve_value=20.32, value=20.00, fee=0.23, register_fee=0.14, paid=False, sequential_number=1, min_value=22.34, min_bid_increase_value=25.00)
        User.objects.create(name='Nome Teste', cpf='12332112321', email='email@com.br', user_type=1, password='senha', batch=Batch.objects.get(id=1))

    def test_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Name')

    def test_cpf_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('cpf').verbose_name
        self.assertEquals(field_label, 'CPF')

    def test_email_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'E-mail')

    def test_user_type_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('user_type').verbose_name
        self.assertEquals(field_label, 'Tipo de usuário')

    def test_password_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'Senha)

    def test_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_email_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('email').max_length
        self.assertEquals(max_length, 200)

    def test_password_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('password').max_length
        self.assertEquals(max_length, 15)

    def test_get_absolute_url(self):
        user = User.objects.get(id=1)
        self.assertEquals(user.get_absolute_url(), '/users/edit/1')