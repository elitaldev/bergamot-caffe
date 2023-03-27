from django.urls import path

urlpattern = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
