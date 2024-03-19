import requests
import json

iToken = "4c1bc488751e8305c560d1f5b322357a"
iTipoConsulta = 1

#http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=São Paulo&state=SP&token=your-app-token

if iTipoConsulta == 1:
    iCity = input("Nome da cidade")
    iUrl = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=" + str(iCity) + "&token=" + str(iToken)
    iResponse = requests.request("GET", iUrl)
    iRetorno = json.loads(iResponse.text)
    for iChave in iRetorno:
        iId = iChave['id']
        iName = iChave['name']
        iCountry = iChave['country']
        iState = iChave['state']
        print("id: " + str(iId) + " name: " + str(iName) + " country: " + str(iCountry) + " state: " + str(iState))

        iUrl2 = "http://apiadvisor.climatempo.com.br/api-manager/user-token/" + str(iToken) + "/locales"
        payload = "localeId[]=" + str(iId)
        headers = {'Content-Type' : 'application/x-www-form-urlencoded'}
        iResponse = requests.request("PUT", iUrl2, headers= headers, data=payload)
        iTipoConsulta=2

if iTipoConsulta == 2:
    iUrl = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/" + str(iId) + "/current?token=" + str(iToken)
    iResponse = requests.request("GET", iUrl)
    iRetorno = json.loads(iResponse.text)
    print(iRetorno)
    iTipoConsulta=3

if iTipoConsulta == 3:
    iUrl = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/" + str(iId) + "/hours/72?token=" + str(iToken)
    iResponse = requests.request("GET", iUrl)
    iRetorno = json.loads(iResponse.text)
    print(iRetorno)