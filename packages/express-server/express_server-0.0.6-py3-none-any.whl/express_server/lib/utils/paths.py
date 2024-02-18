from datetime import datetime, timezone
import os
import json
from ..constants import file_types
from .file_oprations import Create_Folder
import random
import string
import time
from ..constants import temp_file_path

# < -- user query like js object -- >
class LinkedObj():
    def __init__(self, arr) -> None:
        self.__list__ = arr
        for key in arr:
            # < -- set as self -- >
            setattr(self, key, arr[key])
        
    # if key not not find 
    def __getattr__(self, attr):
        return None


# < -- check valid json or not  -- >
def is_valid_json(json_str):
    try:
        json.loads(json_str)
        return True
    except json.JSONDecodeError:
        return False

# < -- generate random string between {0-9 a-z} -- >
def generate_random_string(length):
    characters = string.ascii_letters + string.digits  # includes letters (both cases) and digits
    return ''.join(random.choice(characters) for _ in range(length))


# < -- make path simple example: 1: c://programming 2: ./index.php output:-c://programming/index.php -- >
def path_normalizer(filepath):
     if (not os.path.splitdrive(filepath)[0]):
            base_path = os.getcwd()
            return os.path.normpath(os.path.join(base_path,filepath))


# < -- it's reutrn content type of paths that available in file types -- >
def get_content_info_by_extension(extension):
    for FileCategory in file_types:
        for ext in file_types[FileCategory]:
                if ext == extension:
                    return ((file_types[FileCategory][ext],FileCategory))
    return (None,None)

# < -- Find Content Type From File Path -- >
def find_content_type(path,path_info):
    extension = path
    if path_info == "filename":
            extension = os.path.splitext(path)[1]
      
    elif path_info == "extention":
         if not str(extension).startswith("."): extension = "."+extension
    try:
        return get_content_info_by_extension(extension)
    except:
        return (None,None)

# handle cookie options
def keyExist(list,key):
    try:
        return list[key]
    except:
        return False



def CalcuateGMT(sec):
    # Get the current time in GMT
    current_time_gmt = datetime.utcfromtimestamp(sec).replace(tzinfo=timezone.utc)

    # Format the datetime object as a string
    formatted_time = current_time_gmt.strftime("%a, %d %b %Y %H:%M:%S GMT")
    return formatted_time

def GetCookieOptions(options):
    optionsStr = ""
    preOptions={
        "path": keyExist(options,"path"),
        "domain": keyExist(options,"domain"),
        "expires": keyExist(options,"expires"),
        "secure": keyExist(options,"secure"),
        "httpOnly": keyExist(options,"httpOnly"),
        "sameSite": keyExist(options,"sameSite")
    }    
    
    # calcuate expires
    if type(preOptions["expires"]) == int or type(preOptions["expires"]) == float:
        gmt_time = CalcuateGMT(preOptions["expires"])
        optionsStr += f'Expires={gmt_time};'
        
    # check domain
    if preOptions["domain"]:
        optionsStr += f'Domain={preOptions["domain"]};'
    
    # check path
    if preOptions["path"]:
        optionsStr += f'Path={preOptions["path"]};'
    
    #check same site
    sameSite = preOptions["sameSite"]
    if type(sameSite) == str and (sameSite in  "Lax" or sameSite in "Strict" or sameSite in "None"):
        optionsStr += f"SameSite={sameSite};"
        
    # check secure bool value
    if preOptions["secure"]:
        optionsStr += f"Secure;"
        
    # check httpOnly bool value
    if preOptions["httpOnly"]:
        optionsStr += f"HttpOnly;"
 
    return optionsStr

# < -- URL Macing Functions -- >
# convert /about/asdfasdfs////////////dasfsd/asdfasdf/dfasdfasdf/// --> /about/asdfasdfs/dasfsd/asdfasdf/dfasdfasdf
def normalize_path(path):
    normalizePath = path
    try:
        while True:
            if normalizePath.find("//") > 0:
                normalizePath = normalizePath.replace("//", "/")
            else:
                if len(normalizePath) > 1 and normalizePath[-1] == "/":
                    normalizePath = normalizePath[:len(normalizePath) - 1]
                break
    except:
        normalizePath = path
        pass
    return normalizePath

# < -- split path into / -- >
def split_url(url):
    url = url.split("/")
    return url

# < -- match paths like /name /name or /name/home or /name/home -- >
def matchBasePath(req,route):
    for i,p in enumerate(route):
        if(len(req)>i and p == req[i]):
            pass
        else:
            if(p[0] ==  ":" or p[0] ==  "*"):
                return {"index": i,"pattern": p[0]}
            break
    return {"index": None,"pattern": None}


# < -- find params -- >
def findParmas(req,route):
    # all params appended here 
    Match_parmas = {}
    
    # match paths like about/name == about/name 
    basePath = matchBasePath(req,route)
    
    # if path not exist return False
    if basePath["index"] == None:
        return False

    # find only slugs 
    routeIndex = basePath["index"]
    nextReq = req[routeIndex:]
    nextRoute = route[routeIndex:]
    # length of slugs 
    nextReq_len = len(nextReq)
    nextRoute_len = len(nextRoute)
    
    # this is for *
    forward = 0
    if nextRoute_len <= nextReq_len:
        for i in range(0,nextRoute_len):          
            req_param = nextReq[i+forward]
            route_pattern = nextRoute[i]

            if route_pattern.startswith(":"):
                params_key = route_pattern[1:]
                Match_parmas[params_key] = req_param
                
                
            elif route_pattern == "*":
                if (len(nextReq[i:])) >= (len(nextRoute[i:])):
                    forward += len(nextReq[i:])-len(nextRoute[i:])                
            else:
                if req_param != route_pattern:
                    Match_parmas = {}
                    return False

                    
            if(i==nextRoute_len-1):
                if (len(nextReq[i+forward:]) != len(nextRoute[i:]) and not route_pattern.startswith("*")):
                        Match_parmas = {}
                        return False
    else:
        Match_parmas = {}
        return False
    
    return Match_parmas

# < -- check valid file name or not -- >
def is_valid_file_name(file_name):
    try:
        # Check if the file name is valid without attempting to create a file
        with open(file_name, 'a'):
            pass
        os.remove(file_name)  # Remove the file if it was created successfully
        return True
    except OSError:
        return False

# < -- FIND BODY FROM CONTENET -- >
def set_body(requestRoute):
    # < -- getting content type,length from header -- >
    ContentType = requestRoute.headers.ContentType
    ContentLength = None
    try: ContentLength = int(requestRoute.headers.ContentLength)
    except: pass

    # < --  set json data in body  -- >
    try:

        if ContentType and ContentType.lower() == "application/json":
            # < --  getting body data in binary  -- >
            if ContentLength and ContentLength>0:
                rawBody = requestRoute.request.rfile.read(ContentLength)
            
            # decode json 
            jsonStr = rawBody.decode("utf-8")
            
            if is_valid_json(str(jsonStr)):
                requestRoute.body = json.loads(jsonStr)
            return
    except:
        # < -- invlaud json -- >
        pass
    
    fileds = {}
    files = {}
    try:
        # < -- handle form data  -- >
        ContentType_Form = ContentType.split("; ")
        if ContentType and ContentType_Form[0] == "multipart/form-data" and len(ContentType_Form)>1:
           boundaryID = ContentType_Form[1].split("boundary=----")[1]
           
           while boundaryID:
                line = requestRoute.request.rfile.readline()
                try:
                    rawBody = line.decode("utf-8")
                    
                    if(len(rawBody) > 0 and rawBody != "\r\n"):
                        try:
                            singleHeader = rawBody.split("; ")
                            
                            # find only filed name 
                            if len(singleHeader) == 2:
                                ContentDisposition = singleHeader[0].split("Content-Disposition: ")[1]
                                htmlName = singleHeader[1].split("name=")[1].replace("\r\n","")[1:-1]
                                if(ContentDisposition == "form-data" and htmlName):
                                    line = requestRoute.request.rfile.readlines(2)
                                    value = (line[1].decode("utf-8")[:-2])
                                    # setting final vlaue 
                                    fileds[htmlName] = value

                            # find filename
                            if len(singleHeader) == 3:
                                # getting headers 
                                ContentDisposition = singleHeader[0].split("Content-Disposition: ")[1]
                                htmlName = singleHeader[1].split("name=")[1][1:-1]
                                fileName = singleHeader[2].split("filename=")[1].replace("\r\n","")[1:-1]
                                fileName = fileName.lower()
                                
                                # getting file content type
                                line = requestRoute.request.rfile.readlines(1)
                                FileCType = line[0].decode("utf-8").split("Content-Type:")[1][1:-2]

                                # check for file 
                                if(ContentDisposition == "form-data" and len(htmlName)>0 and len(fileName) and len(FileCType)>0):
                                    # < -- getting current time for folder  -- >
                                    current_time = int(time.time())
                                    
                                    # < -- temp path of current os -- >
                                    tempPCPath = f"{temp_file_path}\\{current_time}\\"
                                    # tempPCPath = f"{os.getcwd()}\\py_express_temp\\{current_time}\\"

                                    # < -- creating folder in temp path -- >
                                    tempPath = Create_Folder(tempPCPath)
                                    
                                    if tempPath==False or is_valid_file_name(fileName) == False:
                                        break
                                    
                                    # < -- full file path -- >
                                    filePath = f"{tempPath}\\{fileName}"
                                                                        
                                    # < -- getting extention -- >
                                    fileStr,extension  = os.path.splitext(filePath)
                                    
                                    # < -- Generate a random string of length 10 -- >
                                    random_file_name = generate_random_string(10)

                                    # < -- full path with random file name like avi.txt --> avi-kdj334.txt -- >
                                    filePath = f"{fileStr}-{random_file_name}{extension}"

                                    # save file 
                                    try:
                                        with open(filePath,"wb") as writeFile:
                                            line = requestRoute.request.rfile.readline()
                                            isFileChunk = True
                                            while isFileChunk:
                                                try:
                                                    line = requestRoute.request.rfile.readline()
                                                    rawBody = line.decode("utf-8")
                                                    # exit reading form 
                                                    if (rawBody.startswith(f"------{boundaryID}--")) or (rawBody.startswith(f"------{boundaryID}")):
                                                        isFileChunk = False
                                                        # < -- close file -- >
                                                        writeFile.close()
                                                    else:
                                                        raise Exception("Error")

                                                except Exception as error:
                                                    writeFile.write(line)
                                        
                                            # < -- close file -- >
                                            writeFile.close()
                                    except Exception as error:
                                        # print(error)
                                        # if any error delete file 
                                        os.unlink(filePath)
                                    # check file exist or not 
                                    if(os.path.exists(filePath)):
                                        fileSize = os.path.getsize(filePath)

                                        # setting file info in file dict
                                        fileInfo = {"name": fileName,"Content-Type": FileCType,"temp": filePath,"fileSize": fileSize,"extension": extension}
                                        try: files[htmlName]
                                        except: files[htmlName] = []
                                        files[htmlName].append(fileInfo)

                        except Exception as error:
                            pass
                    # exit reading form 
                    if (rawBody.startswith(f"------{boundaryID}--")):
                        break
                     
                except Exception as error:
                    break
        
        # setting body and files in main object 
        requestRoute.body = fileds
        requestRoute.files = files
    
    except:
        pass