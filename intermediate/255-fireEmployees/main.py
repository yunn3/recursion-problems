def fireEmployees(employees: str, unemployed: str) -> list[str]:

    unemployed_dict = {fired: True for fired in unemployed}
    new_roaster = []

    for employee in employees:
        if unemployed_dict.get(employee) is None:
            new_roaster.append(employee)

    return new_roaster


print(
    fireEmployees(
        ["Steve", "David", "Mike", "Donald", "Lake", "Julian"],
        ["Donald", "Lake"],
    ),
)
