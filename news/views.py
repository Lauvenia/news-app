from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from .twitter import send_tweet

from .forms import ArticleForm, NewsletterForm
from .models import Article, Newsletter, Publisher


@login_required  # Ensures only logged-in users can access this view
def home(request):
    return render(request, "home.html")


@login_required  # Ensures only logged-in users can access this view
def create_article(request):
    if request.user.role == "journalist":

        # If the request is a POST, it means the form was submitted
        if request.method == "POST":
            form = ArticleForm(request.POST)
            # Check if form input is valid according to the model & form rules
            if form.is_valid():
                article = form.save(commit=False)
                # Assign the logged-in user as the article's author
                article.author = request.user
                article.save()
                return redirect("dashboard")
        else:
            # If it's not a POST request, display a blank form
            form = ArticleForm()
            return render(request, "article/article_form.html", {"form": form})
    else:  # If user is not a journalist, redirect to homepage
        return redirect("home")


@login_required  # Ensures only logged-in users can access this view
def list_articles_and_newsletters(request):
    if request.method == "GET":
        user = request.user

        if user.role in ["journalist", "editor"]:
            article = Article.objects.all()
        else:
            article = Article.objects.filter(is_approved=True)

        newsletter = Newsletter.objects.all()

        # Get users that subscribed to journalists and publishers for display
        subscribed_to_journalists = user.subscribed_journalists.all()
        subscribed_to_publishers = user.subscribed_publishers.all()

        context = {
            "articles": article,
            "newsletters": newsletter,
            "journalists": subscribed_to_journalists,
            "publishers": subscribed_to_publishers,
        }
        return render(request, "dashboard.html", context)


@login_required  # Ensures only logged-in users can access this view
def article_detail(request, pk):
    if request.method == "GET":
        article = get_object_or_404(Article, pk=pk)

        return render(request, "article/article_detail.html", {"article": article})


@login_required  # Ensures only logged-in users can access this view
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)

    # ensure user is an editor or the journalist for this particular article
    if not (request.user.role == "editor" or request.user == article.author):
        raise PermissionError

    if request.method == "POST":
        # Bind the form to POST data and the existing newsletter instance
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("article_detail", pk=article.pk)
    else:
        # If it's a GET request, display the form with current data pre-filled
        form = ArticleForm(instance=article)
    # Render the update form template with the form instance
    return render(request, "article/article_form.html", {"form": form})


@login_required  # Ensures only logged-in users can access this view
def delete_article(request, pk):
    # Fetch the article by primary key-pk or return a 404 error if not found
    article = get_object_or_404(Article, pk=pk)

    if request.user.role == "editor" or request.user == article.author:
        article.delete()
    return redirect("dashboard")


@login_required  # Ensures only logged-in users can access this view
def approve(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.user.role == "editor":
        article.is_approved = True
        article.save()

        # Retrieve the emails of users who subscribed to this article's author
        # (journalist)  & publisher when a new article has been approved
        email_set1 = (
            article.author.subscribed_journalists.all()
            .values_list("email", flat=True)
            .distinct()  # Remove duplicates
        )
        email_set2 = (
            article.publisher.publisher_subscribers.all()
            .values_list("email", flat=True)
            .distinct()  # Remove duplicates
        )
        # Combine both email sets into a single list without duplicates
        combined_emails = email_set1 | email_set2

        subject = f"{article.title} has been approved"
        message = "This an update message to inform you that a new article from your subscriptions has been approved"
        from_email = "shop@example.com"
        recipients = combined_emails

        # Send the notification email to all subscribers
        send_mail(subject, message, from_email, recipients, fail_silently=False)

        # Send a tweet to announce the approved article
        tweet_msg = f"New article {article.title} has been approved"
        send_tweet(tweet_msg)

    return redirect("dashboard")


@login_required  # Ensures only logged-in users can access this view
def create_newsletter(request):
    if request.user.role == "journalist":
        if request.method == "POST":
            form = NewsletterForm(request.POST)
            if form.is_valid():
                newsletter = form.save(commit=False)
                newsletter.author = request.user
                newsletter.save()
                return redirect("dashboard")
        else:
            form = NewsletterForm()
            return render(request, "newsletter/newsletter_form.html", {"form": form})


@login_required  # Ensures only logged-in users can access this view
def newsletter_detail(request, pk):
    if request.method == "GET":
        newsletter = get_object_or_404(Newsletter, pk=pk)
        return render(
            request, "newsletter/newsletter_detail.html", {"newsletter": newsletter}
        )


@login_required  # Ensures only logged-in users can access this view
def newsletter_update(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)

    if not (request.user.role == "editor" or request.user == newsletter.author):
        raise PermissionError

    if request.method == "POST":
        # Bind the form to POST data and the existing newsletter instance
        form = NewsletterForm(request.POST, instance=newsletter)
        if form.is_valid():
            form.save()
            # After saving Redirect to detail page of the updated newsletter
            return redirect("newsletter_detail", pk=newsletter.pk)
    else:
        # If it's a GET request, display the form with current data pre-filled
        form = NewsletterForm(instance=newsletter)

    # Render the update form template with the form instance
    return render(request, "newsletter/newsletter_form.html", {"form": form})


@login_required  # Ensures only logged-in users can access this view
def delete_newsletter(request, pk):
    # Fetch the newsletter by primary key-pk or return a 404 error if not found
    newsletter = get_object_or_404(Newsletter, pk=pk)

    # make sure the logged in user is not a reader and delete the newsletter
    if request.user.role != "reader":
        newsletter.delete()
    return redirect("dashboard")


@login_required  # Ensures only logged-in users can access this view
def subscribe_to_publisher(request, pk):
    if request.user.role != "reader":
        return redirect("home")

    publisher = get_object_or_404(Publisher, id=pk)
    # Get user to be updated
    user = request.user

    user.subscribed_publishers.add(publisher)

    # Save modification to user
    user.save()
    return redirect("dashboard")


@login_required
def subscribe_to_journalist(request, pk):
    if request.user.role != "reader":
        return redirect("home")

    # Get the specific author / journalist
    author = get_object_or_404(get_user_model(), id=pk)

    # Get user to be updated
    user = request.user

    # Update the user subscribed_journalists with author
    user.subscribed_journalists.add(author)

    # Save the user
    user.save()

    return redirect("dashboard")
