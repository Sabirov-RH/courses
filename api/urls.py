from django.urls import path, include
from api.models import CourseResourse, CategoryResourse
from tastypie.api import Api

api = Api(api_name = 'v1')
api.register(CourseResourse())
api.register(CategoryResourse())

# api/v1/courses/1
# api/v1/categories

urlpatterns = [
    path('', include(api.urls), name = 'index')
]
