#-------------------------------------------------------------------------------
# Name: Ronald DeAngelis
# Assignment 2
# Due Date: 02/20/2022
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Zybooks, In-class materials, and preivous knowledge
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

def spectral_color(wavelength):
        result = ''
        #long if statment chain checking all of the wavelength options
        if wavelength < 380:
                result = 'ultraviolet'
        elif wavelength >= 380 and wavelength < 450:
                result = 'violet'
        elif wavelength >= 450 and wavelength < 485:
                result = 'blue'
        elif wavelength >= 485 and wavelength < 500:
                result = 'cyan'
        elif wavelength >= 500 and wavelength < 565:
                result = 'green'
        elif wavelength >= 565 and wavelength < 590:
                result = 'yellow'
        elif wavelength >= 590 and wavelength < 625:
                result = 'orange'
        elif wavelength >= 625 and wavelength < 750:
                result = 'red'
        else:
                result = 'infrared'
        
        return result

def robot_actions(side_sensor, front_sensor, dirt_sensor):
        result = ''
        #starts with dirt if because that takes precedent
        if dirt_sensor == 'clear':
                #front sensor has second precendence
                if front_sensor == 'clear':
                        #side sensor has last precedence
                        if side_sensor == 'clear':
                                #vacuum stop is checked for first
                                result = 'stop'
        #all else results are the other results based on the sensor triggered
                        else:
                                result = 'forward'
                else:
                        result = 'turn'
        else:
                result = 'vacuum'
        
        return result

def bad_broker(price, prev_price):
        result = ''
        #subtracts percentage from 100 to easier use in the if statments
        percent = 100 - price / prev_price * 100
        #if stock changed by 50% and it went up
        if percent < -50:
                result = 'BUY'
        #if stock changed by 50% and it went down
        elif percent > 50:
                result = 'HOLD'
        #stock did not changed by 50%
        else:
                result = 'SELL'
        
        return result
