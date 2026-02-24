from django.shortcuts import render, redirect
from reviews.models import Review
from reviews.forms import ReviewForm


def reviews_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()

    reviews = Review.objects.all().order_by('-id')
    return render(request, 'reviews.html', {'reviews': reviews, 'form': form})
