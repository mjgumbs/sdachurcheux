import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required

from .models import Image, ImageCategory

@csrf_exempt
@require_POST
@login_required
def upload_photos(request):
    images = []
    for f in request.FILES.getlist("file"):
        category = ImageCategory.objects.get(title="Page")
        obj = Image.objects.create(title='test',file=f, category=category)
        images.append({"filelink": obj.get_absolute_url()})
    return HttpResponse(json.dumps(images))


@login_required
def recent_photos(request):
    images = [
        {"thumb": obj.get_absolute_url(), "image": obj.get_absolute_url()}
        for obj in Image.objects.filter()[:20]
    ]
    return HttpResponse(json.dumps(images))