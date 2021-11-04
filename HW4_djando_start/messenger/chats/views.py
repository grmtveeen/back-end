from django.shortcuts import render
from django.http.response import JsonResponse


def chat_detail(request, chat_id):
    return JsonResponse({'chat': chat_id})
