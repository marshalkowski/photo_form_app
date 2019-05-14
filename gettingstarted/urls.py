from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("dlphoto/", hello.views.dlphoto, name="dlphoto"),
    path("postdlphoto/", hello.views.postdlphoto, name="postdlphoto"),
    path("regphoto/", hello.views.regphoto, name="regphoto"),
    path("postregphoto/", hello.views.postregphoto, name="postregphoto"),
    path("carphoto/", hello.views.carphoto, name="carphoto"),
    path("postcarphoto/", hello.views.postcarphoto, name="postcarphoto"),
    path("userform/", hello.views.userform, name="userform"),
    path("postuserform/", hello.views.postuserform, name="postuserform"),
    path("quote/", hello.views.quote, name="quote"),
    path("updatedquote/", hello.views.updatedquote, name="updatedquote"),
    # path("proofphoto/", hello.views.proofphoto, name="proofphoto"),
    # path("showphoto/", hello.views.showphoto, name="showphoto"),
    path("admin/", admin.site.urls)

]
