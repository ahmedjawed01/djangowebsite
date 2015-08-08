
from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext,render
import json
from .models import *
from django.http import HttpResponseRedirect
import re
import time

def home(request):

    
    meta_title="Home"
    meta_descr="my description"
    header_title="My Django Website"
    title="My Article"
    content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras at metus ut elit ultricies interdum. Donec vel risus mauris. Quisque facilisis sit amet libero vel fermentum. Sed sit amet arcu a neque placerat lobortis quis at dui. Suspendisse nec arcu varius, interdum mi ac, viverra tellus. Aenean placerat lacinia diam, dictum mollis augue accumsan in. Aenean vel fringilla mauris. Phasellus non lorem sed augue pulvinar aliquam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam feugiat quam nisi, id viverra libero auctor at. Fusce sed quam cursus, euismod massa id, dapibus velit. Curabitur nunc ex, semper a mattis vel, accumsan et nulla."
   
    return render_to_response("page.html", 
            { 
            "title":title,
            "content":content,
            "meta_title":meta_title,
            "meta_descr":meta_descr,
            "header_title":header_title,
           
            }  
            ,context_instance=RequestContext(request))


def article(request,page_slug=""):

    header_title="Article 2"
    title="My title 2"
    meta_descr="Article description "
    content="lorem ipsum test info"
    header_title="My title 2"
    slug="/"+page_slug

  
    return render_to_response("page.html", 
            { 
            
            "meta_title":title,
            "meta_descr":meta_descr,
            "title":title,
            "content":content,
            "slug":slug,
            "header_title":header_title,
            }  
            ,context_instance=RequestContext(request))


def generate_sitemap(request):
    sitemap_data="<?xml version=\"1.0\" encoding=\"UTF-8\"?><urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">"
    sitemap_data+="<url><loc>http://www.djangotutsme.com/</loc><lastmod>2014-10-10</lastmod><changefreq>monthly</changefreq><priority>1.0</priority></url>"
    pages=Pages.objects.filter(active=True)
    for data in pages:
        sitemap_data+="<url><loc>http://www.djangotutsme.com"+data.slug+"</loc><lastmod>"+str(data.date).split()[0]+"</lastmod><changefreq>monthly</changefreq><priority>0.5</priority></url>"

    sitemap_data+="</urlset>"  
    return HttpResponse(sitemap_data,content_type="application/xhtml+xml")

