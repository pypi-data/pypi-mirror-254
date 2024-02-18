import os
from ..utils.paths import path_normalizer,find_content_type
from .file_oprations import write_file_chunks,write_video_stream

class Attributes:
    # < -- set header from list -- >
    def setHeader(self,request,headers=[],end=False):
        isContentTypeAvailable = False
        
        # < -- add header one by one -- >
        for (key,value) in headers:
            request.send_header(key, value)
            if(key.lower() == "content-type"): isContentTypeAvailable = True
        
        # < -- if content type not given -- >
        if(not isContentTypeAvailable): request.send_header('Content-Type', 'text/html')

        # < -- end header -- >
        if(end): request.end_headers()
    
    # < -- end the headers -- >
    def endHeader(self,request):
        request.end_headers()
           
    # < -- Send Simple Text -- >
    def addText(self,text,request):
        request.wfile.write(text.encode("utf-8"))

    def getHeader(self,name,request):
        return request.headers.get(name,None)
         
    # < -- send a file with with chunks -- >
    def sendfile(self,route,request,method,chunk_size = 1024):
        try:
            # < -- get send file path using route  -- >
            filepath = route.sendfilepath
            
            # check full path given or not if not so add cwd + path
            file_full_path = path_normalizer(filepath)
            
            # check path exist and path is correct
            if(not os.path.exists(file_full_path)):
                request.send_response(404)
                self.endHeader(request)
                request.wfile.write(f"{method} {file_full_path} Not Exists.".encode("utf-8"))
                return None
                
            # < -- file size -- >
            file_size = os.stat(filepath).st_size
            
            # < -- find file content type -- >
            (content_type,FileCategory) = find_content_type(file_full_path,"filename")
            
            # < -- if found video then write video staream -- > <-- handle chunk video file letter 
            if(FileCategory == "video"):
                chunk_size_mb = 5
                write_video_stream(file_full_path,content_type,chunk_size_mb,file_size,request)
                return None

            # < -- set status code  -- >
            request.send_response(route.statusCode)
            # < -- if content_type found then add in header -- > 
            if(content_type):route.setHeader("Content-Type",content_type)
            # < -- set content length headers -- >
            route.setHeader("Content-Length",file_size)
            # < -- set headers -- >
            self.setHeader(request,route.headers)
            # < -- end headers -- >
            self.endHeader(request)

            # write file in bytes 
            write_file_chunks(file_full_path,request,chunk_size)
        except Exception as error:
                # print(error)
                request.wfile.write(f"{error}".encode("utf-8"))
    
    def download_file(self,route,request,method,chunk_size = 1024):
        try:
            # < -- get send file path using route  -- >
            filepath = route.download_obj.path
            
            # check full path given or not if not so add cwd + path
            file_full_path = path_normalizer(filepath)
            
            # check path exist and path is correct
            if(not os.path.exists(file_full_path)):
                request.send_response(404)
                self.endHeader(request)
                route.download_obj.throw_error(f"{method} {file_full_path} File Not Exists.")
                return None
                
            # < -- file size -- >
            file_size = os.stat(filepath).st_size
            
            # < -- find file content type -- >
            (content_type,FileCategory) = find_content_type(file_full_path,"filename")
            
            # < -- set status code  -- >
            request.send_response(route.statusCode)

            # < -- downlaod file file name -- >
            file_name = os.path.basename(file_full_path)
            if route.download_obj.filename:
                 file_name = route.download_obj.filename

            # < -- set headers -- > 
            if(content_type):route.setHeader("Content-Type",content_type)
            route.setHeader("Content-Length",file_size)
            route.setHeader('Content-Disposition', f"attachment; filename={file_name}")
            route.setHeader('Accept-Ranges', 'bytes')
            self.setHeader(request,route.headers,True)

            # write file in bytes 
            write_file_chunks(file_full_path,request,chunk_size)
            route.download_obj.throw_error(None)
        except Exception as error:
                route.download_obj.throw_error(error)