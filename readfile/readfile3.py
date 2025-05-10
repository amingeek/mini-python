import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data31.xlsx')

plt.figure(figsize=(10, 5))
plt.scatter(df['dama'], df['tedade tamir bokhari'], color='blue')
plt.title('تعداد تعمیر بخاری برحسب دما')
plt.xlabel('دما (°C)')
plt.ylabel('تعداد تعمیر')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(df['dama'], df['masrafe bargh'], color='red')
plt.title('مصرف برق برحسب دما')
plt.xlabel('دما (°C)')
plt.ylabel('مصرف برق (واحد نامشخص)')
plt.grid(True)
plt.show()

print("""
نتیجه‌گیری:
- با افزایش دما، تعداد تعمیرات بخاری کاهش می‌یابد (رابطه معکوس).
- با افزایش دما، مصرف برق به طور قابل توجهی افزایش می‌یابد (رابطه مستقیم).
- بنابراین، توان (مصرف برق) مستقیماً تحت تأثیر دماست و در دماهای بالاتر، سیستم انرژی بیشتری مصرف می‌کند.
""")