# TO Display the Forms
from django import forms
# To Display the Pop Up Messages
from django.contrib import messages
from django.contrib.messages.api import add_message, info
from django.core.checks.messages import INFO
# For the User Request
from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
# TO get the models Data
from books import models
from .models import Book, Profile
from .models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
# For check the user Valid or Not
from django.contrib.auth import authenticate
# for login required
from django.contrib.auth.decorators import login_required
# create user
from .forms import UserUpdate, ProfileUpdate

from django.core.files.storage import FileSystemStorage

# for contact us email send
from django.core.mail import send_mail

# check email address exists or not
# from validate_email import validate_email

# following system models
from .models import FollowersCount


# Create your views here.

# home page


@login_required(login_url="/login/")
def homepage(request):

    allbooks = []

    bookitems = Book.objects.values('book_category', 'id')
    cats = {item['book_category'] for item in bookitems}
    cats = sorted(cats)

    for cat in cats:
        book = Book.objects.filter(book_category=cat)
        n = len(book)
        nSlides = len(allbooks)
        allbooks.append([book, nSlides])

    RequestProfile = User.objects.all()
    bookcatdis = Book.objects.all()
    categorynav = []
    for b in bookcatdis:
        if b.book_category not in categorynav:
            categorynav.append(b.book_category)
    categorynav.sort()

    UserIds = []
    for i in User.objects.all():
        UserIds.append(i.id)

    for i in FollowersCount.objects.all():
        if int(i.user) not in UserIds:
            i.delete()
        if int(i.follower) not in UserIds:
            i.delete()

    params = {'allbooks': allbooks, 'BookCat': categorynav,
              "RequestProfile": RequestProfile}
    return render(request, 'helping_books.html', params)

# contact us


@login_required(login_url="/login/")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', 'unknown')
        email_address = request.POST.get('email')
        message = request.POST.get('message', 'no message')

        # send mail to web host
        send_mail(
            # mail subject
            f"message from {name} and send from {email_address}",
            message,  # message
            email_address,  # from email
            ['sagarkakade0201@gmail.com'],  # to mail
        )

        Contact_us = Contact(
            name=name, email_address=email_address, message=message)
        Contact_us.save()
        messages.success(request, "Message Send  Successfully")
    return render(request, 'ContactUs.html')

# For About Page


@login_required(login_url="/login/")
def about(request):
    return render(request, 'helping_books.html')

# add book


@login_required(login_url="/login/")
def addbook(request):
    if request.method == "POST":
        book_image = request.FILES['img']
        user_image = request.user.profile.image.url
        user_name = request.user.username
        user_id = request.user.id
        book_name = request.POST.get('book_name',)
        book_category = request.POST.get('book_category')
        book_outher = request.POST.get('book_outher')
        book_category = book_category.capitalize()
        user_mobile_no = int(request.POST.get('mobile_number'))
        book_info = request.POST.get('book_info')
        user_address = request.POST.get('user_address')

        params = {"book_image": book_image, "book_name": book_name, "book_category": book_category,
                  "book_outher": book_outher, "user_mobile_no": user_mobile_no, "book_info": book_info, "user_address": user_address}

        if type(user_mobile_no) != int:
            messages.error(request, 'Mobile Number Must Be Intergers.')
            return render(request, 'addBook.html', params)

        if len(str(user_mobile_no)) != 10:
            messages.error(request, "Mobile Number Must Be 10 Degits.")
            # return redirect('/addbook', params)
            return render(request, 'addBook.html', params)

        addbook = Book(user_id=user_id, user_name=user_name, book_image=book_image, book_name=book_name, book_category=book_category,
                       book_outher=book_outher, user_mobile_no=user_mobile_no, book_info=book_info, user_address=user_address, user_image=user_image)
        addbook.save()
        messages.success(request, "Book Added Successfully")
    return render(request, 'addBook.html')

# new user account creation


def SignUp(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']

        # check for errorneous input
        if len(username) > 10:
            messages.error(request, "Plase Enter The User Name Under 10 Char.")
            return redirect('/signup')

        if not username.isalnum():
            messages.error(
                request, "Username should only contain letters and number")
            return redirect('/signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "This Username should All Ready Taken")
            return redirect('/signup')
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, f"Account Created sucessfully. Your Username is {username} and Password is {password}")

    return render(request, 'signup.html')

# Login User


def login(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect("home")
            else:
                messages.error(request, "You're Account is Disable")
        else:
            messages.error(
                request, "Invalid Username Or Password please try again")
            return render(request, 'loginpage.html', {"loginusername": loginusername, "loginpassword": loginpassword})

    return render(request, 'loginpage.html')

# Logout login user


@login_required(login_url="/login/")
def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("/")

# Login User Profile page


@login_required(login_url="/login/")
def profile(request):
    if request.method == "POST":
        u_form = UserUpdate(request.POST, instance=request.user)
        p_form = ProfileUpdate(request.POST, request.FILES,
                               instance=request.user.profile)
        BookId = request.POST.get('BookId')

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile Update Sucessfully.")

        if BookId is not None:
            BookDelete = Book.objects.get(pk=BookId)
            BookDelete.delete()
            messages.success(request, "Book Delete Sucessfully")
            return redirect("profile")
        return redirect("/profile")

    else:
        u_form = UserUpdate(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.profile)
        books = Book.objects.all()
        profile = Profile.objects.all()
        current_user = request.user.id
        UserId = current_user

        Request_user_profile_info = User.objects.filter(id=UserId)

        person_user = ""
        for person in Request_user_profile_info:
            person_user = person.id

        user_followers = len(FollowersCount.objects.filter(
            user=person_user))
        user_following = len(
            FollowersCount.objects.filter(follower=person_user))

        allbooks = []
        for book in books:
            if book.user.id == current_user:
                allbooks.append(book)
        n = len(allbooks)
        r = range(1, n)

        # User Followings User Display

        user_following_name_list = []
        for user in FollowersCount.objects.filter(follower=current_user):
            user_following_name_list.append(user.user)

        user_following_user_list = []
        for i in user_following_name_list:
            for u in User.objects.filter(id=i):
                user_following_user_list.append(u)

        user_follower_name_list = []
        for user in FollowersCount.objects.filter(user=current_user):
            user_follower_name_list.append(user.follower)

        user_follower_user_list = []
        for i in user_follower_name_list:
            for u in User.objects.filter(id=i):
                user_follower_user_list.append(u)

        params = {'current_user': current_user, 'Book': allbooks,
                  'p_form': p_form, 'u_form': u_form, 'r': r, 'n': n, 'user_followers': user_followers, 'user_following': user_following, "user_following_user_list": user_following_user_list, 'user_follower_user_list': user_follower_user_list}
        return render(request, 'account/profile.html', params)


# show allbooks in categories
@login_required(login_url="/login/")
def allBooks(request):
    if request.method == "POST":
        BooksCategory = request.POST.get('showBook', 'history')

        books = Book.objects.all()
        allbooks = []
        for book in books:
            if book.book_category == BooksCategory:
                allbooks.append(book)
        params = {'Book': allbooks}
        return render(request, 'allBooksPages.html', params)

# Users Request Profile Page


@login_required(login_url="/login/")
def requestProfile(request):
    if request.method == 'POST':
        value = request.POST.get('value')
        follower = request.POST.get('follower')
        user = request.POST.get('user')
        userId = request.POST.get('userId')
        logged_in_user = request.user.username

        if value == "follow":
            followers_cnt = FollowersCount.objects.create(
                follower=follower, user=user)
            followers_cnt.save()
        else:
            FollowersCount.objects.filter(
                follower=follower, user=user).delete()

        return redirect("/requestProfile?UserId="+userId)

    UserId = int(request.GET.get('UserId', '0'))
    logged_in_user = str(request.user.id)

    Request_user_profile_info = User.objects.filter(id=UserId)
    # Request_user_profile_photo = User.objects.filter(id=UserId)
    Request_user_profile_Books = Book.objects.filter(user_id=UserId)

    person_user = ""
    for person in Request_user_profile_info:
        person_user = str(person.id)

    users_followers0 = FollowersCount.objects.filter(
        follower=logged_in_user, user=person_user)

    user_post = len(Request_user_profile_Books)
    user_followers = len(FollowersCount.objects.filter(
        user=person_user))
    user_following = len(
        FollowersCount.objects.filter(follower=person_user))

    users_followers1 = []
    for user in users_followers0:
        users_followers1.append([user.follower, user.user])

    if [logged_in_user, person_user] in users_followers1:
        user_follower_value = "unfollow"
    else:
        user_follower_value = "follow"

    params = {'Profile': Request_user_profile_info,
              'user_followers': user_followers, 'user_following': user_following, 'user_post': user_post, 'user_follower_value': user_follower_value, 'UserId': UserId}
    return render(request, 'requestProfile.html', params)


# Search Results
@login_required(login_url="/login/")
def search(request):
    search = request.GET.get('Query')

    if len(search) > 78:
        allbooks = Book.objects.none()
    else:
        allbook_name = Book.objects.filter(book_name__icontains=search)
        allbook_user_name = Book.objects.filter(user_name__icontains=search)
        allbook_book_category = Book.objects.filter(
            book_category__icontains=search)
        allbook_book_outher = Book.objects.filter(
            book_outher__icontains=search)
        allbook_user_mobile_no = Book.objects.filter(
            user_mobile_no__icontains=search)
        allbook_book_info = Book.objects.filter(book_info__icontains=search)
        allbook_user_address = Book.objects.filter(
            user_address__icontains=search)
        allbooks = allbook_name.union(
            allbook_user_name, allbook_book_category, allbook_book_outher, allbook_user_mobile_no, allbook_book_info, allbook_user_address)

    if allbooks.count() == 0:
        messages.warning(
            request, "No Search results Found. Please refine your query. Please Try Another KeyWords.")

    params = {"Book": allbooks, "Query": search}
    return render(request, 'SearchResults.html', params)
