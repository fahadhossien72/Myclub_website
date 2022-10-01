from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . models import *
def paginatorVenue(request, venues, results):
    page = request.GET.get('page')
    paginator = Paginator(venues, results)

    try:
        venues = paginator.page(page)
    except PageNotAnInteger:
        page=1
        venues = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        venues = paginator.page(page)

    left_index = (int(page)- 3)
    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 4)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages 

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages

    custom_range = range(left_index, right_index)
    return venues, paginator, custom_range