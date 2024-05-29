import os
import asyncio
from aggregator import Aggregator
from vabus import VaBus, Event, Metric

async def main():
    vab_url = os.getenv('VABUS_URL')
    storage_type = os.getenv('STORAGE_TYPE')
    aggregation_interval = int(os.getenv('AGGREGATION_INTERVAL'))
    
    aggregator = Aggregator(interval=aggregation_interval)

    async with VaBus(vab_url) as vabus:
        asyncio.create_task(aggregator.run())

        while True:
            event = await vabus.get_event()
            if event:
                aggregator.add_event(event)
            
            metric = Metric(name="received_events", value=1)
            await vabus.send_metric(metric)


if __name__ == "__main__":
    asyncio.run(main())