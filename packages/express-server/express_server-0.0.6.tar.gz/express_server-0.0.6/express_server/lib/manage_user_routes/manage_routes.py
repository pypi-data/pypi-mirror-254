from typing import Any
from .user_defind_route import NewRoute

"""
in this object we have all the routes that user defind using res.route we fillter that route and add all routes object.
AddNewRoute is Apending new route on our object

all routes sotre data like this format we devide routes by method
allroutes = {
                "GET": [routeObj(path,method,handler),routeObj(path,method,handler]
                "POST": [routeObj(path,method,handler),routeObj(path,method,handler]
                etc.
                .
                .
            }
"""
class MangaeRoutes:
    def __init__(self):
        # < -- all the routes any method -- >
        self.all_routes = {}
    
    
    # < -- add new route in all_routes dictionary -- >
    def AddNewRoute(self, resData):
        # < -- Defice route by methods -- >
        try:
            # Check if the method key exists, and create an empty list if not
            self.all_routes[resData["method"]]
        except KeyError:
            # if route list not exit add new list 
            self.all_routes[resData["method"]] = []

        # < -- Append a new ResRoute instance to the method -- >
        if(len(self.all_routes[resData["method"]]) == 0):
                newResponse = [NewRoute(resData),0]
                self.all_routes[resData["method"]].append(newResponse)
        else:
             for route in self.all_routes[resData["method"]]:
                  if(resData["path"] == route[0].path):
                       route[0].addHandlers(resData["handlers"])
                       route[1] = route[1]+1
                       break
             else:
                newResponse = [NewRoute(resData),0]
                self.all_routes[resData["method"]].append(newResponse)