#web scraping
import requests
from bs4 import BeautifulSoup

requisicao= requests.get("https://www.bbc.com/portuguese/geral-56687257.amp/")
resposta_rqc=requisicao.status_code
if resposta_rqc==200:
	print("Requisicao aceita!",requisicao.status_code)
else:
	print("falha!",resposta_rqc)

dados_html= requisicao.content

site_html=BeautifulSoup(dados_html, "html.parser")
site_fmt=site_html.prettify()


a= site_html.find_all("li", attrs={"class": "bbc-acwcvw e1drcs2w0"})
contador=0
for lista in a:
	#print(lista)
	
	for lista_filtro in lista:
		print(lista_filtro.next_element)
		
#bbc-acwcvw e1drcs2w0
#"bbc-1fobf8d e1gggypo0"


