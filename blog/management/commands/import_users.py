import requests
from django.core.management.base import BaseCommand
from blog.models import User, Company, Address, Geo


class Command(BaseCommand):
    help = 'Import users from web site'

    def handle(self, *args, **options):

        response = requests.get('http://jsonplaceholder.typicode.com/users')
        users_list = response.json()

        for user in users_list:
            company = Company.objects.create(
                                            name=user['company']['name'],
                                            catchPhrase=user['company']['catchPhrase'],
                                            bs=user['company']['bs']
                                            )

            geo = Geo.objects.create(
                                    lat=user['address']['geo']['lat'],
                                    lng=user['address']['geo']['lng']
                                    )

            address = Address.objects.create(
                                           street=user['address']['street'],
                                           suite=user['address']['suite'],
                                           city=user['address']['city'],
                                           zipcode=user['address']['zipcode'],
                                           geo_id=geo.id
                                            )

            User.objects.create(
                                id=user['id'],
                                name=user['name'],
                                username=user['username'],
                                email=user['email'],
                                address_id=address.id,
                                phone=user['phone'],
                                website=user['website'],
                                company_id=company.id
                                )

        self.stdout.write('Данные о пользователях загружены в базу данных.')
