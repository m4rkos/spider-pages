from bs4 import BeautifulSoup
import requests
import datetime
import os
import urllib
import json
from tqdm import tqdm

class Scrap:
    
    def __init__(self):
        print("Hello")
    
    def __main__(self):
        url = "https://www.fotball.no/fotballdata/klubb/hjem/?fiksId="
        print(url)
                
        path0 = "_Data"
        
        try:
            os.makedirs(path0)
        except OSError:
            pass

        for a in range(15):
        
            check = requests.get(url + str(a + 1))
            url_ok = url + str(a + 1)

            if check.status_code == 200:
                print(check)
                print(a + 1)

                soup = BeautifulSoup(check.text, 'lxml')

                try:                      
                    img = soup.find('div', class_="fiks-header").img["src"]
                    
                    
                    img_link = "https://www.fotball.no"+img.rsplit('/', 1)[0]
                    print(img_link)

                    title = soup.find('a', class_="hero-heading").text
                    
                    #if requests.get(img_link).status_code == 200:    
                    self.upload_img(self.repl_simbols(title), path0 + "/images", img_link)
                    #print(self.repl_simbols(title))                        
                        
                    pass
                    
                except:
                    print("No brand available !")
                    pass

                """Klubb = soup.find('')
                Log = soup.find('')"""
                Krets = soup.find('div', class_="grid__item one-third mobile--one-whole no-margin--p").findChildren()[16].text
                print(Krets)
                """Navn = soup.find('')
                Epost = soup.find('')
                Rolle = soup.find('')
                Telefon = soup.find('')
                fax = soup.find('')
                
                self.save_log(path0, url_ok, Klubb, Log, Krets, Navn, Epost, Rolle, Telefon, fax)
                """
                pass
            else:
                print("Not found")
                pass
            pass

    @staticmethod
    def upload_img(url, path0, check):
        img = check.rsplit('/', 1)[1]
        
        
        path1 = path0 + '/' + url
        try:
            os.makedirs(path1)
        except OSError:
            pass

        img_t = requests.get(check, stream=True)

        if os.path.exists(path1 + "/" + img):
            print('> There is !')
            pass
        else:
            with open(path1 + "/" + img, "wb") as handle:
                for data in tqdm(img_t.iter_content()):
                    handle.write(data)
            
            pass
    
    """@staticmethod
    def save_log(path0, search_for, Klubb, Log, Krets, Navn, Epost, Rolle, Telefon, fax ):
        timex = datetime.datetime.now()
        tmf = str("tm_" + timex.strftime("%d-%m-%Y"))
        #path2 = "_test/log_" + tmf + ".csv"

        for_ = search_for.replace(",", "_")
        for_ = for_.replace("https://www.", "")

        path = path0 +  "/" + for_.rsplit('.', 1)[0] + "_" + tmf + ".csv"

        header = 'TimeStamp, Search for, \
            Klubb, Log, Krets, Navn, E-post, Rolle, Telefon, fax;\n'
        data = 'Time: ' + str(timex.strftime("%I:%M:%S %p")) + ' , ' + for_ + ' , \
            ' + Klubb + ', ' + Log + ', ' + Krets + ', ' + Navn + ', ' + Epost + ', ' + Rolle + ', ' + Telefon + ', ' + fax + ';\n'

        if os.path.exists(path):
            try:
                file = open(path, "ab")
                file.write(data.encode())
                file.close()
            except IOError:
                file = open(path, "wb")
                file.write(data.encode())
                file.close()

            pass

        else:
            try:
                file = open(path, "ab")
                file.write(header.encode())
                file.write(data.encode())
                file.close()
            except IOError:
                file = open(path, "wb")
                file.write(header)
                file.write(data)
                file.close()

            pass"""

    def repl_simbols(self, repl):
                    
        n = repl.replace('Ç', 'C')
        n = n.replace('ç', 'c')
        n = n.replace('ã', 'a')
        n = n.replace('Ã', 'A')
        n = n.replace('õ', 'o')
        n = n.replace('Õ', 'O')
        n = n.replace('é', 'e')
        n = n.replace('É', 'E')
        n = n.replace('è', 'e')
        n = n.replace('È', 'E')
        n = n.replace('á', 'a')
        n = n.replace('Á', 'A')
        n = n.replace('à', 'a')
        n = n.replace('À', 'A')
        n = n.replace('â', 'a')
        n = n.replace('Â', 'A')
        n = n.replace('ô', 'o')
        n = n.replace('Ô', 'O')
        n = n.replace('ê', 'e')
        n = n.replace('Ê', 'E')
        n = n.replace('ü', 'u')
        n = n.replace('Ü', 'U')
        
        n = n.replace('å', 'a')
        n = n.replace('ä', 'a')
        n = n.replace('ö', 'o')
        n = n.replace('Å', 'A')
        n = n.replace('Ä', 'A')
        n = n.replace('Ö', 'O')
        
        n = " ".join(n.split())
        n = n.replace(' ', '-')

        res = str(n.lower())
        return res

if __name__ == "__main__":
    s = Scrap()
    s.__main__()
    pass

