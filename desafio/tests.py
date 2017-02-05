from django.test import TestCase
from django.core.urlresolvers import reverse
from django.db import IntegrityError

from .models import Solicitante, Teleconsultor, Solicitacao

from datetime import datetime


class SolicitanteTests(TestCase):
    def test_create(self):
        Solicitante.objects.create(nome="Jose", email="jose@email.com",
                                   cpf="01022233345", telefone="5133337777")
        response = self.client.get(reverse('solicitante_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jose")
        self.assertQuerysetEqual(response.context['object_list'],
                                 ['<Solicitante: Jose (01022233345)>'])

    def test_read(self):
        response = self.client.get(reverse('solicitante_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<tbody>\n        \n    </tbody>")
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_update(self):
        joao = Solicitante.objects.create(nome="João", email="joao@email.com",
                                          cpf="01099933345",
                                          telefone="5133337777")
        response = self.client.get(reverse('solicitante_list'))
        self.assertQuerysetEqual(response.context['object_list'],
                                 ['<Solicitante: João (01099933345)>'])

        joao.nome = "Joana"
        joao.save()
        response = self.client.get(reverse('solicitante_list'))
        self.assertQuerysetEqual(response.context['object_list'],
                                 ['<Solicitante: Joana (01099933345)>'])

    def test_delete(self):
        Solicitante.objects.create(nome="Karina", email="karina@email.com",
                                   cpf="01047233345", telefone="5133337777")
        response = self.client.get(reverse('solicitante_list'))
        self.assertEqual(len(response.context['object_list']), 1)

        Solicitante.objects.filter(cpf="01047233345").delete()
        response = self.client.get(reverse('solicitante_list'))
        self.assertEqual(len(response.context['object_list']), 0)

    def test_duas_pessoas_com_mesmo_cpf(self):
        try:
            Solicitante.objects.create(nome="Jose", email="jose@email.com",
                                       cpf="01022233345", telefone="5133337777")
            Solicitante.objects.create(nome="Maria", email="maria@email.com",
                                       cpf="01022233345", telefone="5133337777")
        except IntegrityError as e:
            if 'unique constraint' in e.__str__():
                self.assertTrue(True)
            else:
                raise Exception("Um erro inesperado ocorreu")


class TeleconsultorTests(TestCase):
    def test_create(self):
        Teleconsultor.objects.create(nome="Jaqueline",
                                     data_formatura="2010-01-27",
                                     crm="57432", email="jaqueline@email.com")
        response = self.client.get(reverse('teleconsultor_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jaqueline")
        self.assertQuerysetEqual(response.context['object_list'],
                                 ['<Teleconsultor: Jaqueline (57432)>'])

    def test_read(self):
        response = self.client.get(reverse('teleconsultor_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<tbody>\n        \n    </tbody>")
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_update(self):
        jaqueline = Teleconsultor.objects.create(
                                     nome="Jaqueline",
                                     data_formatura="2010-01-27",
                                     crm="57432", email="jaqueline@email.com")
        response = self.client.get(reverse('teleconsultor_list'))
        self.assertQuerysetEqual(response.context['object_list'],
                                 ['<Teleconsultor: Jaqueline (57432)>'])

        jaqueline.nome = "Karina Dalsin"
        jaqueline.save()
        response = self.client.get(reverse('teleconsultor_list'))
        self.assertQuerysetEqual(response.context['object_list'],
                                 ['<Teleconsultor: Karina Dalsin (57432)>'])

    def test_delete(self):
        Teleconsultor.objects.create(nome="Karina", data_formatura="2010-01-27",
                                     crm="57432", email="karina@email.com")
        response = self.client.get(reverse('teleconsultor_list'))
        self.assertEqual(len(response.context['object_list']), 1)

        Teleconsultor.objects.filter(crm="57432").delete()
        response = self.client.get(reverse('teleconsultor_list'))
        self.assertEqual(len(response.context['object_list']), 0)

    def test_duas_pessoas_com_mesmo_crm(self):
        try:
            Teleconsultor.objects.create(nome="Karina",
                                         data_formatura="2010-01-27",
                                         crm="57432", email="karina@email.com")
            Teleconsultor.objects.create(nome="Leticia",
                                         data_formatura="2008-07-19",
                                         crm="57432", email="leticia@email.com")
        except IntegrityError as e:
            if 'unique constraint' in e.__str__():
                self.assertTrue(True)
            else:
                raise Exception("Um erro inesperado ocorreu")


class SolicitacaoTests(TestCase):
    def create_solicitante_e_teleconsultor(self):
        teleconsultor = Teleconsultor.objects.create(
                                    nome="Jaqueline",
                                    data_formatura="2010-01-27",
                                    crm="57432", email="jaqueline@email.com")
        solicitante = Solicitante.objects.create(
                                    nome="Jose",
                                    email="jose@email.com",
                                    cpf="01022233345", telefone="5133337777")
        return teleconsultor, solicitante

    def test_create(self):
        teleconsultor, solicitante = self.create_solicitante_e_teleconsultor()
        Solicitacao.objects.create(texto="Solicito uma teleconsultoria",
                                   data="2017-02-06",
                                   solicitante=solicitante,
                                   teleconsultor=teleconsultor)
        response = self.client.get(reverse('solicitacao_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'],
                                 ['<Solicitacao: Jose - 2017-02-06>'])

    def test_read(self):
        teleconsultor, solicitante = self.create_solicitante_e_teleconsultor()
        Solicitacao.objects.create(texto="Solicito uma teleconsultoria",
                                   data="2017-02-06",
                                   solicitante=solicitante,
                                   teleconsultor=teleconsultor)
        response = self.client.get(reverse('solicitacao_list'))
        self.assertEqual(len(response.context['object_list']), 1)

    def test_update(self):
        teleconsultor, solicitante = self.create_solicitante_e_teleconsultor()
        solicitacao = Solicitacao.objects.create(
                                    texto="Solicito uma teleconsultoria",
                                    data="2017-02-06",
                                    solicitante=solicitante,
                                    teleconsultor=teleconsultor)
        response = self.client.get(reverse('solicitacao_list'))
        self.assertQuerysetEqual(response.context['object_list'],
                                 ['<Solicitacao: Jose - 2017-02-06>'])

        hoje = datetime.now()
        solicitacao.data = hoje
        solicitacao.save()
        hoje_yyyy_mm_dd = hoje.strftime('%Y-%m-%d')
        response = self.client.get(reverse('solicitacao_list'))
        self.assertQuerysetEqual(response.context['object_list'],
                                 ['<Solicitacao: Jose - ' +
                                  hoje_yyyy_mm_dd + '>'])

    def test_delete(self):
        teleconsultor, solicitante = self.create_solicitante_e_teleconsultor()
        Solicitacao.objects.create(
            texto="Solicito uma teleconsultoria",
            data="2017-02-06",
            solicitante=solicitante,
            teleconsultor=teleconsultor)
        response = self.client.get(reverse('solicitacao_list'))
        self.assertEqual(len(response.context['object_list']), 1)

        Solicitacao.objects.filter(
            solicitante=solicitante,
            data="2017-02-06").delete()
        response = self.client.get(reverse('solicitacao_list'))
        self.assertEqual(len(response.context['object_list']), 0)

    def test_mesmo_solicitante_duas_solicitacoes_em_um_dia(self):
        try:
            self.create_solicitante_e_teleconsultor()
            self.create_solicitante_e_teleconsultor()
        except IntegrityError as e:
            if 'unique constraint' in e.__str__():
                self.assertTrue(True)
            else:
                raise Exception("Um erro inesperado ocorreu")
