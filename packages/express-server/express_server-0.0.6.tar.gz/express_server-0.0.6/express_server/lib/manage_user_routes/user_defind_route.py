"""
this is a single route object contain path,method,and callbacks of route
"""

class NewRoute:
    def __init__(self,data):
        self.path = data["path"]
        self.method = data["method"]
        self.AllHandlers = [data["handlers"]]
        self.text = ''
        self.headers = []

    def addHandlers(self,newHandler):
        self.AllHandlers.append(newHandler)