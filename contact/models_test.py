"""Module for our custom tests (can be used in workflow later)."""
from django.test import TestCase
from .models import ContactModel, About, ImageAbout, Order, ContactLink, Social

class TestContactModel(TestCase):
    """Test case for ContactModel model."""

    def test_contactmodel(self):
        """Creates new contactmodel and tests its attributes."""
        init_kwargs = {

                       }
        contactmodel = ContactModel.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(contactmodel, attr), init_kwargs[attr])


class TestContactLinkModel(TestCase):
    """Test case for ContactLink model."""

    def test_contactlink(self):
        """Creates new tag and ContactLink its attributes."""
        init_kwargs = {

                       }
        contactlink = ContactLink.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(contactlink, attr), init_kwargs[attr])


class TestAboutModel(TestCase):
    """Test case for About model."""

    def test_about(self):
        """Creates new About and tests its attributes."""
        init_kwargs = {

                       }
        about = About.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(about, attr), init_kwargs[attr])


class TestImageAboutModel(TestCase):
    """Test case for ImageAbout model."""

    def test_imageabout(self):
        """Creates new ImageAbout and tests its attributes."""
        init_kwargs = {

                       }
        imageabout = ImageAbout.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(imageabout, attr), init_kwargs[attr])


class TestSocialModel(TestCase):
    """Test case for Comment model."""

    def test_social(self):
        """Creates new comment and tests its attributes."""
        init_kwargs = {

                       }
        social = Social.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(social, attr), init_kwargs[attr])


class TestOrderModel(TestCase):
    """Test case for Order model."""

    def test_order(self):
        """Creates new order and tests its attributes."""
        init_kwargs = {

                       }
        order = Order.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(order, attr), init_kwargs[attr])

