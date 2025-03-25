from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from sites.forms import CommentForm
from django.http import JsonResponse
from .models import Site, LikeDislike, Comment, CommentLikeDislike


@login_required(login_url='login')
def like_dislike(request, site_id, action):
    site = get_object_or_404(Site, id=site_id)
    existing_vote = LikeDislike.objects.filter(user=request.user, site=site).first()

    if existing_vote:
        if (action == 'like' and existing_vote.is_like) or (action == 'dislike' and not existing_vote.is_like):
            existing_vote.delete()  # Agar user o‘z ovozini qayta bossa, o‘chiramiz
        else:
            existing_vote.is_like = (action == 'like')
            existing_vote.save()
    else:
        LikeDislike.objects.create(user=request.user, site=site, is_like=(action == 'like'))

    return redirect('detail', site_id=site.id)


def sites_list(request):
    sites = Site.objects.all()
    context = {'sites': sites}
    return render(request, 'home.html', context)


def sites_detail(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    like_count = LikeDislike.objects.filter(site=site, is_like=True).count()
    dislike_count = LikeDislike.objects.filter(site=site, is_like=False).count()

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.site = site
            comment.user = request.user
            comment.save()
            return redirect('detail', site_id=site.id)
    else:
        form = CommentForm()

    comments = site.comments.filter(active=True)

    # 🚀 Kommentariyalarning layk/dislayk sonlarini qo‘shamiz
    for comment in comments:
        comment.like_count = comment.likes_dislikes.filter(is_like=True).count()
        comment.dislike_count = comment.likes_dislikes.filter(is_like=False).count()

    context = {
        'site': site,
        'comments': comments,
        'form': form,
        'like_count': like_count,
        'dislike_count': dislike_count,
    }

    return render(request, 'detail.html', context)


@login_required(login_url='login')
def comment_like_dislike(request, comment_id, action):
    comment = get_object_or_404(Comment, id=comment_id)
    existing_vote = CommentLikeDislike.objects.filter(user=request.user, comment=comment).first()

    if existing_vote:
        if (action == 'like' and existing_vote.is_like) or (action == 'dislike' and not existing_vote.is_like):
            existing_vote.delete()  # Agar user o‘z ovozini qayta bossa, o‘chiramiz
        else:
            existing_vote.is_like = (action == 'like')
            existing_vote.save()
    else:
        CommentLikeDislike.objects.create(user=request.user, comment=comment, is_like=(action == 'like'))

    return redirect('detail', site_id=comment.site.id)
