from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
#post
#from django.template import RequestContext
#post

from webmail.models import Book


def test(request):
    return HttpResponse("test_views")

def ua_display_good(request):
    ua = request.META.get('HTTP_USER_AGENT','unknown')
    return HttpResponse('You browser is %s' %ua)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def login_webmail(request):
    if 'inputUserName' in request.POST and request.POST['inputUserName']:
        bookname = request.POST['inputUserName']
        books = Book.objects.filter(title__icontains=bookname)
        return render_to_response('search_book.html',{'books':books})
    else:
        books = "Not inputUserName"
        return render_to_response('search_book.html',{'books':books})
    
    
    
    
    
    