import whois

dominio = input("Digite o domínio:")
consulta_whois = whois.whois(dominio)

#print consulta whois
print(consulta_whois.text)