from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article, Tag
# Create your tests here.


class ArticleModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='User', password='password')
        self.article = Article.objects.create(
            name='test-name',
            content='test-content',
            author=self.user,
        )

    def test_article_created_and_in_database(self):
        articles = Article.objects.all()
        self.assertIn(self.article, articles)

    def test_article_with_tags_can_be_create(self):
        tags = [
            Tag.objects.create(name='tag-1'),
            Tag.objects.create(name='tag-2')
        ]
        self.article.tags.set(tags)
        self.article.save()
        articles = Article.objects.filter(tags__name='tag-2')
        self.assertIn(self.article, articles)

        def tearDown(self):


class ArticleViewTest(TestCase):
    def test_article_created_and_exist_on_page(self):
        user = User.objects.create(username='User', password='password')
        article = Article.objects.create(
            name='test-name',
            content='test-content',
            author=user,
        )
        response = self.client.get('/article/'+str(article.id))
        self.assertContains(response, 'test-content')
