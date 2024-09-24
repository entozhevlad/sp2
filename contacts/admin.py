from django.contrib import admin
from .models import Adress

@admin.register(Adress)
class AdressAdmin(admin.ModelAdmin):
    list_display = ('adress', 'graphic_1', 'graphic_2')
    search_fields = ('adress',)
    list_filter = ('graphic_1', 'graphic_2')
    ordering = ('adress',)
    fieldsets = (
        (None, {
            'fields': ('adress', 'graphic_1', 'graphic_2')
        }),
    )

    class Meta:
        model = Adress