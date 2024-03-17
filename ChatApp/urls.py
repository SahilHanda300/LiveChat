from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('discover/',views.discover,name="discover"),
    path('safety/',views.safety,name="safety"),
    path('support/',views.support,name="support"),
    path('register/',views.register,name="register"),
    path('login/',views.loginPage,name="login"),
    path('supportSupport/',views.submittedSupport,name="supportSubmit"),
    
    
    path("loggedUser/",views.loggedInPage),
    path("userProfile/",views.userProfile,name="userProfile"),
    path("logout/",views.logoutWebsite,name="logout"),
    path("updateUserProfile/",views.userProfile,name="updateUser"),
    path("forgotPassword/",views.forgotPassword,name="forgotPassword"),
    path("jobChat/",views.jobChat,name="jobChat"),
    path("jobChat/",views.jobChat,name="jobChat"),
    path("vehicalChat/",views.vehicalChat,name="vehicalChat"),
    path("writersChat/",views.writers,name="writers"),
    path("friendsChat/",views.friends,name="friends"),
    path("bodyBuildingChat/",views.bodyBuilding,name="bodyBuilding"),
    path("multimediaChat/",views.multiMedia,name="multimedia"),
    path("medicoChat/",views.medico,name="medico"),
    path("technoChat/",views.techno,name="techno"),

    path("loggedIndex/",views.loggedIndex,name="loggedIndex")

]