# UsinaFotovoltaica
Calcula qtd de placas e kwp entregue ao cliente em projeto. Calcula tanto pelo valor do Kwh medio ou desejado como direto pelo Kwp.
Baixe a teste.py para testar direto no pycharm, vcode e etc.

Para utilizar import as classes filhas (kwh e kwp) para seu programa 

Para calcular por Kwh:

kwh = Kwh(700, 440, 5.02, 0.95) #valor_kwp, potencia das placas, indice solar da região, eficiencia das placas em % ou seja 0,95 = 95% 
kwh.tranforma_em_kwp() #Chame o Metodo que transforma Kwh em Kwp 
kwh.qtd_placas() #Chame o Metodo que calcula qtd de placas 
kwh.kwp_final() #Se desejar saber chame o Metodo que apresenta quanto em Kwp será entregue 


Para calcular por Kwp:

kwp = Kwp(6.00, 440) #valor kwp, potencia das placas 
kwp.qtd_placas() #Chame o Metodo que calcula qtd de placas 
kwp.kwp_final() #Se desejar saber chame o Metodo que apresenta quanto em Kwp será entregue  


