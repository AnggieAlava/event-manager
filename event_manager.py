from singleton_decorator import singleton

@singleton
class EventManager:
    listeners = {}

    def register(self, name):
        def inner(func):
            if not self.listeners.get(name):
                self.listeners[name] = []
            self.listeners[name].append(func)

        return inner
    
    def emit(self, name, data=None):
        for func in self.listeners.get(name, []):
            func(data)