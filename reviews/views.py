from django.shortcuts import render, redirect

from reviews.models import Review
from reviews.forms import ReviewForm

# Create your views here.
def index(request):
    reviews = Review.objects.order_by('-pk')
    
    context = {
        'reviews' : reviews
    }
    return render(request, 'reviews/index.html', context)

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