from django.contrib import admin
from .models import Item, Review, Tag

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'name', 'desc', 'photo', 'updated_at',]
    # 위에서 'author.username'으로 하면 'not a callable' 오류
    # 위에서 'tags'로 하면 'must not be a ManyToManyField'라고 오류
    list_display_links = ['id', 'name', ]
    list_filter = ['created_at', 'updated_at', ]
    search_fields = ['name', 'desc', ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # list_display = ['id', 'post', 'message', 'updated_at', ]  # 바른 현지 시각
    list_display = ['id', 'item', 'review', 'updated', ]
    list_display_links = ['id', 'review', ]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    list_display_links = ['id', 'name', ]