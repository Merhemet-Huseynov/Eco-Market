from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from users.models import CustomUser


class CustomUserDocument(Document):
    class Index:
        name = 'users'

    class Django:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']