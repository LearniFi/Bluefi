import asyncio
from bleak import BleakScanner

async def main():
    print("🔍 Scanning for Bluefi devices...")
    devices = await BleakScanner.discover()
    for d in devices:
        if "Bluefi" in (d.name or ""):
            print(f"Found {d.name} @ {d.address}")

asyncio.run(main())
