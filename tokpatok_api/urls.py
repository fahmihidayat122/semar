from django.urls import path
from tokpatok_api.views import TokpatokCreate, TokpatokList, TokpatokDetail

urlpatterns = [
    path('', TokpatokCreate.as_view()),
    path('list/', TokpatokList.as_view()),
    path('<int:pk>', TokpatokDetail.as_view())
    ]


