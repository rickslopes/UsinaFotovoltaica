#BY RICARDO SOUZA LOPES - rickslopes@gmail.com
#LICENÇA MIT

import math

class CalculoUsinaSolar:
    def __init__(self, potencia_placas):
        self._potencia_placas = potencia_placas
        self.kwp = 0
        self.quantidade_placas = 0
        self.kwp_entregue = 0

    @property
    def potencia_placas(self):
        return self._potencia_placas

    def transforma_em_kwp(self):
        quilowatt_dia = self.kwh / 30.416666667
        self.kwp = (quilowatt_dia / self.indice_solar) / self.eficiencia_placas
        return self.kwp

    def qtd_placas(self):
        self.quantidade_placas = math.ceil((self.kwp / self.potencia_placas) * 1000)
        if self.quantidade_placas % 2 != 0:
            self.quantidade_placas += 1
        return self.quantidade_placas

    def kwp_final(self):
        self.kwp_entregue = (self.quantidade_placas * self.potencia_placas) / 1000
        return self.kwp_entregue

class Kwh(CalculoUsinaSolar):
    def __init__(self, kwh, potencia_placas, indice_solar, eficiencia_placas):
        super().__init__(potencia_placas)
        self._kwh = kwh
        self._indice_solar = indice_solar
        self._eficiencia_placas = eficiencia_placas

    @property
    def kwh(self):
        return self._kwh

    @property
    def indice_solar(self):
        return self._indice_solar

    @property
    def eficiencia_placas(self):
        return self._eficiencia_placas


class Kwp(CalculoUsinaSolar):
    def __init__(self, kwp, potencia_placas):
        super().__init__(potencia_placas)
        self._kwp = kwp

    @property
    def kwp(self):
        return self._kwp
