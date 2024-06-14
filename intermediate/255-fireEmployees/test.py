def fireEmployees(employees: str, unemployed: str) -> list[str]:

    for i in range(len(employees)):
        if employees[i] in unemployed:
            employees.remove(employees[i])
            unemployed.remove(employees[i])

        if unemployed == []:
            return employees
