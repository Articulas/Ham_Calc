# App for math formulas

import math

def area_rectangle (length, width):
    area = length * width
    print (" ")
    print ("****** Result ******")
    print ("The area of the rectangle is " + str(area) + " square units")
    print ("********************")
    print (" ")
    input ("**** Press Enter to Continue ****")
    print (" ")
    
def area_triangle (base, height):
    tri_area = base * height / 2
    print (" ")
    print ("****** Result ******")
    print ("The area of the triangle is: " + str(tri_area) + " square units")
    print ("********************")
    print (" ")
    input ("**** Press Enter to Continue ****")
    print (" ")
    
def area_circle (radius):
    cir_area = 3.14 * radius **2
    print (" ")
    print ("****** Result ******")
    print ("The area of the circle is: " + str(cir_area) + " square units")
    print ("********************")
    print (" ")
    input ("**** Press Enter to Continue ****")
    print (" ")

def celsius_to_fahrenheit (degrees_celsius):
    degrees_fahrenheit = degrees_celsius * 9/5 + 32
    print (" ")
    print ("****** Result ******")
    print ("The temperature in fahrenheit is: " + str(degrees_fahrenheit))
    print ("********************")
    print (" ")
    input ("**** Press Enter to Continue ****")
    print (" ")
    
    #degrees_fahrenheit = degrees_celsius * 9/5 + 32
    return degrees_fahrenheit

def bmi_calc (height, weight):
    bmi = int(weight) / float(height) ** 2
    # print (int(bmi))
    print (" ")
    print ("****** Result ******")
    print ("The Body Mass Index is: " + str(int(bmi)))
    print ("********************")
    print (" ")
    input ("**** Press Enter to Continue ****")
    print (" ")
    
def band_wlength (freqcy):
    # Wavelength in meters equals 300 divided by frequency in mhz
    band_mtrs = 300 / float(freqcy)
    rounded_up = math.ceil(band_mtrs)
    # rounded_dwn = math.floor(band_mtrs)
    
    # print (int(band_mtrs))
    print (" ")
    print ("****** Result ******")
    print ("The Band Wave Length: " + str(band_mtrs) + str(rounded_up) + " meters")
    print ("********************")
    print (" ")
    input ("**** Press Enter to Continue ****")
    print (" ")
    
def btry_usg_ratio (amp_hour, avg_crnt):
        #To determine the length of time that equipment can be powered from a
        #battery, divide the battery ampere-hour rating by the average current
        #draw of the equipment. 
        hours_of_pwr = int(amp_hour) / int(avg_crnt)
        
def watt_calc (amps, volts):
    # Power is calculated as electromotive force times
    # electrical current: Amps times Volts equals Watts.
    watts = amps * volts

def ohms_law_volts (amps,ohms):
    # Volts = Amps * Ohms
    volts =amps*ohms
    
def ohms_law_amps (volts,ohms):
    # Amps = Volts / Ohms
    amps= volts/ohms
    
def ohms_law_ohms (volts,amps):
    # Ohms = Volts / Amps
    ohms = volts/amps
    
def dipole_length_calc ():
    # 1. Find Wave Length. 2. Covert Meters to Inches. 3. Find dipole length inches\portion (1/2, 1/4/ 5/8) 
    length=z
def amp_hours (cca,volts):
    ah = (cca/volts)
    
def adc_volts (adcVal):
    volTage = (3.3*int(adcVal))/65535
    print (" ")
    print ("****** Result ******")
    print ("Voltage is: " + str(volTage) + " volts")
    print ("********************")
    print (" ")
    input ("**** Press Enter to Continue ****")
    print (" ")
    
def volts_adc(inptVolts):
    dgiTl = (65535*float(inptVolts))/3.3
    print (" ")
    print ("****** Result ******")
    print ("Digital Value is:", int(dgiTl))
    print ("********************")
    print (" ")
    input ("**** Press Enter to Continue ****")
    print (" ")
       
    
# **App Engine**
while True:
    # Menu Display
    print ("=-=-= Main Menu =-=-=")
    print (" <<Area*Volum*Mass>>")
    print (" t = Area of a Triangle")
    print (" r = Area of a Rectangle")
    print (" c = Area of Circle")
    print (" <<Conversions and Misc>>")
    print (" f = Convert Celsius to Fahrenheit")
    print (" i = BMI Calculator")
    print (" <<Ham and Electronics>>")
    print (" b = Band Length Calculator")
    print (" q = Quit")
    print (" <<Robotics>>")
    print (" v = ADC (16bit) to Volts")
    print (" a = Volts to ADC (16 bit)")
    print ("=-=-=-=-=-=-=-=-")
    
    # **Menu Engine**
    menu_choice = input ("Enter: ")
    if menu_choice == "t":
        print (" ")
        tri_base = input ("Enter triangle base length: ")
        tri_height = input ("Enter triangle height length: ")
        area_triangle (int(tri_base), int(tri_height))
        
    elif menu_choice == "r":
        x_rect = input ("Enter rectangle length: ")
        y_rect = input ("Enter rectangle width: ")
        area_rectangle (int (x_rect), int (y_rect))
    
    elif menu_choice == "c":
        circle_radius = input ("Enter circle radius: ")
        area_circle(int (circle_radius))
        
    elif menu_choice == "f":
        celsius_temp = input ("Enter Temperature in Celsius: ")
        celsius_to_fahrenheit (int(celsius_temp))
        
    elif menu_choice == "b":
        freqcy = input ("Enter Frequency in MHZ: ")
        band_wlength (float(freqcy))
    
    elif menu_choice == "i":
        height = input ("Enter Height: ")
        weight = input ("Enter Weight: ")
        bmi_calc(height, weight)
            
    elif menu_choice == "q":
        break
    
    elif menu_choice == "v":
        digiVal = input ("Digital Value: ")
        adc_volts(digiVal)
        
    elif menu_choice =="a":
        usr_volts = input ("Voltage: ")
        volts_adc(usr_volts)
        
    
    else:
        pass
