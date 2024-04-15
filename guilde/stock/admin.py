from django.contrib import admin
from .models import GameInstance, Game, User_info, Booking

admin.site.register(Game)
admin.site.register(GameInstance)
admin.site.register(User_info)
admin.site.register(Booking)

# @admin.register(GameInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#     list_display = ('game', 'state', 'borrower', 'echeance', 'id')
#     list_filter = ('state', 'echeance')

#     fieldsets = (
#         (None, {
#             'fields': ('game', 'id')
#         }),
#         ('Availability', {
#             'fields': ('state', 'echeance', 'borrower')
#         }),
#     )

# # BoxAdmin ???