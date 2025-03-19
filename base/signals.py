from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User
import json

@receiver(post_migrate)
def populate_user_model(sender, **kwargs):
    # Check if the User model already has data
    if not User.objects.exists():
        # Create initial users
        with open("base/MOCK_DATA.json","r") as mock_data:
            data = json.load(mock_data)
            User.objects.create_user(username='admin', password='admin123', email='admin@example.com', is_staff=True, is_superuser=True)
            for user in data:
                User.objects.create_user(username=user['username'], password=user['password'], email=user["email"])
                print("Initial users have been created.")
    else:
        print("user exist")