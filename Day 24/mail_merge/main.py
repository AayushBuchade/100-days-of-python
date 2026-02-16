
import os


def main():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f'{current_dir}/Input/Letters/starting_letter.txt') as file:
        template = file.read()

    with open(f'{current_dir}/Input/Names/invited_names.txt') as file:
        names = file.readlines()

    names = [name.strip() for name in names]

    for name in names:
        output = template.replace('[name]', name)
        with open(f'{current_dir}/Output/ReadyToSend/letter_to_{name}.txt', mode='w') as file:
            file.write(output)


if __name__ == "__main__":
    main()
