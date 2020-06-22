import os,re, io,requests, urllib
from bs4 import BeautifulSoup


def getUrl():
    return input('Url do site [com http ou https)]:')

#https://api.github.com/users/ORuan
def request():
    
        url = getUrl()
        #r = requests.get(url)
        html_page = urllib.request.urlopen(url)


        soup = BeautifulSoup(html_page, features="html.parser")
        strsoup = str(soup)
        achados = re.findall('.........@......................', strsoup)
        email_file = io.open('./emails.txt', 'w')
        email_file.write(' '+ str(achados))
        email_file.close()


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

        new_html_page = urllib.request.urlopen(link)
        newsoup = BeautifulSoup(new_html_page, features="html.parser")
        strnewsoup = str(newsoup)
        achados = re.findall('.........@......................', strnewsoup)
        for ac in achados:
            email_file = io.open('./emails.txt', 'a')
            email_file.write(' '+ str(ac))
            email_file.close()

    except:
        
        complet_link = url_old + link
        new_html_page = urllib.request.urlopen(link)
        newsoup_ = BeautifulSoup(new_html_page, features="html.parser")
        strnewsoup_ = str(newsoup_)
        achados_ = re.findall('.........@......................', strnewsoup_)
        for ac_ in achados_:
            email_file = io.open('./emails.txt', 'a')
            email_file.write(' '+ str(ac_))
            email_file.close()
            


    else:
        print('nao conseguimos nos conectar, srry')


#def request_inside(link):


request()
