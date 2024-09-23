import time

print(f"Cronometro 24h")
for d in range(0, 7, 1):
    for h in range(0, 24, 1):
        for m in range(0, 60, 1):
            for s in range(0, 60, 1):
                for ms in range(0, 60, 1):
                    print(f"{d:02d}:{h:02d}:{m:02d}:{s:02d}:{ms:02d}", end='', flush=True)
                    time.sleep(1/60)
                    print("\b" * (len(str(f"{d:02d}:{h:02d}:{m:02d}:{s:02d}:{ms:02d}"))), end='', flush=True)

