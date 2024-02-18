from ..utils.pages import Pages
from ..routes.RequestRoute import RequestRoute
from ..routes.ResponseRoute import ResponseRoute
from ..utils import styles
import traceback 
from ..utils.paths import normalize_path
from .handle_paths import verifyPaths
from ..utils.file_oprations import removeTempFile,remvoe_form_files

# < -- show html pages custom  -- >
pages = Pages()

class HandleRoutes:
    # < -- it's handle response or next requests (it's recursion  function it's run until next not founc)-- >
    def handle_next_handler(self,index,request,routes,method,RequestData=None,ResopnseData=None):
        # < -- first check request data available or not if not add -- >
        if not RequestData: 
            # < -- generate new user request using request object -- >
            RequestData = RequestRoute(method,request)
        
        # < -- find user requested url like:- /,/about,/user?name="Ok" -- >
        requestPath = normalize_path(RequestData.url)
        
        # < -- run loop current requested method from all routes -- >
        for routeIndex in range(0,len(routes.all_routes[method])):
                # < -- getting a single route it's reutrn [user defind route,number of routes] -- >
                currentRoute = routes.all_routes[method][routeIndex]
                # < -- find current route (route,count) -- >
                route = currentRoute[0]
                routePath = normalize_path(route.path)
                # verify all the path like /name /* /:name all this 
                verifyPath = verifyPaths(requestPath,routePath,RequestData)

                # < -- Match requested path and current path repalce %20 to blank space -- >
                # < -- if path not match continue  -- >
                if (not verifyPath):continue
                try:
                    # < -- if resonse data alrady exist don't add new -- >
                    if not ResopnseData: ResopnseData = ResponseRoute()

                    CallbackResponse = None
                    try:
                        # < -- user callback handler resonse.send or resonse.next -- >
                        CallbackResponse = route.AllHandlers[index](RequestData,ResopnseData,ResopnseData.next)
                    except Exception as error:
                         # < -- remvoe formfiles from temp foder -- >
                        remvoe_form_files(RequestData.files)
                        raise error
                    
                    # < -- check user reponse  -- >
                    ResponseState = CallbackResponse
                    if(ResponseState == "end"):
                        try:
                            # < -- remvoe formfiles from temp foder -- >
                            remvoe_form_files(RequestData.files)
                            
                            # < -- finaly do last opration -- >
                            pages.Send(request,ResopnseData,method)
                        except Exception as error:
                             pages.error(request,f"Internal Server Error:{error}")
                        return True
                    elif(ResponseState == "next"):
                        if(index<currentRoute[1]):
                            self.handle_next_handler(index+1,request,routes,method,RequestData,ResopnseData)
                        else:
                            pages.error(request,f"Error:- Thare Is Not Any Next() Response at "+request.path)
                        return True
                    else:
                        pages.error(request,f"Error:- Return Some Values at "+request.path)
                        return True
                except Exception as error:
                    # < -- console the full traceback of error -- >
                    traceback.print_exc()  
                    # show repsone error page 
                    pages.error(request,f"Internal Server Error:{error}")
                    
                    return True
        
        # < -- it don't found any page -- >
        return False
    
    # < -- handler new get request -- > 
    def handle_user_request(self,request,routes,method):
        # < -- removing unknown temp files if not removed -- >
        removeTempFile()

        try:
            # < -- check method available or not  -- >
            try:
                if len(routes.all_routes[method]) > 0:
                    pass
            except:
                return

            # < -- check routes exit or not inside user defined routes -- >
            if len(routes.all_routes)<=0:
                # if route not exist show 404 error 
                pages.show404(request)
            
            # < -- handle get request -- >
            elif not self.handle_next_handler(0,request,routes,method):
                # < --  if handle_next_handler return false then show 404 error  -- >
                pages.show404(request)
                
        except Exception as error:
            traceback.print_exc()  
            # < -- if any error occurred show 505 server error -- >
            styles.redText(error)
            pages.default("Internal Server Error",request,500)
            return None 