import time
import datetime

print("🚀 Bắt đầu chạy tác vụ trên mây của GitHub Actions...")

for i in range(1, 6):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] Đang thực hiện chu kỳ chạy thứ {i} trên server mây...")
    time.sleep(2)

    print("✅ Hoàn thành tác vụ!")
  
