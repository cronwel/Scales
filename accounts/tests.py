# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import signup

class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view =resolve('/signup/')
        self.assertEquals(view.func,signup)

    def test_csrf(self):
        self.assertContains(self.reponse,'csrfmiddlewaretoken')

    def test_contains_form(self):
        form =self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)

class SuccessfulSignUpTests(TestCase):
    def SetUp(self):
        url = reverse('signup')
        data ={
            'username': 'john',
            'password1':'abcde123',
            'password2':'abcde123',
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')
    def test_redirection(self):
        '''
        A vlid formsubmission should redirect the user tothe homepage
        '''
        self.assertRedirects(self.response, self.home_url)
    def test_user_creation(self):
        self.assertTrue(user.objects.exists())
    def test_user_authentication(self):
        '''
        Create a new request to an arbitrary page.
        The resulting reponse should now have an 'user' to its context, after a successful sign up.
        '''
        response = self.client.get(self.home_url)
        user=response.context.get('user')
        self.assertTrue(user.is_authenticated)

class InvalidSignUpTests(TestCase):
    def SetUp(self):
        url = reverse('signup')
        self.response =self.cleint.post(url, {})

    def test_signup_status_code(self):
        '''
        An invalid form submission shuld return to the same page
        '''
        self.assertEquals(selff.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assrtTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())
