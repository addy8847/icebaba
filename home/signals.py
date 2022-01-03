from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver


@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("----------")
    print("this is login run in signal")
    print("sender:",sender)
    print("request:",request)
    print("User:",user)
    print(f"key word arguments:{kwargs}")
# user_logged_in.connect(login_success,sender=User)    


@receiver(user_logged_out,sender=User)
def logout_success(sender,request,user,**kwargs):
    print("----------")
    print("this is logout run in signal")
    print("sender:",sender)
    print("request:",request)
    print("User:",user)
    print(f"key word arguments:{kwargs}")
# user_logged_out.connect(logout_success,sender=User)



@receiver(user_login_failed)
def login_failed(sender,request,credentials,**kwargs):
    print("----------")
    print("this is login failed run  in signal")
    print("sender:",sender)
    print("request:",request)
    print("cred:",credentials)
    print(f"key word arguments:{kwargs}")
# user_login_failed.connect(login_failed)