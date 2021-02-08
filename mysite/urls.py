from django.contrib import admin
from django.urls import path, include    # include 추가
# from bookmark.views import BookmarkLV, BookmarkDV
from mysite.views import HomeView    # 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),      # 추가, 메인페이지
    path('bookmark/', include('bookmark.urls')),    # 추가
    path('blog/', include('blog.urls')),            # 추가

    # path('bookmark/', BookmarkLV.as_view(), name='index'),
    # path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
]





# from django.contrib import admin
# from django.urls import path, include
# from .views import HomeView
# # from bookmark.views import BookmarkLV, BookmarkDV
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', HomeView.as_view(), name='home'),    # 메인페이지
#     path('bookmark/', include('bookmark.urls')),
#     path('blog/', include('blog.urls')),
#
#     # path('bookmark/', BookmarkLV.as_view(), name='index'),
#     # path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),
# ]
