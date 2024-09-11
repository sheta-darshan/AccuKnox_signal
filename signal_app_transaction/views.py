from django.http import HttpResponse
from .models import MyModel

def create_model(request):
    try:
        instance = MyModel(name="Test")
        instance.save()  # This will trigger the signal
        return HttpResponse("Model saved successfully")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")