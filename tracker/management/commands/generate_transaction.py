import random
from faker import Faker
from django.core.management.base import BaseCommand
from tracker.models import User, Category, Trasaction


class Command(BaseCommand):
    help = "Generate Transaction for Testing"

    def handle(self, *args, **options):
        fake = Faker()
        Categories = [
            "Bills",
            "clothes",
            "Food",
            "Medical",
            "Housing",
            "Salary",
            "Social",
            "Investment",
            "Transport",
            "Vacations",
        ]
        
        for category in Categories:
            Category.objects.get_or_create(name=category)
        
        # get the user
        user = User.objects.get(username="Rutuja") 
        if not user:
            user = User.objects.create_user(username="Test", password="1234")
        categories = Category.objects.all()
        for i in range(20):
            Trasaction.objects.create(
                user=user,
                category=random.choice(categories),
                type=random.choice(["income", "expense"]),
                amount=random.randint(100, 10000),
                date=fake.date_between(start_date = '-1y', end_date = 'today'),
            )
        
