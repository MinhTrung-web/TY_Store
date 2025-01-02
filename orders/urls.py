from django.urls import path
from orders import views

app_name = 'orders'
urlpatterns = [
    path('place', views.CreateOrder.as_view(), name='place'),
    path('my', views.MyOrders.as_view(), name='my'),
    path('<int:id>/details/', views.OrderDetail.as_view(), name='details'),  # Thêm dòng này
]

