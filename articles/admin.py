from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, ArticleScope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        chek = False
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                if chek:
                    raise ValidationError('Главная тема может быть лишь одна')
                else:
                    chek = True

        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = RelationshipInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ArticleScopeInline, ]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
