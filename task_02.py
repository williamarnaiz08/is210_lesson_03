#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''QUESTION = float(raw_input("What is your blood pressure (from 90-160)?"))'''


BP_STATUS = float(input("What is your blood pressure? (Scale of 90-160)"

                     
if BP_STATUS < 90            
        print ( "Your blood pressure is Low.")
    elif BP_STATUS >= 90 and <= 119:                        
        print ("Your blood pressure is Ideal!")                       
    elif BP_STATUS >= 120 and <= 139:                        
        print ("Your blood pressure is getting a bit High. Keep and eye on it!")                        
    elif BP_STATUS >= 140 and <=160:
        print ("Your blood pressure is High! Consult a physician!")          
    elif BP_STATUS > 160:
        print ("Your blood pressure is Very High! Seek emergency help!")                       
    else:                        
        print ("That doesn't make sense.")
