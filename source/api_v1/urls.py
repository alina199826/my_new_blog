from django.urls import path, include

from api_v1.views import echo_view, get_token_view, article_view, add_view, subtract_view, multiply_view, divide_view
app_name = 'api_v1'

article_url = [
    path('', article_view)
]


urlpatterns = [

    path('echo/', echo_view),
    path('get_token/', get_token_view),
    path('article/', include(article_url)),
    path('add/', add_view),
    path('subtract/', subtract_view),
    path('multiply/', multiply_view),
    path('divide/', divide_view)
]