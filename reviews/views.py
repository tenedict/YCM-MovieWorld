from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from reviews.models import Review
from reviews.forms import ReviewForm

# Create your views here.
def index(request):
    reviews = Review.objects.order_by('-pk')
    
    context = {
        'reviews' : reviews
    }
    return render(request, 'reviews/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save()
            return redirect('reviews:detail', review.pk)
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form
    }
    return render(request, 'reviews/create.html', context)

# 작성글 상세 페이지
def detail(request, pk):
    review = Review.objects.get(pk=pk)
    
    context = {
        'review': review,
    }

    return render(request, 'reviews/detail.html', context)

# 글 수정 페이지 및 리뷰 데이터 수정
@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'review': review,
    }

    return render(request, 'reviews/update.html', context)

# 글 삭제
@login_required
def delete(request, pk):
    review = Review.objects.get(pk=pk)

    review.delete()

    return redirect('reviews:index')