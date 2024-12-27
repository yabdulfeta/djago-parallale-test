from django.urls import path
from .views import AddView, SubtractView, MultiplyView, DivideView

urlpatterns = [
    path('add/', AddView.as_view(), name='add'),
    path('subtract/', SubtractView.as_view(), name='subtract'),
    path('multiply/', MultiplyView.as_view(), name='multiply'),
    path('divide/', DivideView.as_view(), name='divide'),
]