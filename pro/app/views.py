from django.shortcuts import render
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Get cleaned data
            data = form.cleaned_data
            return render(request, 'feedback/thank_you.html', {'data': data})
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback/feedback_form.html', {'form': form})
#done
#gjghi
    

