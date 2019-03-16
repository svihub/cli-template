from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')

    def test_json(self):
        b = Blog('Test', 'Test Author')
        
        b.create_post('Test Post1', 'Test Content1')
        b.create_post('Test Post2', 'Test Content2')

        expected = {
            'Title': 'Test',
            'Author': 'Test Author',
            'posts': [
                {
                    'title': 'Test Post1',
                    'content': 'Test Content1'
                },
                {
                    'title': 'Test Post2',
                    'content': 'Test Content2'
                }
            ]
        }

        self.assertDictEqual(expected, b.json())

        
