#from django.contrib import admin
#from .models import Post, Author, Tags

#class PostAdmin(admin.ModelAdmin):
 #   list_display = ('tags', 'author', 'date')
  #  prepopulated_fields = {'slug': ('title',)}
    #search_fields = ('title', 'content')
 #   list_filter = ('date', 'author', 'title')  


#admin.site.register(Post, PostAdmin)  
#admin.site.register(Author)
#admin.site.register(Tags)
# Register your models here.


from django.contrib import admin
from .models import Post, Author, Tags # Use capitalized Post
from .models import Comment 
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_tags', 'author', 'date')  # Replaced 'tags' with 'get_tags'
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('date', 'author', 'title')

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tags)
admin.site.register(Comment, CommentAdmin)  # Register Comment model with admin