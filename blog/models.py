from django.db import models
from django.core.validators import MinLengthValidator

class Tags(models.Model):
    caption = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=100)  # Removed unique=True
    last_name = models.CharField(max_length=100)   # Removed unique=True
    email = models.EmailField(unique=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Post(models.Model):  # Capitalized model name
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    image = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=200)
    excerpt = models.TextField(max_length=300)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tags, blank=True)

    def __str__(self):
        return self.title

    def get_tags(self):  # Added to display tags in admin
        return ", ".join([tag.caption for tag in self.tags.all()])
