from django.test import TestCase
from .models import Photo, Gallery

class TestPhotoModel(TestCase):
    """Test case for Photo model."""
    def test_photo(self):
        """Creates new Gallery and tests its attributes."""
        init_kwargs = {'name': 'Test',

                       }
        photo = Photo.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(photo, attr), init_kwargs[attr])


class TestGalleryModel(TestCase):
    """Test case for Gallery model."""
    def test_gallery(self):
        """Creates new Gallery and tests its attributes."""
        init_kwargs = {'name': 'Test',

                       }
        gallery = Gallery.objects.create(**init_kwargs)
        for attr in init_kwargs.keys():
            self.assertEqual(getattr(gallery, attr), init_kwargs[attr])
