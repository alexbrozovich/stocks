from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='stocks'
urlpatterns = [
    path('', views.home, name='home'),
    path('<str:ticker_id>/', views.detail, name='detail'),
    path('tracking', views.tracking, name='tracking'),
    path('add/tracknewstock', views.tracknewstock, name='tracknewstock'),
    path('add_tracked_stock', views.add_tracked_stock, name='add_tracked_stock'),
    path('home', views.home, name='home'),
    path('tracked_graphs', views.tracked_graphs, name='tracked_graphs'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
