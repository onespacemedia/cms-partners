from cms.admin import OnlineBaseAdmin
from django.contrib import admin
from suit.admin import SortableModelAdmin

from .models import Partner


@admin.register(Partner)
class PartnerAdmin(OnlineBaseAdmin, SortableModelAdmin):
    list_display = ['title', 'is_online', 'order']
    list_editable = ['is_online', 'order']
