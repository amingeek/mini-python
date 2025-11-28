import numpy as np

# تعداد دانش‌آموزان و درس‌ها
num_students = 1000
num_subjects = 5

# ستون‌ها: ID، سن، ۵ درس
ids = np.arange(1001, 1001+num_students)           # ID از 1001 شروع
ages = np.random.randint(14, 19, size=num_students)  # سن بین 14 و 18
scores = np.random.randint(0, 101, size=(num_students, num_subjects))  # نمره بین 0-100

# ترکیب ستون‌ها
data = np.column_stack((ids, ages, scores))

# ذخیره در فایل
np.save('students_data.npy', data)
