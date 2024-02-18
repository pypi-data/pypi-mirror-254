from .lib.http_server import Server,UserRoutes
from .lib.utils.express import ServerListenerHandler

def helper_add_route(path,handlers,method):
        resData = {"path": path,"method": method,"handlers": handlers}
        # add routes
        UserRoutes.AddNewRoute(resData)
class express:
    # < -- get request  -- >
    def get(self,path,handlers):
        helper_add_route(path,handlers,"GET")

    # < -- post request -- >
    def post(self,path,handlers):
        helper_add_route(path,handlers,"POST")

    # < -- PUT request  -- >
    def put(self,path,handlers):
        helper_add_route(path,handlers,"PUT")

    # < -- DELETE request  -- >
    def delete(self,path,handlers):
        helper_add_route(path,handlers,"DELETE")

    # < -- PATCH request  -- >
    def patch(self,path,handlers):
        helper_add_route(path,handlers,"PATCH")

    # < -- HEAD request  -- >
    def head(self,path,handlers):
        helper_add_route(path,handlers,"HEAD")

    # < -- OPTIONS request  -- >
    def options(self,path,handlers):
        helper_add_route(path,handlers,"OPTIONS")

    # < -- add all request  -- >
    def all(self,path,handlers):
        methods = ["GET","POST","PUT","DELETE","PATCH","HEAD","OPTIONS"]
        for METHOD in methods:
            helper_add_route(path,handlers,METHOD)
            

    # express.listen() handle listener
    def listen(self, port, *args):
        ServerListenerHandler(self, port, *args,Server=Server)