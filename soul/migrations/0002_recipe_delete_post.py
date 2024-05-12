# Generated by Django 4.2.11 on 2024-05-12 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('soul', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('instructions', djrichtextfield.models.RichTextField(max_length=1000)),
                ('ingredients', models.TextField(max_length=1000)),
                ('image_url', models.URLField(blank=True)),
                ('meal_type', models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('dessert', 'Dessert')], default='brakfast', max_length=50)),
                ('vegan', models.BooleanField(default=False)),
                ('vegetarian', models.BooleanField(default=False)),
                ('published_on', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('featured', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_owner', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='recipe_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-published_on'],
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
