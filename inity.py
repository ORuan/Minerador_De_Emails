import os,re, io,requests, urllib
from bs4 import BeautifulSoup


def getUrl():
    return input('Url do site [com http ou https)]:')


def request():
    
        url = getUrl()
        #r = requests.get(url)
        html_page = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_page, features="html.parser")

        try :
            request_page = requests.get(url)
            response_text = soup.text
            encontrados = re.findall('\w+@\w*\.\w+', response_text)
            email_file = io.open('./emails.txt', 'w')
            email_file.write('-------'+ str(encontrados))
            email_file.close()
        except:
            print('nao encontramos email, mb')

        for link in soup.findAll('a'):
            
            founds = link.get('href')
            arrayFound = []
            arrayFound.append(founds)
          

            for founds in arrayFound:
                print('Encontramos os seguintes links', founds)
                
                try:
                    if "http" in founds:
                        
                        #print(founds.index())
                        arrayHttp=[]    
                        arrayHttp.append(founds)
                        
                        for http in arrayHttp:
                            new_request(http,url)    
                        
                    
                    elif "https" in founds:
                        print('entrei no elif')
                        
                        arrayHttps=[]    
                        arrayHttps.append(founds)
                        for https in arrayHttps:
                            new_request(https,url)    
               
                except:
                    print('Problema interno')
            
        
def new_request(link,url_old):
    try:

        
            request_page = requests.get(url)
            response_text = soup.text
            encontrados = re.findall('\w+@\w*\.\w+', response_text)
            email_file = io.open('./emails.txt', 'a')
            email_file.write('-------'+ str(encontrados))
            email_file.close()


    except:
        
        complet_link = url_old + link
                
        request_page = requests.get(complet_link)
        response_text = soup.text
        encontrados = re.findall('\w+@\w*\.\w+', response_text)
        email_file = io.open('./emails.txt', 'a')
        email_file.write('-------'+ str(encontrados))
        email_file.close()
            


    else:
        print('nao conseguimos nos conectar, srry')

request()
