from django.contrib import admin
from models import Carousel, register, Tags, Category, Article
from django import forms
from django.forms import CheckboxSelectMultiple
# Register your models here.

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'create_time')

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'img', 'create_time')

class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time')

class TagsForm(forms.ModelForm):

    tags = forms.ModelMultipleChoiceField(widget=CheckboxSelectMultiple, queryset=Tags.objects.all())

    class Meta:
        model = Tags
        fields = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'create_time')

class ArticleAdmin(admin.ModelAdmin):
    # inlines = [TagsAdmin, ]
    # filter_horizontal = ('Tags',)
    form = TagsForm
    list_display = ('title', 'author', 'category', 'create_time')

admin.site.register(Carousel, CarouselAdmin)
admin.site.register(register, RegisterAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
