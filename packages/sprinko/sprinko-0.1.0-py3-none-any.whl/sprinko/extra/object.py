import json 
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
def json_serializable(obj):
    try:
        json.dumps(obj)
        return True
    except: # noqa
        return False