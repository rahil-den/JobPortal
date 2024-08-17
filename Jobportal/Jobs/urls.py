from django.urls import path,include
from .import views

urlpatterns = [
    # path("sec/",views.home.as_view()),
    path("index/",views.index),
    path("about/",views.about),
    path("blog-single/",views.blog_single),
    path("blog/",views.blog),
    path("contact/",views.contact),
    path("faq/",views.faq),
    path("gallery/",views.gallery),
    path("job-listings/",views.job_listings),
    path("job-single/",views.job_single),
    path("login/",views.user_login),
    path("portfolio-single/",views.portfolio_single),
    path("portfolio/",views.portfolio),
    path("post-job/",views.post_job),
    path("service-single/",views.service_single),
    path("services/",views.services),
    path("testimonials/",views.testimonials),
    path("signin/",views.register),
    path("Crud/",views.crud),
    path('delete/<int:id>/',views.delete_user),
    # path('update/<int:id>/',views.update),


    
    
]
 