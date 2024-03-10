from event_manager import EventManager

ev = EventManager()

@ev.register('RECEIVED_DATA')
def received_data(event):
    print(list(event))
    
@ev.register('RECEIVED_DATA')
def recevied_data2(event):
    print(f'Got data: {event}')

@ev.register('END_PROGRAM')
def on_exit(event):
    print('Goodbye')