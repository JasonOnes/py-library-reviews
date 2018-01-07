""" imghdr mod simply determines the type of image in a file or byte stream"""

import os
import imghdr

def check_pics_for_suitable_file(suitable_file_type):
    # goes through my pictures looking for one that can be used for an image with a specific type
   
    source_directory = '/home/jasonones/Pictures'
    files_that_can_be_used = []
   
    for root, dirs, filenames in os.walk(source_directory):
        for name in filenames:
            name = '{}/{}'.format(source_directory, name)
            #log = open(os.path.join(root, name), 'r')
            
            try:
                if imghdr.what(name) is suitable_file_type:
                    files_that_can_be_used.append(name)
                
            except FileNotFoundError:
               # the folder is named (because of walk) but can't be opened from subdirectory (?) 
               # perhaps call imghdr recursively through additional looping of subdicts  
                pass       
               
    print("Here's a list of files that can be used: {}".format(files_that_can_be_used))

if __name__ == "__main__":
    check_pics_for_suitable_file('jpeg')
    check_pics_for_suitable_file('png')