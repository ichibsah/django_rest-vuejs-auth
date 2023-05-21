from django.urls import path
#from django.urls import path, include

from games.views import HomeView, MathGameView, AnagramGameView

app_games = "games"
urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('math-game/', MathGameView.as_view(), name='math-game'),
    path('anagram-game/', AnagramGameView.as_view(), name='anagram-game'),
    #path("accounts/", include(("django.contrib.auth.urls", 'accounts'), namespace='accounts')),  # new
    
]