from django.test import TestCase
from django.core.urlresolvers import reverse
from django.db import IntegrityError

from .models import Solicitante


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
        self.assertContains(response, "<ul>\n    \n</ul>")
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
