import os
import fade

_LOGO_ = """
 
      (                                                              
   (  )\ )                                                           
 ( )\(()/(   (                                                       
 )((_)/(_))  )\                                                      
((_)_(_)) _ ((_)                                                     
 | _ | | | | | |                                                
 | _ | |_| |_| |                                                     
 |___|____\)__/  )           )                 *      *        (     
  *   ) ( /(  ( /(  *   ) ( /(         (     (  `   (  `       )\ )  
` )  /( )\()) )\()` )  /( )\())    (   )\    )\))(  )\))(  (  (()/(  
 ( )(_)((_)\ ((_)\ ( )(_)((_)\     )((((_)( ((_)()\((_)()\ )\  /(_)) 
(_(_())  ((_)  ((_(_(_()) _((_)   ((_)\ _ )\(_()((_(_()((_((_)(_))   
|_   _| / _ \ / _ |_   _|| || |  _ | (_)_\(_|  \/  |  \/  | __| _ \  
  | |  | (_) | (_) || |  | __ | | || |/ _ \ | |\/| | |\/| | _||   /  
  |_|   \___/ \___/ |_|  |_||_|  \__//_/ \_\|_|  |_|_|  |_|___|_|_\  
                                                                     
{ SABA KAAYO ANG SPEAKER LABAY PANA NINYO WAA MO!!!--for Educational purposes only :> } 


- By Harvy Jay| IG: @_eugene.hjsw | Github Jcodei6

"""

def print_logo():
    os.system("clear||cls")
    faded_logo = fade.water(_LOGO_)
    print(faded_logo)

if __name__ == "__main__":
    logo()
    

