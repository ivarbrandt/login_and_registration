from django.shortcuts import render, redirect
from . models import Message, Comment
from apps.login_and_reg.models import User

def postmessage(request):
    print("The post message method is running")
    if 'user_id' in request.session:
        message = Message.objects.create(message_text=request.POST['message_text'], user=User.objects.get(id=request.session['user_id']))
        return redirect('/wall')
    else:
        return redirect('/wall')

def postcomment(request):
    print("The post comment method is running")
    if 'user_id' in request.session:
        comment = Comment.objects.create(comment_text=request.POST['comment_text'], user=User.objects.get(id=request.session['user_id']), message=Message.objects.get(id=request.POST['message_id']))
        return redirect('/wall')
    else:
        return redirect('/wall')


def mainpage(request):
    if 'user_id' in request.session:
        context = {
            "user": User.objects.get(id=request.session['user_id']),
            "messages": Message.objects.all()
        }
        return render(request, 'The_Wall/mainpage.html', context)
    else:
        return redirect('/')

def deletemessage(request, id):
    if 'user_id' in request.session:
        c=Message.objects.get(id=id)
        c.delete()
        return redirect('/wall')
    else:
        return redirect('/wall')

# Create your views here.
