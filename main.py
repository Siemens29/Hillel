import names


def generate_male_name():
    male = names.get_full_name(gender='male')
    return male


print(generate_male_name())


def generate_female_name():
    female = names.get_full_name(gender='female')
    return female


print(generate_female_name())
