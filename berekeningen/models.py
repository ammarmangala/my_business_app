from django.db import models


class BerekeningLog(models.Model):
	omzet = models.DecimalField(max_digits=12, decimal_places=2)
	inkoopkosten = models.DecimalField(max_digits=12, decimal_places=2)
	brutomarge = models.DecimalField(max_digits=12, decimal_places=2)
	margepercentage = models.DecimalField(max_digits=7, decimal_places=2)
	aangemaakt_op = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'Omzet {self.omzet} - Inkoop {self.inkoopkosten}'
