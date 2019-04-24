# import random
# from datetime import datetime

# class Robot(object):
    
#     def __init__(self):
#         self.name = self.generate_name()

#     def generate_name(self):
#         temp_str = self.randomAZ() + self.randomAZ() + self.random_number() + self.random_number() + self.random_number()
#         return temp_str
   
#     def randomAZ(self):
#         random.seed(datetime.now())
#         return chr(random.randint(65,90))

#     def random_number(self):
#         return str(random.randint(0,9))

#     def reset(self):
#         self.__init__()


# ******** Improved Version *********
import random
import string
from datetime import datetime

class Robot(object):

    def __init__(self):
        self.name = self.generate_name()
    
    def generate_name(self):
        random.seed(datetime.now())
        str_result = ''.join(random.choices(string.ascii_uppercase,k=2)) + ''.join(random.choices(string.digits,k=3))
        return str_result
    
    def reset(self):
        self.__init__()