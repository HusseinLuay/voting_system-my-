from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Competition)
admin.site.register(Team)
admin.site.register(Vote)

