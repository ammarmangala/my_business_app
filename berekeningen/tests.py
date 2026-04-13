from django.test import TestCase


class BerekeningenViewTests(TestCase):
	def test_home_page_renders_form(self):
		response = self.client.get('/')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Brutomarge calculator')
		self.assertContains(response, 'Omzet')
		self.assertContains(response, 'Inkoopkosten')

	def test_valid_post_calculates_results(self):
		response = self.client.post('/', {'omzet': '12500', 'inkoopkosten': '8300'})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Brutomarge')
		self.assertContains(response, '4200.00')
		self.assertContains(response, '33.60')

	def test_invalid_post_shows_error(self):
		response = self.client.post('/', {'omzet': 'abc', 'inkoopkosten': '8300'})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Vul geldige numerieke waarden in voor beide velden.')

	def test_zero_revenue_shows_error(self):
		response = self.client.post('/', {'omzet': '0', 'inkoopkosten': '100'})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Omzet moet groter zijn dan 0 om het margepercentage te berekenen.')
