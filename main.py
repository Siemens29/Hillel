import names


def generate_male_name():
    male = names.get_full_name(gender='male')
    return print(male)


generate_male_name()


def generate_female_name():
    female = names.get_full_name(gender='female')
    return print(female)


generate_female_name()


def random_family():
    male_name: str = ' '.join(names.get_full_name(gender='male').split(' ')[0:1])
    female_name = ' '.join(names.get_full_name(gender='female').split(' ')[0:1])
    last_name = ' '.join(names.get_full_name(gender='male').split(' ')[1:])
    return print(f"{male_name} and {female_name} {last_name}")


random_family()
