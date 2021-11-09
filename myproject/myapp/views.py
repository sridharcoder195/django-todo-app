from django.shortcuts import render, redirect
from .models import a
from .form import myform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


class lista(ListView):
    model = a
    template_name = 'index.html'
    context_object_name = 'obj'


class detail(DetailView):
    model = a
    template_name = 'detail.html'
    context_object_name = 'i'


class updatetask(UpdateView):
    model = a
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.id})


class deletetask(DeleteView):
    model = a
    template_name = 'detele.html'
    success_url = reverse_lazy('list')


def index(request):
    obj = a.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        s = a(name=name, priority=priority, date=date)
        s.save()
    return render(request, 'index.html', {'obj': obj})


def delete(request, ida):
    a1 = a.objects.get(id=ida)
    if request.method == 'POST':
        a1.delete()
        return redirect('/')
    return render(request, 'detele.html', {'a1': a1})


def update(request, ida):
    task = a.objects.get(id=ida)
    form = myform(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form})
