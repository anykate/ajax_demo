from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from time import time


# Create your views here.
class AjaxHandlerView(View):
    def get(self, request):
        text = request.GET.get('request_text')
        t = time()
        if request.is_ajax():
            return JsonResponse({'response_text': str(t)}, status=200)
        return render(request, 'app/index.html')

    def post(self, request):
        text = request.POST.get('li_text')
        response_text = f"I've got {text}"
        if request.is_ajax():
            return JsonResponse({'response_text': response_text}, status=200)
