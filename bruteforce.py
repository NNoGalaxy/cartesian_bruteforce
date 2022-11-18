from string import * 
import itertools
Alph = ascii_lowercase + ascii_uppercase + ascii_letters + "!@#$%^&*()-=_+[]{};',.<>\/"


for length in range(1000):
    for i in itertools.product(Alph,repeat=length):
        
        w = "".join(i)
        print(w)
        
    
    