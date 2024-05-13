hotel = {
    "1": {"101": ["George Jefferson", "Wheezy Jefferson"]},
    "2": {"237": ["Jack Torrance", "Wendy Torrance"]},
    "3": {"333": ["Neo", "Trinity", "Morpheus"]},
}


def start_check_in_or_out():
    checkinout = None
    while checkinout == None:
        checkinout = input("Are you checkin in, or out?").lower()
        if checkinout == 'in' or checkinout == 'out':
            return checkinout
        else: 
            print('I\'m sorry, I only understand "in" or "out". Please reply with "in" or "out".')
            checkinout = None

def get_room_and_floor(in_or_out):
    if in_or_out == 'in':
        floor = int(input('Which floor would you prefer?'))
        room = int(input('Which room would you prefer?'))
    if in_or_out == 'out': 
        floor = int(input('Which floor was your room on?'))
        room = int(input('Which room are you checking out of?'))
    return floor, room

def is_room_empty(floor,room): 
    if floor in hotel.keys():
        if room in hotel[floor].keys() and len(hotel[floor][room]) > 0:
            return False
        else:
            return True
    else: 
        return True
    return False


    