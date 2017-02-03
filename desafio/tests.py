from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Solicitante


class SolicitanteTests(TestCase):
    def test_read_after_inserting_with_zero_solicitantes(self):
        Solicitante.objects.create(nome="Jose", email="jose@email.com",
                                   cpf="01022233345", telefone="5133337777")
        response = self.client.get(reverse('solicitante_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jose")
        self.assertQuerysetEqual(response.context['object_list'],
                                 ['<Solicitante: Jose (01022233345)>'])


