import pandas as pd

# โหลดข้อมูลคะแนนสอบ
df = pd.read_csv('Grades.csv')

# คำนวณคะแนนเฉลี่ย
mean = df['grade'].mean()

# ค้นหานักเรียนที่มีคะแนนเฉลี่ยต่ำกว่าคะแนนเฉลี่ย
low_scorers = df[df['grade'] < mean]

# ค้นหานักเรียนที่มีคะแนนเฉลี่ยสูงกว่าคะแนนเฉลี่ย
high_scorers = df[df['grade'] > mean]

print('mean : ', mean)

# แสดงข้อมูลของนักเรียนที่มีคะแนนเฉลี่ยต่ำกว่าคะแนนเฉลี่ย
print(low_scorers)

# แสดงข้อมูลของนักเรียนที่มีคะแนนเฉลี่ยสูงกว่าคะแนนเฉลี่ย
print(high_scorers)