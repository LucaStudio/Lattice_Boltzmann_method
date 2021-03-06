# Autogenerated with SMOP 
from smop.core import *
# 

    
@function
def computehydrostaticpressure3D(rho=None,cssq=None,*args,**kwargs):
    varargin = computehydrostaticpressure3D.varargin
    nargin = computehydrostaticpressure3D.nargin

    ##
#        Project: Fluid - structure interaction on deformable surfaces
#         Author: Luca Di Stasio
#    Institution: ETH Zrich
#                 Institute for Building Materials
# Research group: Computational Physics for Engineering Materials
#        Version: 0.1
#  Creation date: May 30th, 2014
#    Last update: June 3rd, 2014
    
    #    Description: 
#          Input: 
#         Output:
    
    ##
    
    p=multiply(cssq,rho)
    return p