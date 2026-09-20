from django.contrib import admin

from apps.cart.models import Cart, CartItem

class CartItemLine(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'updated_at']
    inlines = [CartItemLine]