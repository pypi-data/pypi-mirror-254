from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class Notems:
    def __init__(self,host="https://note.ms",proxy=""):
        self.host = host

        options = Options()
        options.add_argument("--headless")
        if proxy != "":
            parsed_uri = urlparse(proxy)
            proxy_adr = parsed_uri.hostname
            proxy_port = parsed_uri.port
            options.set_preference('network.proxy.type', 1)
            options.set_preference('network.proxy.socks', proxy_adr)
            options.set_preference('network.proxy.socks_port', proxy_port)
            options.set_preference('network.proxy.socks_remote_dns', True)
        self.driver = webdriver.Firefox(options=options)
    
    def get_note(self,page):
        url = self.host + "/" + page
        self.driver.get(url)
        doc = self.driver.page_source
        soup = BeautifulSoup(doc, "html.parser")
        try:
            note = soup.find_all("textarea", {"class": "content"})[0].text
            return note
        except IndexError:
            print("There are some problems with the server")
            print("Page source:\n" + doc)
            return ""
    
    def post_note(self,page,text):
        url = self.host + "/" + page
        if self.driver.current_url != url:
            self.driver.get(url)
        text = text.replace("`","\`")
        post_js = f'''$.ajax({{
                        type: "POST",
                        data: "&t=" + encodeURIComponent(`{text}`)
                    }});
        '''
        self.driver.execute_script(post_js)
    
    def close(self):
        self.driver.close()

