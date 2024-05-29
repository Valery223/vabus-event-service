from vabus import Event
import asyncio

class Aggregator:
    def __init__(self, interval: int):
        self.interval = interval
        self.events = {}
    
    def add_event(self, event: Event):
        pass
    
    def aggregate_events(self):
        pass

    async def send_to_storage(self):
        '''
        send to kafka or postgresql
        '''
        pass

    async def run(self):
        while True:
            await asyncio.sleep(self.interval)
            aggregate_data = self.aggregate_events()
            await self.send_to_storage(aggregate_data)