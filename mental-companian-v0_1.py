"""
An app that keep tracking mental health of the user,
 when discover subhealth symptom, LLM comes in to make user feel better.
"""

import datetime
import pytz


def send_inquiries(hour_number=8):
    """
    get Mental state on specific time
    """
    if hour_number:
        hour_number = hour_number
    else:
        beijing_tz = pytz.timezone('Asia/Shanghai')
        now = datetime.datetime.now(beijing_tz)
        #current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        hour_number = now.strftime("%H")
    if hour_number == 8:
        print('this should be an inquiries')
        print("how do you feel from 1 to 10, 1 is the worst, 10 is the best.")
        mental_states = input('how do you feel now?')
    elif hour_number == 15:
        print('this should be an inquiries')
        mental_states = input('how do you feel now?')        
    elif hour_number == 22:
        print('this should be an inquiries')
        mental_states = input('how do you feel now?')

    # running on the back ground and catch extreme emotional moment
    else:
        print('this should be an inquiries too')
        mental_states = input('how do you feel now?')

    return mental_states

def test_states(timehour):
    timehour == 8
    states = send_inquiries(timehour)
    if states:
        print('test success')
        print(states) 
    else:
        print('test fail')


def get_small_talk_theropy():

    """
    After get inquiries, send corresponding messages
    get LLMs respons to make this more empathy
    """

    mental_states = int(send_inquiries())

    if mental_states >= 7:
        print('keep your happy mood')
        print('need plan for something just ask me')
        #output with LLMs
    
    elif mental_states <= 3:
        print('what happened i am here to help')
        #output with LLMs
    else:
        print('not good not bad')
        print('take deep breath and carry on')
        #output with LLMs


def test_get_talk():
    get_small_talk_theropy()
