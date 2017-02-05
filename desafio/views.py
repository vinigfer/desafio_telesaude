from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from desafio.models import Solicitante, Teleconsultor, Solicitacao


def home(request, template_name='home.html'):
    data = {}
    return render(request, template_name, data)


class SolicitanteForm(ModelForm):
    class Meta:
        model = Solicitante
        fields = ['nome', 'email', 'cpf', 'telefone']

    def __init__(self, *args, **kwargs):
        super(SolicitanteForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].label = 'CPF'
        self.fields['cpf'].widget.attrs.update({
            'placeholder': 'Números apenas',
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'email@examplo.com',
        })


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
        error_messages = {
            'data_formatura': {
                'invalid': "Data inválida. Preencha no formato AAAA-MM-DD.",
            },
        }

    def __init__(self, *args, **kwargs):
        super(TeleconsultorForm, self).__init__(*args, **kwargs)
        self.fields['crm'].label = 'CRM'
        self.fields['crm'].widget.attrs.update({
            'placeholder': 'Números apenas',
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'email@examplo.com',
        })
        self.fields['data_formatura'].widget.attrs.update({
            'placeholder': 'AAAA-MM-DD',
        })



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


class SolicitacaoForm(ModelForm):
    class Meta:
        model = Solicitacao
        fields = ['texto', 'data', 'solicitante', 'teleconsultor']

    def __init__(self, *args, **kwargs):
        super(SolicitacaoForm, self).__init__(*args, **kwargs)
        self.fields['data'].widget.attrs.update({
            'placeholder': 'AAAA-MM-DD',
        })
        self.fields['texto'].widget.attrs.update({
            'placeholder': 'Digite aqui sua solicitação',
        })


def solicitacao_list(request, template_name='solicitacao_list.html'):
    solicitacoes = Solicitacao.objects.all()
    data = {}
    data['object_list'] = solicitacoes
    return render(request, template_name, data)


def solicitacao_create(request, template_name='solicitacao_form.html'):
    form = SolicitacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('solicitacao_list')
    return render(request, template_name, {'form':form})


def solicitacao_update(request, pk, template_name='solicitacao_form.html'):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    form = SolicitacaoForm(request.POST or None, instance=solicitacao)
    if form.is_valid():
        form.save()
        return redirect('solicitacao_list')
    return render(request, template_name, {'form':form})


def solicitacao_delete(request, pk, template_name='solicitacao_confirm_delete.html'):
    solicitacao = get_object_or_404(Solicitacao, pk=pk)
    if request.method == 'POST':
        solicitacao.delete()
        return redirect('solicitacao_list')
    return render(request, template_name, {'object':solicitacao})
