from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from network.models import (
    Company,
    Products
)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Админка связанная с информацией о компаниях"""
    list_display = ('title',
                    'email',
                    'country',
                    'city',
                    'street',
                    'house',
                    'vendor_link',
                    'debt',
                    'publication_date',
                    'user', )

    list_filter = ['city']

    actions = ['erase_debt_action']

    @admin.action(description='обнулить задолженность перед поставщиком у выбранных объектов')
    def erase_debt_action(self, request, queryset):
        """Обнуляет задолженность у выбранных компаний"""
        queryset.update(debt=0)

    def vendor_link(self, obj):
        """Ссылку на компанию-вендора"""
        if obj.vendor:
            link = reverse(
                'admin:company_company_change',  # app:model:page
                args=(obj.vendor.id,)
            )
            return mark_safe(
                u"<a href='{0}'>{1}</a>".format(link, obj.vendor)
            )


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'release',)
    search_fields = ('title', 'model',)