from multiprocessing.sharedctypes import Value


def main():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"first name": "Sayr", "last name": "Olivares"}

    super_list = [
        {"firstname": "Sayr", "lastname": "Olivares"},
        {"firstname": "Ana", "lastname": "Herrera"},
        {"firstname": "Carla", "lastname": "Ortega"},
        {"firstname": "Facundo", "lastname": "García"},
    ]

    super_dict = {
        "natural_numbs": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    super_list = [
        {"firstname": "Sayr", "lastname": "Olivares"},
        {"firstname": "Ana", "lastname": "Herrera"},
        {"firstname": "Carla", "lastname": "Ortega"},
        {"firstname": "Facundo", "lastname": "García"},
    ]

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i["firstname"], "-", i["lastname"])

if __name__ == "__main__":
    main()