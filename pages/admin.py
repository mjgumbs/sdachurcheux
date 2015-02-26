from django.contrib import admin
from django.conf import settings
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Page




SHOW_LOGIN_REQUIRED = getattr(settings, 'PAGE_SHOW_LOGIN', False)




@admin.register(Page)
class PageAdmin(DjangoMpttAdmin):

    list_display = ('url', 'title')
    list_filter = ('published',) + (('login_required',) if SHOW_LOGIN_REQUIRED else ())
    search_fields = ('url', 'title')


    def get_queryset(self, request):
        qs = super(PageAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(is_system=False)
