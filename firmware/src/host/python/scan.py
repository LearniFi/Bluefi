import asyncio
import datetime
import sys
from bleak import BleakScanner

def detection_callback(device, advertisement_data):
    if "Bluefi" in (device.name or ""):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\033[92m[{now}] 📡 Found {device.name} @ {device.address} "
              f"(RSSI: {device.rssi} dBm)\033[0m")

async def run_scan(duration=None):
    """If duration is None → run until Ctrl+C, else run for that many seconds."""
    scanner = BleakScanner(detection_callback)
    await scanner.start()
    try:
        if duration is None:
            print("♾️ Continuous Bluefi scan started...")
            while True:
                await asyncio.sleep(1)
        else:
            print(f"🎨 Listening for Bluefi devices for {duration} seconds...")
            await asyncio.sleep(duration)
    except KeyboardInterrupt:
        pass
    finally:
        await scanner.stop()
        print("Scan stopped.")

if __name__ == "__main__":
    # Pass a number for fixed‑time scan, or leave empty for continuous
    secs = int(sys.argv[1]) if len(sys.argv) > 1 else None
    asyncio.run(run_scan(secs))
