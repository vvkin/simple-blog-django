from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post

class TestPages(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='user',
            email='user@gmail.com',
            password='user1234'
        )

        self.post = Post.objects.create(
            title='title',
            body='body',
            author=self.user
            )

    def test_home_page_request(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_name_request(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_one_page_response_template(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'one_post.html')

class TestPostModel(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='user',
            email='user@gmail.com',
            password='user1234'
        )
        self.post = Post.objects.create(
            title='title',
            body='body',
            author=self.user,
            )

    def test_object_fields(self):
        self.assertEqual('title', self.post.title)
        self.assertEqual('body', self.post.body)
        self.assertEqual(self.user, self.post.author)

    def test_author_fields(self):
        self.assertEqual('user', self.user.username)
        self.assertEqual('user@gmail.com', self.user.email)
        self.assertEqual('user1234', self.user.password)

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'title')
        self.assertTemplateUsed(response, 'one_post.html')
