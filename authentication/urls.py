from django.urls import path
from . import views

urlpatterns = [
    # User URLs
    path('signup', views.CreateUser, name="Create User"),
    path('users',views.UserDetail,name="User Detail"),
    path('login/<str:pk>', views.UserLogin, name="Users Login"),
    path('update/<str:pk>',views.UpdateUser,name="Update User"),
    path('delete/<str:pk>',views.DeleteUser,name="Delete User"),
    path('user/<str:pk>',views.ParticularUserDetail,name="User Detail"),

    # Mental State URLs
    path('mentalstate/<str:pk>', views.ShowMentalStates, name="Mental States"),
    
    # AnonymousUser URLs
    # path('anyuser',views.UserAnonymousDetail,name="User Any"),
    #path('anoyuser/<str:pk>', views.ParticularAnonymousUserDetail, "Anonymous User Details"),
    # path('createanyuser',views.CreateUserAnonymous,name="Create Any User"),
    # path('deleteanyuser/<str:pk>',views.DeleteUserAnonymous,name="Update any user"),

    # Counsellor URLs
    path('counsellors',views.CounsellorDetail,name="Counsellor"),
    path('addcounsellor',views.AddCounsellor,name="Add Counsellor"),
    path('updatecounsellor/<str:pk>',views.UpdateCounsellor, name="Update Counsellor Profile"),
    path('deletecounsellor/<str:pk>', views.DeleteCounsellor,name="Delete Counsellor"),

    # Article URLs
    path('articles', views.ListArticle, name="List Article"),
    path('addarticle', views.AddArticle, name="Add Article"),
    path('updatearticle', views.UpdateArticle, name="Update Article"),
    path('deletearticle', views.DeleteArticle, name="Delete Article"),


    #Charts URLs
    path('agemorbiditychart',views.DisplayAgeMorbidityChart,name="Age Morbidity Chart"),
    path('statedisorderchart',views.DisplayStateDisorderChart,name="State Disorder Chart"),
    path('suicidalriskchart',views.DisplaySuicidalRiskChart,name="Suicidal Risk Chart"),
    path('humanresourceschart',views.DisplayHumanResourcesChart,name="Human Resources Chart"),

    #Emotion Capture URLs
    path('video_feed', views.video_feed, name='video_feed'),

    #Chatbot URLs
    path('chatbot',views.Chat,name="Chatbot"),
    path('mentalhealthchart/<str:pk>', views.MentalHealthChart, name="Mental Health Chart"),
]