from django.test import TestCase


from hello.models import Person

class HelloModelsTest(TestCase):

    def setUp(self):
        self.person = Person.objects.create(
            name='Artem',
            last_name='Khymenko',
            date_of_birth='07.11.1989',
            bio='Long way',
            email='artem.khymenko@gmail.com',
            jabber='artemkhymenko',
            skype='breakerhim',
            other_contacts='smth'
        )

    def test_model(self):
        self.asserEqual(self.person.name, 'Artem')
        self.asserEqual(self.person.bio, 'Long way')
