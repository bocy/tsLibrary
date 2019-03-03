from django.contrib import admin
from .models import BookInfo, BorrowRecord

# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'type', 'up_time', 'borrowed_time', 'borrower', 'is_borrowed']


class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ['borrower', 'book', 'borrow_time', 'return_time', 'is_return']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(BorrowRecord, BorrowRecordAdmin)
