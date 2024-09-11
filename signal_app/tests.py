from django.test import TestCase
from django.db.models.signals import post_save
from .models import Post
import threading



class PostSignalTest(TestCase):

    def test_post_save_signal(self):
        # Create a new Post object
        print("creating test This prove Answer 1")  # this will be printed before the signal is called

        print(f"Test thread ID: {threading.get_ident()} This prove Answer 2")

        post = Post.objects.create(title="Signal Test")

        print("test completed This prove Answer 1")  # this will be printed after the signal is called

        self.assertEqual(post.title, "Signal Test")
