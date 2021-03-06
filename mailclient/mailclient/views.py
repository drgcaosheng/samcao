from django.http import HttpResponse
import datetime
from django.shortcuts import render_to_response
#post
from django.template import RequestContext
#post
def hello(request):
    #return HttpResponse('Hello World!')
    return render_to_response('index.html')
    
    
def current_datetime(request):
    now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" %now
    #return HttpResponse(html)
    return render_to_response('current_datetime.html',{'current_time':now})
    
def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset,dt)
    #return HttpResponse(html)
    return render_to_response("hours_ahead.html",{'hour_offset':offset,'next_time':dt})
    
def webmail(request):
    return render_to_response('index.html',context_instance=RequestContext(request))    