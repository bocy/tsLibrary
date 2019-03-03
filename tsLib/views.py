from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotAllowed
from .models import BorrowRecord, BookInfo
from django.utils import timezone
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

# Create your views here.


def index(request):
    return render(request, "index.html")


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        request.session['user'] = username
        response = HttpResponseRedirect("/borrowed_list/")
        return response
    else:
        return render(request, "index.html", {"error": "用户名密码错误"})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


@login_required
def borrowed_list(request):
    username = request.session.get('user', '')
    borrowed_list = BorrowRecord.objects.filter(borrower=username, is_return=False)
    return render(request, "myBorrowedList.html", {"username": username, "borrowed_list": borrowed_list})


@login_required
def book_list(request):
    username = request.session.get('user', '')
    books = BookInfo.objects.all()
    paginator = Paginator(books, 15)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "bookList.html", {"username": username, "books": contacts})


@login_required
def borrow_book(request, book_id):
    username = request.session.get("user", "")
    bookinfo = BookInfo.objects.get(pk=book_id)
    if bookinfo.is_borrowed:
        return HttpResponseNotAllowed(content="图书已被借阅，请勿重复借阅", permitted_methods="post")
    bookinfo.is_borrowed = True
    bookinfo.borrower = username
    bookinfo.borrowed_time = timezone.now()
    bookinfo.save()
    borrow_record = BorrowRecord.objects.create(borrower=username, book=bookinfo,
                                                return_time=None,
                                                is_return=False)
    borrow_record.save()

    return HttpResponseRedirect("/book_list/")


@login_required
def return_book(request, borrow_id):
    borrow_record = BorrowRecord.objects.get(pk=borrow_id)
    if borrow_record.is_return:
        return HttpResponseNotAllowed(permitted_methods='post')
    borrow_record.is_return = True
    borrow_record.return_time = timezone.now()
    borrow_record.save()
    book_id = borrow_record.book.id
    BookInfo.objects.filter(pk=book_id).update(is_borrowed=False, borrower="", borrowed_time=None)
    return HttpResponseRedirect("/borrowed_list/")


@login_required
def borrow_history(request):
    username = request.session.get("user", "")
    borrow_records = BorrowRecord.objects.filter(borrower=username).order_by("-id")
    paginator = Paginator(borrow_records, 15)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "borrowHistory.html", {"username": username, "borrow_records": contacts})


