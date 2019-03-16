from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')

        expected = f"{b.title} by {b.author} ({len(b.posts)} posts)."
        self.assertEqual(expected, b.__repr__())

    def test_repr_mult_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test']

        expected = f"{b.title} by {b.author} (1 post)."
        self.assertEqual(expected, b.__repr__())

