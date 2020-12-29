from django.contrib import admin
from notes.models import Notes
from journal.models import Journal

admin.site.register(Journal)
admin.site.register(Notes)

