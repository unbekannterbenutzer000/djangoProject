from django.urls import path
from .views import Bloglist, BlogDetailView, AboutPageView, SearchResultsView, SearchCategory_1, SearchCategory_2, \
    SearchCategory_3, Bloglist1, UserDetails, Registration, Login, logout_user

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', Bloglist.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('impo/', SearchCategory_1.as_view(), name='category1'),
    path('Rus/', SearchCategory_2.as_view(), name='category2'),
    path('Wrld/', SearchCategory_3.as_view(), name='category3'),
    path('show10/', Bloglist1.as_view(), name='home1'),
    path('reg/', Registration.as_view(), name='reg'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('user/<str:pk>/', UserDetails.as_view(), name='user')
]
