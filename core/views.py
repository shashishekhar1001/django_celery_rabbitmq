from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.

@csrf_exempt
def ajax_post_view(request):
    item_name = request.POST.get('Item')
    item = Item.objects.create(item=item_name)
    item.save()
    return JsonResponse("Message Queued ....", safe=False)


def sample_form(request):
    return render(request, "sample_form.html", {})
