from ..utils.paths import split_url,findParmas

def verifyPaths(requestPath,routePath,RequestData):
    # < -- if path is "*" -- >
    if((len(routePath) == 1 and routePath[0] == "*") or (len(routePath) == 2 and routePath[1] == "*")):
        return True
    
    # < -- if path maatch below in routePath -- >
    if routePath.find("/*") > 0 or routePath.find("/:") > 0:
        indexes_req_path = split_url(requestPath)
        indexes_route_path = split_url(routePath)

        # get all params 
        params = findParmas(indexes_req_path,indexes_route_path)
        
        if(params != False):
            try:
                # set params to request object 
                if(type(params).__name__ == "dict"):
                    RequestData._set_parmas(params)
            except:pass

            # path match send true 
            return True
        
    if requestPath == routePath:
        return True

    return False