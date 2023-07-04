from django.shortcuts import render
from testapp.forms import FeedBackForm
def feedBack_view(request):
    s=FeedBackForm()
    if request.method=='POST':
        s=FeedBackForm(request.POST)
        if s.is_valid():
            print('Form validation completed printing data')
            print('Name  of student:',s.cleaned_data['name'])
            print('RollNo of student:',s.cleaned_data['rollNo'])
            print('Email of student:',s.cleaned_data['email'])
            print('FeedBack of student:',s.cleaned_data['feedback'])
    return render(request,'testapp/feedback.html',{'form':s})
