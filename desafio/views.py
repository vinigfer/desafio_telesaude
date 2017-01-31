from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from desafio.models import Solicitante, Teleconsultor


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


class TeleconsultorForm(ModelForm):
    class Meta:
        model = Teleconsultor
        fields = ['nome', 'email', 'crm', 'data_formatura']


def teleconsultor_list(request, template_name='teleconsultor_list.html'):
    teleconsultores = Teleconsultor.objects.all()
    data = {}
    data['object_list'] = teleconsultores
    return render(request, template_name, data)


def teleconsultor_create(request, template_name='teleconsultor_form.html'):
    form = TeleconsultorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('teleconsultor_list')
    return render(request, template_name, {'form':form})


def teleconsultor_update(request, pk, template_name='teleconsultor_form.html'):
    teleconsultor = get_object_or_404(Teleconsultor, pk=pk)
    form = TeleconsultorForm(request.POST or None, instance=teleconsultor)
    if form.is_valid():
        form.save()
        return redirect('teleconsultor_list')
    return render(request, template_name, {'form':form})


def teleconsultor_delete(request, pk, template_name='teleconsultor_confirm_delete.html'):
    teleconsultor = get_object_or_404(Teleconsultor, pk=pk)
    if request.method == 'POST':
        teleconsultor.delete()
        return redirect('teleconsultor_list')
    return render(request, template_name, {'object':teleconsultor})