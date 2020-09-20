from django.urls import path
from . import views

urlpatterns = [
    # User URLs
    path('signup', views.CreateUser, name="Create User"),
    path('users',views.UserDetail,name="User Detail"),
    path('login/<str:pk>', views.UserLogin, name="Users Login"),
    path('update/<str:pk>',views.UpdateUser,name="Update User"),
    path('delete/<str:pk>',views.DeleteUser,name="Delete User"),
    
    # AnonymousUser URLs
    path('anyuser',views.UserAnonymousDetail,name="User Any"),
    path('createanyuser',views.CreateUserAnonymous,name="Create Any User"),
    path('updateanyuser/<str:pk>',views.UpdateUserAnonymous,name="Update any user"),

    # Counsellor URLs
    path('counsellors',views.CounsellorDetail,name="Counsellor"),
    path('addcounsellor',views.AddCounsellor,name="Add Counsellor"),
    path('updatecounsellor/<str:pk>',views.UpdateCounsellor, name="Update Counsellor Profile"),
    path('deletecounsellor/<str:pk>', views.DeleteCounsellor,name="Delete Counsellor"),

    # Article URLs
    path('articles', views.ListArticle, name="List Article"),
    path('addarticle', views.AddArticle, name="Add Article"),
    path('updatearticle', views.UpdateArticle, name="Update Article"),
    path('deletearticle', views.DeleteArticle, name="Delete Article")
]