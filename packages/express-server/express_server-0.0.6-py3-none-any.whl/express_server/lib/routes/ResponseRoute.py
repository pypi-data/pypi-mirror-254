import json
from ..utils.paths import find_content_type,GetCookieOptions

class DownloadFile:
    def __init__(self,path,filename,error_handler) -> None:
        self.path = path
        self.filename = filename
        self.throw_error = error_handler

class Status:
    def __init__(self,ResRoute) -> None:
        self.ResRoute = ResRoute

    def send(self,*arg):
        return self.ResRoute.send(*arg)
    
    def json(self,*arg):
        return self.ResRoute.json(*arg)
    
    def sendfile(self,*arg):
        return self.ResRoute.sendfile(*arg)

class ResponseRoute:
    def __init__(self):
        self.text = ''
        self.sendfilepath = None
        self.download_obj = None
        self.headers = []
        self.statusCode = 200

    def setHeader(self,key,value):
        self.headers.append((key,value))
    
    def setCookie(self,key,value,options={"expires":False,"path": False,"secure": False,"httpOnly": False,"sameSite": False,"domain": False}):
        
        # getting options 
        optionsStr = GetCookieOptions(options)
        cookie_value = f"{key}={value};{optionsStr}"
        # set cookies in header
        self.setHeader("Set-Cookie",cookie_value)

    def clearCookie(self,key,options={"path":"/"}):
        path = options["path"]
        cookie_value = f"{key}=None;Path={path};Expires=Sun, 05 Feb 2006 02:15:00 GMT"
        self.setHeader("Set-Cookie",cookie_value)
        
    def send(self,text = ""):
        self.text = str(text)
        return "end"
    
    def json(self,json_data = {}):
        self.setHeader("Content-Type","application/json")
        data_json = json.dumps(json_data, indent=2)
        self.text = data_json
        return "end"
    
    def sendfile(self,filename):
        self.sendfilepath = str(filename)
        return self.send()
    
    def location(self,redirect_location):
        self.setHeader("location",redirect_location)
        return self.send(f"<script>window.location.href = '{redirect_location}'</script>")
    
    def redirect(self,status_code,redirect_location):
        self.statusCode = status_code
        return self.location(redirect_location)
    
    def next(self):
        return "next"
    
    def status(self,status_code=200):
        self.statusCode = status_code
        return Status(self)
    
    def download(self,path,filename=None,error_handler=lambda err:None):
        self.download_obj = DownloadFile(path,filename,error_handler)
        return "end"
    
    # send content type like res.type("json")
    def type(self,ContentType):
        ContentType = find_content_type(ContentType,"extention")[0]
        if(ContentType):
            self.setHeader("Content-Type",ContentType)
    
    # if attribute not exist
    def __getattr__(self, attr):
        return None