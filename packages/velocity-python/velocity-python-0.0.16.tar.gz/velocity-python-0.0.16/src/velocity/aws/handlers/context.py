import support.app

engine = support.app.postgres()

@engine.transaction
class Context:
    def __init__(self, args, postdata, response, aws_event, session, aws_context):
        self.__args = args
        self.__postdata = postdata
        self.__response = response
        self.__session = session
        self.__aws_event = aws_event
        self.__aws_context = aws_context

    
    def postdata(self, keys=-1, default=None):
        if keys == -1:
            return self.__postdata 
        if not isinstance(keys, list):
            keys = [keys]
        data = self.__postdata
        for key in keys:
            if key in data:
                data = data[key]
            else:
                return default
        return data
    
    
    def payload(self, keys=-1, default={}):
        if 'payload' not in self.__postdata:
              return default
        if keys == -1:
            return self.__postdata['payload']
        if not isinstance(keys, list):
            keys = [keys]
        data = self.__postdata['payload']
        for key in keys:
            if key in data:
                data = data[key]
            else:
                return default
        return data
    
    def action(self):
        return self.__postdata('action', self.__args('action', ''))