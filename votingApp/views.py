from django.shortcuts import redirect


def page_not_found(request):
    # do something
    return redirect('/election')
