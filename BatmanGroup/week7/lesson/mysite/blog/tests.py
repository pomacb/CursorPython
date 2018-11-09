from django.test import TestCase, Client
from .models import Article
from django.urls import reverse


class ArticleTestCase(TestCase):

    def setUp(self):
        Article.objects.create(
            title='Test title',
            description='Some Description',
            author='Roman'
        )

    def test_article_exist(self):
        """Creatd article exists in the database"""

        article = Article.objects.get(title='Test title')
        self.assertEqual(article.author, 'Roman')


class ArticleCreateViewTest(TestCase):

    def setUp(self):
        client = Client()

    def test_article_created(self):
        """ Check created article in the database"""
        response = self.client.post(reverse('add_article'),
                                    {'title': 'Test title', 'description': 'Some description', 'author': 'Roman'}
                                    )
        self.assertEqual(response.status_code, 302)
