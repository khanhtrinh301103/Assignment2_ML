from django.shortcuts import render, redirect
from .forms import ImageUploadForm  # Make sure to create this form in forms.py
from .ml_model import predict_category  # Assuming you have this function ready as discussed
from .ml_model import classify_furniture

def homepage(request):
    return render(request, 'homepage.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()  # Save the uploaded file
            category, style = classify_furniture(instance.image.path)  # Get both predictions
            return render(request, 'homepage.html', {'category': category, 'style': style})  # Pass results back to template
    else:
        form = ImageUploadForm()
    return render(request, 'homepage.html', {'form': form})

