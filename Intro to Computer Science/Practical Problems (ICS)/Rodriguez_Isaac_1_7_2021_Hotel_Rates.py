guest = int(input('How Many Guests Total? ')) #Number of Guests
night = int(input('How Many Nights are You Staying? ')) #Number of Nights Planned to Stay
if guest == 1: #Runs Code Below if Number of Guests is 1 ($50 per night)
    print('Total Cost: $' + str(50 * night))
elif guest == 2: #Runs Code Below if Number of Guests is 2 ($75 per night)
    print('Total Cost: $' + str(75 * night))
elif guest > 2: #Runs Code Below if Number of Guests is 3 or higher
    suite = input('Would You Like a Normal ($200) or Deluxe Suite ($300)? ').lower()
    if suite == 'normal': #Runs Code Below if Normal is Requested ($200 per night)
        print('Total Cost: $' + str(200 * night))
    elif suite == 'deluxe': #Runs Code Below if Deluxe is Requested ($300 per night)
        print('Total Cost: $' + str(300 * night))