from django.contrib import admin
from .models import Sighting, Comment, Reply, Photo

# Register your models below:
admin.site.register(Sighting)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Photo)
