from django.db import models
from django.utils import timezone
# Create your models here.


class BookInfo(models.Model):
    name = models.CharField(max_length=64, verbose_name="书名")
    author = models.CharField(max_length=64, verbose_name="作者")
    type = models.CharField(max_length=64, verbose_name="类别")
    up_time = models.DateTimeField(auto_now=True, verbose_name="上架时间")
    borrowed_time = models.DateTimeField(null=True, verbose_name="借阅时间")
    borrower = models.CharField(max_length=64, verbose_name="借阅人")
    is_borrowed = models.BooleanField(verbose_name="是否已被借阅")

    def __str__(self):
        return self.name


class BorrowRecord(models.Model):
    borrower = models.CharField(max_length=64, verbose_name="借阅人")
    book = models.ForeignKey("BookInfo", verbose_name="借阅书籍", on_delete=models.CASCADE)
    borrow_time = models.DateTimeField(auto_now=True, verbose_name="借阅时间")
    return_time = models.DateTimeField(null=True, verbose_name="归还时间")
    is_return = models.BooleanField(verbose_name="是否已归还")

    def __str__(self):
        return self.borrower


