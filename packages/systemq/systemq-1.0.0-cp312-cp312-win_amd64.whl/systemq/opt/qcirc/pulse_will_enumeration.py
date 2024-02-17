##################################################################
###################  Pusle Will Enumeration ######################
# In this file provides some default enumeration of the 
# will of the pulse. For development purpose it is encoraged
# to inheret this file, or inheret directly from "pulse_will"
# to create users own pulse_will.
#
# Every enumeration of the will, since it is related to the 
# specfic method of recording the calibrated parameters.
# They are experiment related, that is why when dealing with them.
# They are not nessesarily counted as integrated core part of 
# an this package .
#
# And because of that, this file here serves as an example, or an 
# ready to use default. It is not encoraged to directly modify.
# 
# All the core functional parts howerver,  as well as thier easy 
# to understand functionalities, and how to use documentations.
# are provieded in "pulse_will".
#
# As a beginer, to be able to very quickly harness the the pulse_will
# please seek for simple examples. that utilizes the pulse_will.
# Any complicated experiments can be easily formulated with good 
# understanding of the process provided in the very simple examples.

import numpy as np ;
import qcirc.pulse_will as pw ; 
pi = np.pi ; 
pi2 = np.pi/2 ; 

def pi_gate(w,cp) : 
  w.update(cp['pi'])
  w["vz"] += cp['pi']["phase_offs"] ; 

def pi2gate(w,cp) : 
  w.update(cp['pi2'])
  w["vz"] += cp['pi2']["phase_offs"] ; 

class I_p(pw.PulseWill):  
  __mnr_type__  = "I_p" ;
  def will(self,w,cp): w["amp"] = 0 ; w["width"]  =0;  w["plateau"] =0 ; 
  
class X_p(pw.PulseWill):
  __mnr_type__="X_p"; 
  def will(self,w,cp):pi_gate(w,cp);  w["phase"] = 0 ; 

class Y_p(pw.PulseWill):
  __mnr_type__="Y_p"; 
  def will(self,w,cp):pi_gate(w,cp);   w["phase"] = pi/2 ; 

class mX_p(pw.PulseWill):
  __mnr_type__="mX_p"; 
  def will(self,w,cp):pi_gate(w,cp);   w["phase"] = pi ; 

class mY_p(pw.PulseWill):
  __mnr_type__="mY_p"; 
  def will(self,w,cp):pi_gate(w,cp); w["phase"] = 3*pi/2 ; 


class X2_p(pw.PulseWill):
  __mnr_type__="X2_p"; 
  def will(self,w,cp):pi2gate(w,cp);  w["phase"] = 0 ; 

class Y2_p(pw.PulseWill):
  __mnr_type__="Y2_p"; 
  def will(self,w,cp):pi2gate(w,cp);  w["phase"] = pi/2 ; 

class mX2_p(pw.PulseWill):
  __mnr_type__="mX2_p"; 
  def will(self,w,cp):pi2gate(w,cp);  w["phase"] = pi ; 


class mY2_p(pw.PulseWill):
  __mnr_type__="mY2_p"; 
  def will(self,w,cp):pi2gate(w,cp);  w["phase"] = 3*pi/2 ; 

class F_p(pw.PulseWill):
  __mnr_type__="F_p"; 
  def will(self,w,cp): w.update(cp["fp"]);  w["freq"] = 0 ; 


class W_p(pw.PulseWill):
  __mnr_type__="Y_p"; 
  def will(self,w,cp): pi_gate(w,cp);   w["phase"] = pi/4  ; 

class mW_p(pw.PulseWill):
  __mnr_type__="mW_p"; 
  def will(self,w,cp): pi_gate(w,cp);   w["phase"] = 5*pi/4 ; 

class W2_p(pw.PulseWill):
  __mnr_type__="W2_p"; 
  def will(self,w,cp):   pi2gate(w,cp);  w["phase"] = pi/4  ; 

class mW2_p(pw.PulseWill): 
  __mnr_type__="mW2_p"; 
  def will(self,w,cp): pi2gate(w,cp);   w["phase"] = 5*pi/4 ; 

class VZ_left_p(pw.PulseWill):
  __mnr_type__="VZ_left_p"; 
  def will(self,w,cp): 
    w['amp'] = 0 ; 
    w['vz'] = cp["vz_left"];

class VZ_right_p(pw.PulseWill):
  __mnr_type__="VZ_left_p"; 
  def will(self,w,cp): 
    w['amp'] = 0 ; 
    w['vz'] = cp["vz_right"]; 


class Vz_p(pw.PulseWill) :
  __mnr_type__ = "Vz_p" ; 
  def will(self,w,cp):
    w["width"]= 0;  w["plateau"] = 0 ;  w["amp"] = 0 ; 
    w["vz"] = cp["vz"] ; 


def pi12_gate(w,cp) : 
  w.update(cp['pi12'])
  w["vz"] += cp['pi12']["phase_offs"] ; 


def pi23_gate(w,cp) : 
  w.update(cp['pi23'])
  w["vz"] += cp['pi23']["phase_offs"] ; 


class X12_p(pw.PulseWill) :
  __mnr_type__ = "X12_p" ; 
  def will(self,w,cp,ctx): pi12_gate(w,cp,ctx)  


class X23_p(pw.PulseWill) :
  __mnr_type__ = "X23_p" ; 
  def will(self,w,cp,ctx): pi23_gate(w,cp,ctx)  


class X232_p(pw.PulseWill) :
  __mnr_type__ = "X232_p" ; 
  def will(self,w,cp): 
    pi23_gate(w,cp); 
    w["amp"] =  w["amp"]/2; 


class Xf0g1_p(pw.PulseWill):
  __mnr_type__ = "Xf0g1_p" ; 
  def will(self,w,cp,ctx): w.update(cp['f0g1']) ; 


class Coup_off_p(pw.PulseWill):
  __mnr_type__="Coup_off_p"; 
  def will(self,w,cp): 
    w["amp"]= cp["offamp"];  
    w["freq"] = 0 ;
    w["width"] = 0 ;  
    w["plateau"]  = cp["offplateau"] ;



#############################################
############ Measurement Pusle ##############

class M_p(pw.PulseWill):
  __mnr_type__ = "M_p"; 
  def will(self,w,cp):  
    w.update(cp["M01"]);

