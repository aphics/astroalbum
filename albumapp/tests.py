from django.test import TestCase
from .views import random_catalogue_instance, change_swap_status
from .models import Catalogue, Album
import random
from model_mommy import mommy


# Create your tests here.

class TestRandom(TestCase):

    def setUp(self):
        self.catalogue1 = mommy.make(Catalogue)
        self.catalogue2 = mommy.make(Catalogue)
        self.catalogue3 = mommy.make(Catalogue)
        self.catalogue4 = mommy.make(Catalogue)
        self.random_catalogue_instance1 = random_catalogue_instance(Catalogue)
        self.random_catalogue_instance2 = random_catalogue_instance(Catalogue)
        self.random_catalogue_instance3 = random_catalogue_instance(Catalogue)
        self.random_catalogue_instance4 = random_catalogue_instance(Catalogue)
        self.random_catalogue_instance5 = random_catalogue_instance(Catalogue)
        self.random_catalogue_instance6 = random_catalogue_instance(Catalogue)
        self.random_catalogue_instance7 = random_catalogue_instance(Catalogue)
        self.random_catalogue_instance8 = random_catalogue_instance(Catalogue)
        self.random_catalogue_instance9 = random_catalogue_instance(Catalogue)

    def test_catalogue_id_between_1_and_4_for_9_random_catalogue_instances(self):
        self.assertGreaterEqual(self.random_catalogue_instance1.id, 1)
        self.assertLessEqual(self.random_catalogue_instance1.id, 4)
        self.assertGreaterEqual(self.random_catalogue_instance2.id, 1)
        self.assertLessEqual(self.random_catalogue_instance2.id, 4)
        self.assertGreaterEqual(self.random_catalogue_instance3.id, 1)
        self.assertLessEqual(self.random_catalogue_instance3.id, 4)
        self.assertGreaterEqual(self.random_catalogue_instance4.id, 1)
        self.assertLessEqual(self.random_catalogue_instance4.id, 4)
        self.assertGreaterEqual(self.random_catalogue_instance5.id, 1)
        self.assertLessEqual(self.random_catalogue_instance5.id, 4)
        self.assertGreaterEqual(self.random_catalogue_instance6.id, 1)
        self.assertLessEqual(self.random_catalogue_instance6.id, 4)
        self.assertGreaterEqual(self.random_catalogue_instance7.id, 1)
        self.assertLessEqual(self.random_catalogue_instance7.id, 4)
        self.assertGreaterEqual(self.random_catalogue_instance8.id, 1)
        self.assertLessEqual(self.random_catalogue_instance8.id, 4)
        self.assertGreaterEqual(self.random_catalogue_instance9.id, 1)
        self.assertLessEqual(self.random_catalogue_instance9.id, 4)

class TestSwapStatus(TestCase):

    def setUp(self):
        self.album_instance = mommy.make(Album)

    def test_change_swap_status_on_album_instance(self):
        self.assertFalse(self.album_instance.swap_status)
        change_swap_status(self.album_instance)
        self.assertTrue(self.album_instance.swap_status)
        change_swap_status(self.album_instance)
        self.assertFalse(self.album_instance.swap_status)