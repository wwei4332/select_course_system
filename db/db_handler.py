import os
from conf import settings
import pickle
def save(obj):
    class_name = obj.__class__.__name__
    class_path = os.path.join(settings.DB_PATH, f'{class_name}')
    if not os.path.isdir(class_path):
        os.mkdir(class_path)
    obj_path = os.path.join(class_path, f'{obj.name}')
    with open(obj_path, 'wb') as fw:
        pickle.dump(obj, fw)


def read(cls,name):
    class_path = os.path.join(settings.DB_PATH, f'{cls.__name__}')
    obj_path = os.path.join(class_path, f'{name}')
    with open(obj_path, 'rb') as fr:
        obj=pickle.load(fr)
        return obj
