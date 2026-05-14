import matplotlib.pyplot as plt

employee_name =["Shardul","Sharali","Shayna","Siddhartha","Sharol","Vedanshi","Vivian","Shingini"]
employee_salary = [800,7654,876,765,345,456,1450,1330]

marks_perc = []
for x in employee_salary:
    res = (x/50)*100
    marks_perc.append(res)

print(marks_perc)

def percentage_bar_chart():
    plt.bar(employee_name,marks_perc)
    plt.title("Employee Salary Graph")
    plt.xlabel("Employee's Names")
    plt.ylabel("Employee's Salary")
    plt.show()

percentage_bar_chart()