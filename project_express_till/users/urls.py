from django.urls import path
from project_express_till.users import views

from project_express_till.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    video_feeds,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("video_feed/", view=video_feeds,name="video_feed"),
]
