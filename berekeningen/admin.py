from django.contrib import admin

from .models import BerekeningLog


@admin.register(BerekeningLog)
class BerekeningLogAdmin(admin.ModelAdmin):
	list_display = ('omzet', 'inkoopkosten', 'brutomarge', 'margepercentage', 'aangemaakt_op')
	ordering = ('-aangemaakt_op',)
