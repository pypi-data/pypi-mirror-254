from .attributes import Attributes

attributes = Attributes()

class Pages:
    def Send(self,request,route,method):
        # < -- if send file exist -- >
        if(route.sendfilepath):
            attributes.sendfile(route,request,method)
        # < -- send simple text -- >
        elif(route.download_obj):
            # < -- downlaod file  -- >
            attributes.download_file(route,request,method)
        else:
            # < -- set status code  -- >
            request.send_response(route.statusCode)
            # < -- add haders -- >
            attributes.setHeader(request,route.headers)
            attributes.endHeader(request)
            attributes.addText(route.text,request)
        
    def default(self,text,request,response_code=200):
        request.send_response(response_code)
        attributes.setHeader(request)
        attributes.addText(text,request)

    def show404(self,request):
        request.send_response(400)
        attributes.setHeader(request,[],True)
        attributes.addText('<h2 align="center">404 Not Found !</h2>',request)

    def error(self,request,error):
        request.send_response(500)
        attributes.setHeader(request,[],True)
        attributes.addText(f"""<h2 style="color: red;text-align: center;">{error}</h2""",request)