# encoding=utf8


from .forms import *
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets
from .encryption import jwt_payload_handler, jwt_encode_handler
from django.http import QueryDict
from django.contrib.auth.hashers import make_password
from .authentication import is_authenticate
from .permissions import IsAuthenticated

def home(request):
    return render(request, 'report/base.html')

def category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('category_detail', pk=post.pk)
    else:
        form = CategoryForm()
    return render(request, 'report/category.html', {'form': form})


def category_detail(request, pk):
    post = get_object_or_404(Category, pk=pk)
    return render(request, 'report/category_detail.html', {'post': post})

def category_update(request, pk):
    post = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('category_detail', pk=post.pk)
    else:
        form = CategoryForm(instance=post)
    return render(request, 'report/category_edit.html', {'form': form})

def category_information(request):
    category_data = Category.objects.all()
    return render(request, 'report/category_information.html', {'posts': category_data})

def report(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('report_detail', pk=post.pk)
    else:
        form = ReportForm()
    return render(request, 'report/report.html', {'form': form})


def report_detail(request, pk):
    post = get_object_or_404(Report, pk=pk)
    return render(request, 'report/report_detail.html', {'post': post})

def report_update(request, pk):
    post = get_object_or_404(Report, pk=pk)
    if request.method == "POST":
        form = ReportForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('report_detail', pk=post.pk)
    else:
        form = ReportForm(instance=post)
    return render(request, 'report/report_edit.html', {'form': form})

def report_information(request):
    report_data = Report.objects.all()
    return render(request, 'report/report_information.html', {'posts': report_data})


def comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('comment_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'report/comment.html', {'form': form})


def comment_detail(request, pk):
    post = get_object_or_404(Comments, pk=pk)
    return render(request, 'report/comment_detail.html', {'post': post})


def comment_update(request, pk):
    post = get_object_or_404(Comments, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('comment_detail', pk=post.pk)
    else:
        form = CommentForm(instance=post)
    return render(request, 'report/report_edit.html', {'form': form})


def report_comments(request, pk):
    comment_objs = Comments.objects.filter(report=pk)
    return render(request, 'report/report_comments.html', {'posts': comment_objs})

def filter_report(request):
    from_date = request.POST["from_date"]
    to_date = request.POST["to_date"]
    report_data = Report.objects.filter(created__range=[from_date, to_date])
    return render(request, 'report/report_information.html', {'posts': report_data})

class UserAPIs(viewsets.ModelViewSet):

    @staticmethod
    def signup(request):
        user_obj = UsersDetails.objects.filter(email=request.data["email"])
        if len(user_obj)==0:
            data = QueryDict.dict(request.data)
            data["username"]=request.data["email"]
            data["password"] = make_password(data["password"])
            serializer = UsersDetailsSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                user = UsersDetails.objects.get(id=serializer.data["id"])
                serializer = UsersGetSerializers(user)
                payload = jwt_payload_handler(user)
                context = {
                    'token': jwt_encode_handler(payload),
                    'user': serializer.data,
                    'status': 200
                }
                return Response(context)
            return Response(serializer.errors, status=400)
        else:
            return Response({"message":"User already exists"}, 400)

    @staticmethod
    def login(request):
        user_obj = UsersDetails.objects.filter(email=request.data["email"], active=True)
        if len(user_obj) != 0:
            username = request.data['email']
            password = request.data['password']
            # account_type = request.data['account_type']
            user = is_authenticate(username, password)
            if user is None:
                context = {
                    'message': "User credentials did not match",
                    'status': 400
                }
                return Response(context)
            payload = jwt_payload_handler(user)
            serializer = UsersGetSerializers(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                context = {
                    'token': jwt_encode_handler(payload),
                    'user': serializer.data,
                    'status': 200
                }
                return Response(context, 200)
            else:
                return Response(serializer.errors, 400)
        else:
            context = {
                'message': "User does not exists",
                'status': 400
            }
            return Response(context)


class UsersOtherAPIs(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_users_list(self, request):
        users = UsersDetails.objects.all()
        serializer = UsersGetSerializers(users, many=True)
        return Response(serializer.data)
