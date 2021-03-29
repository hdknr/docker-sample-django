from django.contrib import admin
from .models import Memo


class MemoModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'update_time', 'tag', 'counter')


admin.site.register(Memo, MemoModelAdmin)