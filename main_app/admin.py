from django.contrib import admin
from .models import Sighting, Comment, Reply

# Register your models below:
admin.site.register(Sighting)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Photo)
