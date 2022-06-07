#Para testar importe 
from calculo_solar import Kwh, Kwp


kwh = Kwh(700, 440, 5.02, 0.95) #crie um objeto passando o "Valor Kwh desejado", "Potencia das Placas", "indice solarimetrico", 
                                #"eficiencia das placas" nesse untimo em % ou seja 0.95 = 95% 
kwh.transforma_em_kwp() #Metodo que transforma Kwh em Kwp
kwh.qtd_placas() #Chama o Metodo que calcula qtd de placas
kwh.kwp_final() #Chama o Metodo que apresenta quanto em Kwp será entregue 
#kwh.imprime_kwh() -> #Se quiser usar para teste primeiro copie e cole o metodo imprime abaixo para a classe pai.


kwp = Kwp(6.00, 440) #crie um objeto passando o "Valor em Kwp desejado float" e "Potencia das placas"
kwp.qtd_placas() #Chama o Metodo que calcula qtd de placas
kwp.kwp_final() #Chama o Metodo que apresenta quanto em Kwp será entregue
#kwp.imprime_kwp() -> #Se quiser usar para teste primeiro copie e cole o metodo imprime abaixo para a classe pai.




    """def imprime_kwh(self):
        print(f"Kwh é {self.kwh}")
        print(f'KWp é:{self.kwp}')
        print(f'Qtd é: {self.quantidade_placas} placas')
        print(f'KWp Final é: {self.kwp_entregue}\n')

    def imprime_kwp(self):
        print(f'KWp é: {self.kwp}')
        print(f'Qtd é: {self.quantidade_placas} placas')
        print(f'KWp Final é: {self.kwp_entregue}')"""
