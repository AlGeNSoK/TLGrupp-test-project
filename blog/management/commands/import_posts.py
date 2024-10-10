import requests
from django.core.management.base import BaseCommand
from blog.models import User, Post


class Command(BaseCommand):
    help = 'Import users from web site'

    def handle(self, *args, **options):

        response = requests.get('http://jsonplaceholder.typicode.com/posts')
        posts_list = response.json()

        for post in posts_list:
            Post.objects.create(
                                userId_id=User.objects.get(id=post['userId']).id,
                                id=post['id'],
                                title=post['title'],
                                body=post['body']
                                )

        self.stdout.write('Посты загружены в базу данных.')
