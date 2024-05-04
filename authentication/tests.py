from django.core.files import File
from django.test import TestCase
from authentication.models import Post
from django.test import Client

# Create your tests here.
class PostListCreator(TestCase):

    def setUp(self):
        self.post1 = Post.objects.create(title='Post1', description='huy', owner='1', picture=File(open("./media/images/vert.jpg", 'rb')))
        self.client = Client()


    def test_posts(self):
        response = self.client.get('http://localhost:8000/api/posts/?search=Post1')
        print(response)
        self.assertContains(response, "Post1")
