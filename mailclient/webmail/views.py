from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

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
