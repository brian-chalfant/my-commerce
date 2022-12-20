from django.contrib import admin
from auctions.models import Comment, User, Bid, Listing
# Register your models here.
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Listing)
