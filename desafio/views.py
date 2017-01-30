from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from desafio.models import Solicitante


class SolicitanteForm(ModelForm):
    class Meta:
        model = Solicitante
        fields = ['nome', 'email', 'cpf', 'telefone']


def solicitante_list(request, template_name='solicitante_list.html'):
    solicitantes = Solicitante.objects.all()
    data = {}
    data['object_list'] = solicitantes
    return render(request, template_name, data)


def solicitante_create(request, template_name='solicitante_form.html'):
    form = SolicitanteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('solicitante_list')
    return render(request, template_name, {'form':form})


def solicitante_update(request, pk, template_name='solicitante_form.html'):
    solicitante = get_object_or_404(Solicitante, pk=pk)
    form = SolicitanteForm(request.POST or None, instance=solicitante)
    if form.is_valid():
        form.save()
        return redirect('solicitante_list')
    return render(request, template_name, {'form':form})


def solicitante_delete(request, pk, template_name='solicitante_confirm_delete.html'):
    solicitante = get_object_or_404(Solicitante, pk=pk)
    if request.method == 'POST':
        solicitante.delete()
        return redirect('solicitante_list')
    return render(request, template_name, {'object':solicitante})
