import streamlit as st

# GPA等级转换分数
def grade_to_points(grade):
    grade_map = {
        'O': 10.0, 'A+': 9.0, 'A': 8.0, 'B+': 7.0, 'B': 6.0, 'C': 5.5, 'F':0.0
    }
    return grade_map.get(grade.upper(), 0.0)

# 计算 GPA
def calculate_gpa(credits, grades):
    total_credits = 0
    weighted_sum = 0
    
    for credit, grade in zip(credits, grades):
        credit = int(credit)
        points = grade_to_points(grade)
        
        total_credits += credit
        weighted_sum += credit * points
    
    if total_credits == 0:
        return 0.0
    
    gpa = weighted_sum / total_credits
    return gpa

## 设置图标
st.set_page_config(page_title="GPA 计算器", page_icon=":mortar_board:")

st.title("GPA Calculator")

num_courses = st.number_input("输入有多少门课程:", min_value=1, step=1, value=1)

credits = []
grades = []

st.write("输入课程学分并选择对应等级:")


columns = st.columns(2)
for i in range(num_courses):
    
    with columns[0]:  # 学分 列
        credit = st.number_input(f"学分:", min_value=0, step=1, value=0, key=f"学分_{i}")
        credits.append(credit)
    
    with columns[1]:  # 等级 列
        grade = st.selectbox(f"等级:", ('O', 'A+', 'A', 'B+', 'B', 'C', 'F'), index=0, key=f"等级_{i}")
        grades.append(grade)

if st.button("开始计算 GPA"):
    gpa = calculate_gpa(credits, grades)    
    st.subheader(f"你的 GPA 是 {gpa:.2f}")


# 底部 创建4列，然后并排3列写作者
col = st.columns(4)
with col[3]:
    st.write("[inkglede](https://github.com/66my/gpa-calculator) 汉化翻译")





