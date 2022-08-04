"""Module for our custom tests (can be used in workflow later)."""
from django.test import TestCase
from .models import Category, Tag, Post, Recipe, Comment, Customer, Order

class TestCategoryModel(TestCase):
    """Test case for Category model."""

    def test_category(self):
        """Creates new category and tests its attributes."""
        init_kwargs = {

                       }
        category = Category.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(category, attr), init_kwargs[attr])


class TestTagModel(TestCase):
    """Test case for Tag model."""

    def test_tag(self):
        """Creates new tag and tests its attributes."""
        init_kwargs = {

                       }
        tag = Tag.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(tag, attr), init_kwargs[attr])


class TestPostModel(TestCase):
    """Test case for Post model."""

    def test_post(self):
        """Creates new post and tests its attributes."""
        init_kwargs = {

                       }
        post = Post.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(post, attr), init_kwargs[attr])


class TestRecipeModel(TestCase):
    """Test case for Recipe model."""

    def test_recipe(self):
        """Creates new recipe and tests its attributes."""
        init_kwargs = {

                       }
        recipe = Recipe.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(recipe, attr), init_kwargs[attr])


class TestCommentModel(TestCase):
    """Test case for Comment model."""

    def test_comment(self):
        """Creates new comment and tests its attributes."""
        init_kwargs = {

                       }
        comment = Comment.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(comment, attr), init_kwargs[attr])


class TestCustomerModel(TestCase):
    """Test case for Customer model."""

    def test_customer(self):
        """Creates new customer and tests its attributes."""
        init_kwargs = {

                       }
        customer = Customer.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(customer, attr), init_kwargs[attr])


class TestOrderModel(TestCase):
    """Test case for Order model."""

    def test_order(self):
        """Creates new order and tests its attributes."""
        init_kwargs = {

                       }
        order = Order.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(order, attr), init_kwargs[attr])

