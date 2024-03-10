from event_manager import EventManager
import listeners

ev = EventManager()

ev.emit('RECEIVED_DATA', 'Hello world')
ev.emit('END_PROGRAM')
ev.emit('NO_EXISTE')
print(ev.listeners)