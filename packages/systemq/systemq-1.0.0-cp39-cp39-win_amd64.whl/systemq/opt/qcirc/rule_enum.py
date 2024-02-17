from qcirc.rule import *  ;
from qcirc.pulse_will_enumeration import * ; 


R1= {
  "X":RULE_COMP( [ 
    ['1' , RULE(d0 =[[X_p()] , [I_p(width = 100e-9)]] , _align='center' ) ] ,
    [ '*' , RULE(d0 =[[X_p()]]) ]  ,
  ] ) ,
  "biasZ" :RULE(z0 = [[F_p()]]),
  
  "Y": RULE(d0 = [[Y_p()]]),
  "I": RULE(d0=[[I_p()]]),
  "X2": RULE(d0=[[X2_p()]]),
  "mX": RULE(d0=[[mX_p()]]),
  
  "mX2": RULE(d0=[[mX2_p()]]),
  "Y2": RULE(d0=[[Y2_p()]]),
  "mY2": RULE(d0=[[mY2_p()]]) ,
  "IX": RULE(d0=[[I_p(),X_p()]]),
  "IX2": RULE(d0=[[I_p(),X2_p()]]),
  
  "X12" :RULE(d0=[[X12_p()]]) ,
  "X23" :RULE(d0=[[X23_p()]]) ,
  "X232" :RULE(d0=[[X232_p()]]) ,
  
  "CZ": RULE(zc01=[[ F_p(), ]],d0=[[Vz_p()]],d1=[[Vz_p()]]),
  "CZnz":RULE(zc01=[[F_p(),F_p(amp_scale=-1)]],d0=[[Vz_p()]],d1=[[Vz_p()]])  ,

  "B" : RULE() , 
  "PIN" : RULE() , 
  "M" : RULE(pr=[[M_p()]]) ,
  "Volt": RULE(zc01=[[F_p(edge_shape='sine_edge')]]),
};

