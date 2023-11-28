import time

from celery import shared_task
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question


@shared_task()
def expensive_task(x, y):
    time.sleep(20)
    return x + y
