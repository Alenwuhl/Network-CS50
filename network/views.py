import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, User
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@login_required
def edit_post(request, post_id):
    if request.method == "PUT":
        try:
            post = Post.objects.get(pk=post_id)
            if post.user != request.user:
                return JsonResponse(
                    {"error": "You are not authorized to edit this post."}, status=403
                )
            data = json.loads(request.body)
            new_content = data.get("content", "")
            post.content = new_content
            post.save()

            return JsonResponse({"message": "Post updated successfully."}, status=200)
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post not found."}, status=404)
    else:
        return JsonResponse({"error": "PUT request required."}, status=400)


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "network/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "network/register.html", {"message": "Passwords must match."}
            )

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request, "network/register.html", {"message": "Username already taken."}
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@login_required
def newPost(request):
    if request.method == "POST":
        content = request.POST.get("content", "").strip()

        if content:
            user = request.user
            post = Post(user=user, content=content)
            post.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "network/newPost.html",
                {"error_message": "The post cannot be empty."},
            )
    else:
        return render(request, "network/newPost.html")


def allPosts(request):
    posts = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "network/allPosts.html", {"page_obj": page_obj})


@login_required
def profile(request, username):
    user_profile = get_object_or_404(User, username=username)

    is_following = user_profile.followers.filter(id=request.user.id).exists()

    follower_count = user_profile.followers.count()
    following_count = user_profile.following.count()

    posts = Post.objects.filter(user=user_profile).order_by("-timestamp")

    return render(request, "network/profile.html", {
        "user_profile": user_profile,
        "is_following": is_following,
        "follower_count": follower_count,
        "following_count": following_count,
        "posts": posts
    })


@login_required
def toggle_follow(request, username):
    user_to_follow = get_object_or_404(User, username=username)

    if request.user != user_to_follow:
        if user_to_follow.followers.filter(id=request.user.id).exists():
            user_to_follow.followers.remove(request.user)
        else:
            user_to_follow.followers.add(request.user)

    return redirect('profile', username=user_to_follow.username)

@login_required
def following(request):
    followed_users = request.user.following.all()

    posts = Post.objects.filter(user__in=followed_users).order_by("-timestamp")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "network/following.html", {
        "page_obj": page_obj
    })


@login_required
@require_http_methods(["PUT"])
def like_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)

        if request.user in post.likes.all():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        post.save()

        return JsonResponse(
            {"liked": liked, "likes_count": post.likes.count()}, status=200
        )
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)
