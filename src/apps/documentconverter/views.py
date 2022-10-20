from django.views.generic import ListView, CreateView

from .models import Document, Chapter

# Home page view
class Home(ListView):
    model = Chapter
    template_name = 'pages/home.html'
    context_object_name = 'chapters'

class Upload(CreateView):
    model = Document
    template_name = 'pages/upload.html'
    fields = ['file']
    success_url = '/'