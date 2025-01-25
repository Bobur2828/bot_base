from django.urls import path

from main.views.get_webhook import handle_updates
urlpatterns = [
    path("webhook/<str:bot_id>/updates", handle_updates),

]



