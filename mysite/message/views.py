from django.shortcuts import render, redirect, HttpResponse
from .forms import MessageCreationForm
from .models import Message
from django.views.generic import ListView

def send_message(request):
	if request.method == "POST":
		form = MessageCreationForm(request.POST)
		if form.is_valid():
			m_form = form.save(commit=False)
			m_form.sender = request.user.EMPLID
			m_form.save()
			return redirect('home')
	else:
		form = MessageCreationForm()

	return render(request, 'send_message.html', {'form': form})

def view_inbox(request):
	num_messages = len(Message.objects.filter(receiver = request.user.EMPLID))
	print(num_messages)
	return render(request, 'view_messages.html', {
		'messages' : Message.objects.all(),
		'num_messages' : num_messages,
	})

'''class InboxListView(ListView):
    model = Message 
    template_name = 'view_messages.html'
    context_object_name = 'messages'
    ordering = ['-timestamp']
'''
def delete_message(request):
	inbox = list(Message.objects.filter(receiver = request.user.EMPLID))
	if request.method == "POST":
		Message.objects.filter(pk = request.POST.get('to-delete')).delete()
		return redirect('delete_message')
	return render(request, 'delete_message.html',{'inbox': inbox})
















