from django.shortcuts import render, Http404, HttpResponse
from .models import Contact
from django.contrib import messages
from Blog.models import Post
from SilverFox import settings

# Create your views here.


def home(r):

    Posts = Post.objects.filter(Sno=1)
    Posts2 = Post.objects.filter(Sno=2).first()
    Posts3 = Post.objects.filter(Sno=3).first()
    Posts4 = Post.objects.filter(Sno=4).first()

    Posts |= Post.objects.filter(Sno=Posts2.Sno)
    Posts |= Post.objects.filter(Sno=Posts3.Sno)
    Posts |= Post.objects.filter(Sno=Posts4.Sno)

    return render(r, 'Home/Home.html', {'Posts': Posts})


def about(r):
    return render(r, 'Home/About.html')


def search(r):
    Query = r.GET['query']
    Message = ''
    Heading = f'Search Results For {Query}'
    Fb = ''
    
    Posts = Post.objects.filter(Title__icontains=Query)
    if Posts.count() > 2:
         pass
    else:
         Fb = 'fixed-bottom'

    if not Posts:
        Heading = f'No Search Result Found For {Query}'
        messages.error(r,'Please Check Your Query Again')
        Fb = 'fixed-bottom'
        

    else:
          messages.success(r,f'{Posts.count()} Related Posts Found')
    return render(r, 'Home/Search.html', {'Posts': Posts,  'Heading': Heading,'Fb':Fb})


def contact(r):
    if r.method == 'POST':
        name = r.POST['Name']
        phone = r.POST['Phone']
        email = r.POST['Email']
        content = r.POST['Content']

        if len(name) < 3 or len(phone) < 10 or len(phone) > 13 or len(email) < 6 or len(content) < 5:
            messages.error(r, "Please Fill The Form Correctly and Carefully")

        else:
            try:
                c = Contact(Name=name, Phone=phone,
                            Email=email, Content=content)
                c.save()
                messages.success(
                    r, f"{name}, Your Message Has Been Send Succesfully")

            except Exception as e:
                messages.error(
                    r, f"{name}, Something went Wrong, Please retry to Submit Your Message")

    return render(r, 'Home/Contact.html')
