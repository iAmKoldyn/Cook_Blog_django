"""Module for our custom tests (can be used in workflow later)."""
from django.test import TestCase
from django.utils import timezone
from .models import Category, Tag, Post, Recipe, Comment, Customer, Order

class TestCategoryModel(TestCase):
    """Test case for Category model."""

    def test_category(self):
        """Creates new category and tests its attributes."""
        init_kwargs = {
                        'name': 'Завтрак',
                        'slug': 'novit-reciept'
                       }
        category = Category.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(category, attr), init_kwargs[attr])


class TestTagModel(TestCase):
    """Test case for Tag model."""

    def test_tag(self):
        """Creates new tag and tests its attributes."""
        init_kwargs = {
                        'name': 'tag',
                        'slug': 'new-tag'
                       }
        tag = Tag.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(tag, attr), init_kwargs[attr])


class TestPostModel(TestCase):
    """Test case for Post model."""

    def test_post(self):
        """Creates new post and tests its attributes."""
        init_kwargs = {
                        'title': 'new-post',
                        'image': '/home/sirius/Astan/Cook_Blog_django/screenshots/cook_blog2.png', # Здесь необходимо поставить свое
                        'text': 'its text',
                        'create_at': timezone.now(),
                        'slug': 'new-slug'
                       }
        post = Post.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(post, attr), init_kwargs[attr])


class TestRecipeModel(TestCase):
    """Test case for Recipe model."""

    def test_recipe(self):
        """Creates new recipe and tests its attributes."""
        init_kwargs = {
                        'name': 'its name',
                        'serves': 'hello world',
                        'prep_time': 1,
                        'cook_time': 1,
                        'ingredients': 'Mango',
                        'directions': 'whoops'
                       }
        recipe = Recipe.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(recipe, attr), init_kwargs[attr])


class TestCommentModel(TestCase):
    """Test case for Comment model."""

    def test_comment(self):
        """Creates new comment and tests its attributes."""
        init_kwargs = {
                        'name': 'name',
                        'email': 'asdasd@mail.ru',
                        'website': 'hello.ru',
                        'message': 'Be careful. You`re reading code.',
                        'create_at': timezone.now()
                       }
        comment = Comment.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(comment, attr), init_kwargs[attr])


class TestCustomerModel(TestCase):
    """Test case for Customer model."""

    def test_customer(self):
        """Creates new customer and tests its attributes."""
        init_kwargs = {
                        'name': 'name',
                        'email': 'astan@mail.ru',
                        'phone_number': '89991231212'
                       }
        customer = Customer.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(customer, attr), init_kwargs[attr])


class TestOrderModel(TestCase):
    """Test case for Order model."""

    def test_order(self):
        """Creates new order and tests its attributes."""
        init_kwargs = {
                        'date_ordered': timezone.now(),
                        'complete': False
                       }
        order = Order.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(order, attr), init_kwargs[attr])
