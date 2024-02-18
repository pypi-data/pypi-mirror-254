"""

futurevision/__init__.py

   _____                _           _   _                      _ _   ______    _ _     
  / ____|              | |         | | | |               /\   | (_) |  ____|  | (_)    
 | |     _ __ ___  __ _| |_ ___  __| | | |__  _   _     /  \  | |_  | |__   __| |_ ___ 
 | |    | '__/ _ \/ _` | __/ _ \/ _` | | '_ \| | | |   / /\ \ | | | |  __| / _` | / __|
 | |____| | |  __/ (_| | ||  __/ (_| | | |_) | |_| |  / ____ \| | | | |___| (_| | \__ \
  \_____|_|  \___|\__,_|\__\___|\__,_| |_.__/ \__, | /_/    \_\_|_| |______\__,_|_|___/
                                               __/ |                                   
                                              |___/

"""

import platform

if platform.system() == 'Windows':
    from futurevision import vision
    from futurevision import arduino
    from futurevision import iphone
elif platform.system() == 'Darwin':
    from futurevision import vision
    from futurevision import arduino
    from futurevision import iphone
else:
    from futurevision import vision
    from futurevision import arduino
    from futurevision import iphone
    from futurevision import raspberrypi
    

