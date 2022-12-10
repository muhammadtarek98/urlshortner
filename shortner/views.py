from django.shortcuts import render ,redirect
import uuid
from django.http import HttpRequest, HttpResponse
from .models import Url


# Create your views here.
def index(request):
    return render(request=request,
                  template_name=r'E:\programming practices\pythons\metacourse\urlshortner\templates\base.html')


def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def show_created_url(request,pk):
    url_details=Url.objects.get(uuid=pk)
    return redirect("https://"+url_details.link)
