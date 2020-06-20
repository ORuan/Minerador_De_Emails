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
        email_file = io.open('./emails.txt', 'a')
        email_file.write(' '+ str(achados))
        email_file.close()
        """for main_achado in soup.findAll('.@.'):
            print('mail_achado')"""
    

        for link in soup.findAll('a'):
            founds = link.get('href')
            #print ('1_encontrado',founds)
            if "https" in founds:
                print('é seguro')
                try:
                    other_pages_sec = urllib.request.urlopen(founds)
                    print(other_pages_sec)
                except :
                    print('nada foi achado ;-;')

            if "http" in founds:
                print('não é seguro, mas é externo')
                try :
                    other_pages= urllib.request.urlopen(founds)
                    print(other_pages)
                except:
                    print('Não achamos nada ;-;')



            """if 'https' or 'http' in founds:
                print('------Links externos------')
                print(other_pages)
            else:
                links_inside_sec = ('https'+other_pages)
                links_inside = ('http'+other_pages)

                print(links_inside)
                try :
                    other_urls = urllib.request.urlopen(links_inside)
                    print(other_urls)
                except:
                    other_urls_sec = urllib.request.urlopen(links_inside_sec)
                    print(other_urls_sec)"""


request()
