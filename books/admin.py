from django.contrib import admin
from .models import FollowersCount
from .models import Profile
from .models import Contact
from .models import Book
# from.models import FollowerSystem


# register user model here

admin.site.register(Book)

admin.site.register(Contact)

admin.site.register(Profile)

admin.site.register(FollowersCount)

# admin.site.register(FollowerSystem)
