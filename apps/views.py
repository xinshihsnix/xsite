from django.shortcuts import render_to_response

# def custom_render()

def index(request):
    return render_to_response('../templates/index.html')