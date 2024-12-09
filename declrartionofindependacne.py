import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(1, 6):
        await asyncio.sleep(10 / power)
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    n1 = asyncio.create_task(start_strongman("Citadel of Floor 19", 1))
    n2 = asyncio.create_task(start_strongman("Brian", 3))
    n3 = asyncio.create_task(start_strongman("Jamal", 5))
    await n1
    await n2
    await n3

asyncio.run(start_tournament())
