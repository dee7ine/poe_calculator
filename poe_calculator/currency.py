#!.\venv\Scripts\python.exe
import aiohttp
import asyncio
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

async def get_currency_json(league: str, type: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://poe.ninja/api/data/currencyoverview?league={league}&type={type}') as response:
            with open('response.json', 'wb') as out:
                async for chunk in response.content.iter_chunked(4096):
                    out.write(chunk)
                return True
                    
if __name__ == "__main__":      
    asyncio.run(get_currency_json(league='Crucible', type='Currency'))