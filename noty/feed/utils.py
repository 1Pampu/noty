from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate_items(request, items, items_per_page = 24):
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page', 1)

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return paginator, page