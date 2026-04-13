from decimal import Decimal, InvalidOperation

from django.shortcuts import render

from .models import BerekeningLog


def _parse_decimal(value: str) -> Decimal:
	return Decimal(value.replace(',', '.'))


def home(request):
	context = {
		'omzet': '',
		'inkoopkosten': '',
		'brutomarge': None,
		'margepercentage': None,
		'show_results': False,
		'error': None,
	}

	if request.method == 'POST':
		omzet_raw = request.POST.get('omzet', '').strip()
		inkoopkosten_raw = request.POST.get('inkoopkosten', '').strip()
		context['omzet'] = omzet_raw
		context['inkoopkosten'] = inkoopkosten_raw

		try:
			omzet = _parse_decimal(omzet_raw)
			inkoopkosten = _parse_decimal(inkoopkosten_raw)

			brutomarge = omzet - inkoopkosten

			if omzet == 0:
				context['error'] = 'Omzet moet groter zijn dan 0 om het margepercentage te berekenen.'
			else:
				margepercentage = (brutomarge / omzet) * Decimal('100')
				brutomarge = brutomarge.quantize(Decimal('0.01'))
				margepercentage = margepercentage.quantize(Decimal('0.01'))

				context['brutomarge'] = brutomarge
				context['margepercentage'] = margepercentage
				context['show_results'] = True

				BerekeningLog.objects.create(
					omzet=omzet.quantize(Decimal('0.01')),
					inkoopkosten=inkoopkosten.quantize(Decimal('0.01')),
					brutomarge=brutomarge,
					margepercentage=margepercentage,
				)
		except (InvalidOperation, AttributeError):
			context['error'] = 'Vul geldige numerieke waarden in voor beide velden.'

	return render(request, 'berekeningen/home.html', context)
