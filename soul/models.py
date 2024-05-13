""" Models """
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



MEAL_TYPES = (
    ('breakfast','Breakfast'),
    ('lunch','Lunch'),
    ('dinner','Dinner'),
    ('dessert','Dessert'),
)

STATUS = ((0, "Draft"), (1, "Published"))

class Recipe(models.Model):
    """
    A model to create and manage recipes
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_owner", null=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    instructions = models.TextField(max_length=1000, null=False, blank=False)
    ingredients = models.TextField(max_length=1000, null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    image_url = models.URLField(blank=True)
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPES, default='brakfast') 
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    published_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published_on']

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        now = datetime.datetime.now()
        d_truncated_date = datetime.date(now.year, now.month, now.day)
        d_truncated_time = datetime.time(now.hour, now.minute, now.second)
        self.slug = slugify(
            f'{self.author}-{self.title}-{d_truncated_date}-{d_truncated_time}'
            )
        super(Recipe, self).save(*args, **kwargs)

    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)
    
class Comment(models.Model):
    """
    Model for comments
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments'
        )
    name = models.CharField(max_length=80)
    body = models.TextField(max_length=100, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('recipe_detail', args=[self.recipe.slug])   
    
   
    