
from django.db import models
from django.utils.text import slugify
from django.db.models import Q
#python manage.py makemigrations myapp
#python manage.py sqlmigrate myapp 
#python manage.py shell
########## FIELD TYPES #####################################################
# charfield -  name = models.CharField(max_length=256,null=True,blank=True) 
# boolean - active=models.BooleanField(default=False)
# integer - number = models.IntegerField() 
# textfield - comment = models.TextField(null=True,default=None,blank=True) 
# datetime - modified  = models.DateTimeField()
# datetime - date = models.DateTimeField(auto_now_add=True)
# imagefield - image = models.ImageField(upload_to = "media/", default = "media/no-img.jpg") #pip install Pillow
# manytomany - category = models.ManyToManyField(Category) 
# foreignkey -  user = models.ForeignKey(Users)
# choices -SHIRT_SIZES = (("S", "Small"),("M", "Medium"), ("L", "Large"),)
#         - shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
############################################################################

######### QUERYS ###########################################################
# slideshows = SLideshow.objects.filter()
#user.objects.get(email=email)
#Category.objects.filter(tree__startswith="parent",disable=False)
#Category.objects.filter(Q(tree__contains=children) & ~Q(tree__contains="-") & Q(disable=False))
#Invoices.objects.filter().order_by("-id")
#Subcat.objects.get(variants__name=subcategory)
#Poi.objects.filter(name__icontains=search_input)
#Poi.objects.filter(variants__name__icontains=search_input)

############################################################################


#class Settings(models.Model):

    #title = models.CharField(max_length=256) 
    #value = models.TextField(null=True,default=None,blank=True)
  
    

    #def __unicode__(self):
        #return self.title

    #class Meta:
        #verbose_name_plural="Settings"


#class Pages(models.Model):

    #title = models.CharField(max_length=256,null=True) 
    #short_descr = models.CharField(max_length=256,null=True,blank=True) 
    #content=models.TextField(null=True,default="")
    #slug = models.CharField(max_length=256,null=True,default="",blank=True) 
    #active = models.BooleanField(default=True)
    #date = models.DateTimeField(auto_now_add=True)
  
    #def slug_link(self):
        #return "<a target=\"_blank\" href=\"%s\">%s</a>" % (self.slug,self.slug)
    #slug_link.allow_tags = True


    #def __unicode__(self):
        #return self.title 

    
    #def save(self):
    
        #if Pages.objects.filter(title=self.title).count()>0:
            #title=self.title+str(self.id)
        #else:
            #title=self.title
        
        #self.slug ="/%s" % (slugify(self.title))
        
        #super(Pages, self).save()


    #class Meta:
        #verbose_name_plural="Pages"

