#  ___      _ _                _
# |   \ ___| | |_ __ _ ____  _| |
# | |) / -_) |  _/ _` (_-< || | |
# |___/\___|_|\__\__,_/__/\_,_|_|
#
# Printers Info Scraping v1
# Script para realizar scraping no painel web das impressoras instaladas nas lojas, e filtrar informações relevantes sobre a mesma.
# Cheque o repositório oficial -> https://gitlab.deltasul.com.br/NicolasdaSilvaAraujo/printers-info-scraping/


import requests
from bs4 import BeautifulSoup
import csv
import socket

csvfile = open('printersInfo.csv', 'w', newline='')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(["IP", "MODELO DA IMPRESSORA", "No DE SERIE", "TOTAL IMPRESSOES", "ERROS IMPRESSORA"])

diffLines = [
    '192.168.6.36',
    '192.168.40.36',
    '192.168.50.46',
    '192.168.76.46',
    '192.168.80.46',
    '192.168.115.36',
    '192.168.115.46',
    '192.168.126.36',
    '192.168.126.46',
    '192.168.131.46',
    '192.168.138.46',
    '192.168.143.36',
    '192.168.143.46',
    ]

diffLinesNd = [
    '192.168.42.46',
    '192.168.131.36',
    ]

with open('printers.txt', 'r') as f:
    for line in f:
        line = line.strip()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = 80
        
        try:
            print(line)
            s.settimeout(3)
            s.connect((line, port))
            s.settimeout(None)

            URL = "http://" + line.strip() + "/"
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")
            grepModel = soup.find('td', class_='mastheadTitle').text

            if line in diffLines:
                URL = "http://" + line + "/info_configuration.html?tab=Home&menu=DevConfig"
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, "html.parser")

                printerModel = soup.find('td', class_='itemFont').text
                printerSerial = soup.findAll('td', class_='itemFont')[2].text
                printerIp = soup.findAll('td', class_='itemFont')[19].text.strip()
                printerTotalPages = soup.findAll('td', class_='itemFont')[29].text
                printerErrors = soup.findAll('td', class_='itemFont')[32].text

                print("Modelo: " + printerModel)
                print("Número de Série: " + printerSerial)
                print("IP: " + printerIp)
                print("Páginas impressas: " + printerTotalPages)
                print("Obstruções: " + printerErrors)

                csvwriter.writerow([printerIp, printerModel, printerSerial, printerTotalPages, printerErrors])

            elif line in diffLinesNd:
                URL = "http://" + line + "/hp/device/info_configuration.htm"
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, "html.parser")

                printerModel = soup.find('td', class_='itemFont').text
                printerSerial = soup.findAll('td', class_='itemFont')[2].text
                printerIp = soup.findAll('td', class_='itemFont')[13].text.strip()
                printerTotalPages = soup.findAll('td', class_='itemFont')[16].text
                printerErrors = soup.findAll('td', class_='itemFont')[18].text

                print("Modelo: " + printerModel)
                print("Número de Série: " + printerSerial)
                print("IP: " + printerIp)
                print("Páginas impressas: " + printerTotalPages)
                print("Obstruções: " + printerErrors)

                csvwriter.writerow([printerIp, printerModel, printerSerial, printerTotalPages, printerErrors])

            elif grepModel == 'HP LaserJet P2055dn':
                URL = "http://" + line + "/hp/device/info_configuration.htm"
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, "html.parser")

                printerModel = soup.find('td', class_='itemFont').text
                printerSerial = soup.findAll('td', class_='itemFont')[2].text
                printerIp = soup.findAll('td', class_='itemFont')[13].text.strip()
                printerTotalPages = soup.findAll('td', class_='itemFont')[16].text
                printerErrors = soup.findAll('td', class_='itemFont')[19].text

                print("Modelo: " + printerModel)
                print("Número de Série: " + printerSerial)
                print("IP: " + printerIp)
                print("Páginas impressas: " + printerTotalPages)
                print("Obstruções: " + printerErrors)

                csvwriter.writerow([printerIp, printerModel, printerSerial, printerTotalPages, printerErrors])

            elif grepModel == 'HP LaserJet M402dne':
                URL = "http://" + line + "/info_configuration.html?tab=Home&menu=DevConfig"
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, "html.parser")

                printerModel = soup.find('td', class_='itemFont').text
                printerSerial = soup.findAll('td', class_='itemFont')[2].text
                printerIp = soup.findAll('td', class_='itemFont')[23].text.strip()
                printerTotalPages = soup.findAll('td', class_='itemFont')[28].text
                printerErrors = soup.findAll('td', class_='itemFont')[31].text

                print("Modelo: " + printerModel)
                print("Número de Série: " + printerSerial)
                print("IP: " + printerIp)
                print("Páginas impressas: " + printerTotalPages)
                print("Obstruções: " + printerErrors)

                csvwriter.writerow([printerIp, printerModel, printerSerial, printerTotalPages, printerErrors])

            elif grepModel == 'HP LaserJet P2035n':
                URL = "http://" + line + "/SSI/info_configuration.htm"
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, "html.parser")

                printerSerial = soup.findAll('td', class_='itemFont')[1].text
                printerIp = soup.findAll('td', class_='itemFont')[9].text.strip()
                printerTotalPages = soup.findAll('td', class_='itemFont')[11].text
                printerErrors = soup.findAll('td', class_='itemFont')[12].text

                print("Modelo: " + grepModel)
                print("Número de Série: " + printerSerial)
                print("IP: " + printerIp)
                print("Páginas impressas: " + printerTotalPages)
                print("Obstruções: " + printerErrors)

                csvwriter.writerow([printerIp, grepModel, printerSerial, printerTotalPages, printerErrors])

            elif grepModel == 'HP LaserJet 400 M401n':
                URL = "http://" + line + "/info_configuration.html?tab=Home&menu=DevConfig"
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, "html.parser")

                printerModel = soup.find('td', class_='itemFont').text
                printerSerial = soup.findAll('td', class_='itemFont')[2].text
                printerIp = soup.findAll('td', class_='itemFont')[23].text.strip()
                printerTotalPages = soup.findAll('td', class_='itemFont')[33].text
                printerErrors = soup.findAll('td', class_='itemFont')[36].text

                print("Modelo: " + grepModel)
                print("Número de Série: " + printerSerial)
                print("IP: " + printerIp)
                print("Páginas impressas: " + printerTotalPages)
                print("Obstruções: " + printerErrors)

                csvwriter.writerow([printerIp, printerModel, printerSerial, printerTotalPages, printerErrors])

            elif grepModel == 'HP LaserJet 400 M401dne':
                URL = "http://" + line + "/info_configuration.html?tab=Home&menu=DevConfig"
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, "html.parser")

                printerModel = soup.find('td', class_='itemFont').text
                printerSerial = soup.findAll('td', class_='itemFont')[2].text
                printerIp = soup.findAll('td', class_='itemFont')[20].text.strip()
                printerTotalPages = soup.findAll('td', class_='itemFont')[30].text
                printerErrors = soup.findAll('td', class_='itemFont')[33].text

                print("Modelo: " + printerModel)
                print("Número de Série: " + printerSerial)
                print("IP: " + printerIp)
                print("Páginas impressas: " + printerTotalPages)
                print("Obstruções: " + printerErrors)

                csvwriter.writerow([printerIp, printerModel, printerSerial, printerTotalPages, printerErrors])
            else:
                print("NENHUM DOS MODELOS ACIMA")
                csvwriter.writerow([line, grepModel])
        except socket.error:
            print(f"O host {line} está offline.")
            csvwriter.writerow([line, "IMPRESSORA OFFLINE"])
