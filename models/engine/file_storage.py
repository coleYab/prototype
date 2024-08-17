#!/usr/bin/env python3

import json

class FileEngine:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__objects = {}

    def save(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()
        # write to the file after that
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def all(self, class_name=None):
        if class_name is not None:
            filtered_data = filter(lambda tup: tup[0].split('.')[0] == class_name, self.__objects.items())
            return list(map(lambda tup: tup[1], filtered_data))

        return list(self.__objects.values())

    def reload(self):
        try:
            with open(self.__file_path) as file:
                self.__objects = json.load(file)
        except:
            pass

    def destroy(self, class_name, id):
        key = f"{class_name}.{id}"
        if key not in self.__objects.keys():
            raise Exception("Unable to delete the user the user doesn't exist")

        del self.__objects[key]

    def show(self, class_name, id):
        key = f"{class_name}.{id}"
        if key not in self.__objects.keys():
            raise Exception("Unable to show the object the user don't found")
    
        return self.__objects[key]
