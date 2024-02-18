import os
import shutil
import time
from datetime import datetime 
from ..constants import temp_file_path,temp_file_remove_sec

# < -- send file in chunks -- > 
def write_file_chunks(path,request,chunk_size=1024):
    with open(path,"rb") as file:
        try:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                request.wfile.write(chunk)
            file.close()
        except Exception as error:
            #  print("Uer Disconnected!")
            pass
    
    return True

# < -- write video file stream -- >
def write_video_stream(VIDEO_PATH,video_type,CHUNK_IN_MB,file_size, request):
        CHUNK_SIZE = int(CHUNK_IN_MB*(1024*1024))


        try:
            # < -- getting video current range in bytes from header it not available set default 0 -- >
            range_header = request.headers.get('Range',None)
            if(not range_header): raise Exception("RangeError")

            # < -- start and end video size in bytes -- >
            start = int(range_header.replace("bytes=","").split("-")[0])
            end = min(start + CHUNK_SIZE, file_size - 1)
            
            # < -- sending user data length in bytes -- >
            content_length = end - start + 1

            # < -- set response and content header -- >
            request.send_response(206)
            request.send_header("Content-Type", video_type)
            # < -- set headers and end -- >
            request.send_header("Content-Range", f"bytes {start}-{end}/{file_size}")
            request.send_header("Accept-Ranges", "bytes")
            request.send_header("Content-Length", content_length)
            request.end_headers()

            # < -- write file in bytes -- >
            with open(VIDEO_PATH, "rb") as file:
                file.seek(start)
                while content_length > 0:
                    chunk_size = min(CHUNK_SIZE, content_length)
                    chunk = file.read(chunk_size)
                    if not chunk:
                        break
                    request.wfile.write(chunk)
                    content_length -= len(chunk)
            return
        except Exception as  error:
            pass
        
        # < -- if user try to downlaod or request direct file without any broswer an he don't have any range -- >
        try:
            # < -- set response and content header -- >
            request.send_response(200)
            request.send_header("Content-Type", video_type)
            request.send_header("Content-Length", file_size)
            request.end_headers()
            # < -- write full file chunks by chunks -- >
            write_file_chunks(VIDEO_PATH,request)
        except:
            pass
    

# < -- create temp folder -- >
def Create_Folder(path):
    try:
        path = os.path.normpath(path)
        
        if not os.path.exists(path):
            os.makedirs(path)
        return path
    except:
        return False

# < -- it's get 3 arguments 1. oldtime 2. currenttime 3.second of diffrense if condtion setisfied it's reutrn true -- >
def within_time_limit(OldTimeStamp, CurrentTimeStamp, limit_seconds):
    # Convert timestamps to datetime objects
    dt1 = datetime.fromtimestamp(OldTimeStamp)
    dt2 = datetime.fromtimestamp(CurrentTimeStamp)

    # Calculate the absolute difference in seconds
    time_difference = abs((dt2 - dt1).total_seconds())

    # Check if the difference is less than the specified limit
    return time_difference < limit_seconds

# remove temp saved file if exist exceedingly remove give time 
def removeTempFile():
    try:
        TempFolders = os.listdir(temp_file_path)
        currentTime = int(time.time())
        time_limit = temp_file_remove_sec
        
        for oldDir in TempFolders:
            try:
                within_time = within_time_limit(int(oldDir),currentTime,time_limit)
                if not within_time:
                    removeTempPaths = (os.path.join(temp_file_path,oldDir))
                    shutil.rmtree(removeTempPaths)
            except:
                pass
    except:
        pass


# remove saved file immediately
def remvoe_form_files(files):
    for fileName in files:
        try:
            fileList = files[fileName]
            if(len(fileList)<=0):
                continue
            for fileInfo in fileList:
                try:
                    # Get the directory path from the input file path
                    directory_path = os.path.dirname(fileInfo["temp"])

                    # Go back two steps in the directory path
                    removeTempPaths = os.path.abspath(os.path.join(directory_path))

                    if(os.path.exists(removeTempPaths)):
                        shutil.rmtree(removeTempPaths)
                        break
                except:
                    pass
        except:
            pass