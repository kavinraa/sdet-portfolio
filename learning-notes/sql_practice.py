import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""
create table employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

employees = [
    (1, "Alice", "Engineering", 95000),
    (2, "Bob", "Engineering", 87000),
    (3, "Carol", "Engineering", 102000),
    (4, "Dave", "Sales", 65000),
    (5, "Eve", "Sales", 71000),
    (6, "Frank", "Sales", 58000),
]

cur.executemany("insert into employees values (?, ?, ?, ?)",  employees)
conn.commit()

print("database ready")

cur.execute("""   
    select distinct salary from employees
    order by salary desc
    limit -1
    offset 1
""")

salary = cur.fetchone()
print("Second highest salary : ", salary)

cur.execute("""select  outer_emp.name, outer_emp.department, outer_emp.salary 
    from employees outer_emp
    where outer_emp.salary = (
    select max(inner_emp.salary)
    from employees inner_emp
    where inner_emp.department = outer_emp.department
)
""")

print("highest salary per department :", cur.fetchall())