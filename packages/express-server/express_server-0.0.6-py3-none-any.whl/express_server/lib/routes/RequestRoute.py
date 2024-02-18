from urllib.parse import urlparse,parse_qs
from ..utils.paths import set_body,LinkedObj

class RequestRoute:
    def __init__(self,method,request):
        self.request = request
        self.path = (request.path.replace("%20"," ")).lower()
        self.protocol = request.protocol_version.split("/")[0]
        self.url = self.originalUrl = self.pathname = self.href = self._raw  = urlparse(self.path).path
        # < -- find host and port of server -- >
        (host, port) = self.request.server.server_address
        # < -- set example.com -- >
        self.hostname = host
        # < -- set example.com:port -- >
        self.host = f"http://{host}:{port}"
        self.server_full_url = f"http://{host}:{port}"+self.path
        self.method = method
        # < -- query like ?query=value -- >
        self.query = None
        self._find_query(self.server_full_url)
        # < -- set client ip and port -- >
        self.ip = request.client_address[0]
        self.client_port = request.client_address[1]
        
        self.headers = None
        self.rawHeaders = []
        self._write_row_header(request)

        # this is for /:kjsd like this url 
        self.params = LinkedObj({})
        
        # body
        self.body = {}
        # files
        self.files = {}
        # < -- set cookies -- >
        self._set_init_cookie()
        # < -- set body -- >
        self._set_init_body()
    def getCookie(self,key):
        try:
            for cookieKey, value in self.cookies:
                if(cookieKey == key):
                    return value
        except:
            pass
        return None
    
    def _write_row_header(self,request):
        try:
           headers = {key: value for (key,value) in request.headers.items()}
           # < -- making capitalize word like avi-ok --> AviOk -- >
           headers_modify = {}
           for header in headers:
                # Capitalize the first letter of each part (except the first part)
                modified_header = ''.join(word.capitalize() for word in header.split('-'))
                
                headers_modify[modified_header] = headers[header]
            
           self.headers = LinkedObj(headers_modify)
          
           for key, value in request.headers.items():
               self.rawHeaders.extend([key,value])
        except:
            pass

    def find_qeury(self,query):
        for sotredQuery in self.query:
            if(sotredQuery == query):
                return self.query[sotredQuery]
        return None
    
    def _set_init_cookie(self):
        row_cookies = self.request.headers.get("Cookie")
        
        # set cookies
        cookies_dist = {}
        try:
            if row_cookies:
                for cookie in  row_cookies.split('; '):
                    cookieArr = cookie.split("=")
                    if(len(cookieArr) == 2):
                        cookies_dist[cookieArr[0]] = cookieArr[1]
                    elif(len(cookieArr) == 1):
                        cookies_dist[""] = cookieArr[0]
        except:
            pass 
        # add a cookies object in cookies
        self.cookies = LinkedObj(cookies_dist)

    def _find_query(self,url):
        # < -- splice url -- >
        parsed_url = urlparse(url)

        # < -- find all query from request and add key value in dictionary ex:- {key,value} -- >
        query = {key: value[0] for key, value in parse_qs(parsed_url.query).items()}
        self.query = LinkedObj(query)
        
    def _set_parmas(self,paramsList):
         self.params = LinkedObj(paramsList)
    
    def _set_init_body(self):
        set_body(self)

    # if attribute not exist return None as value not any error
    def __getattr__(self, attr):
        return None