
import psycopg2


def database_connect(dbname_inp, user_inp, host_inp, password_inp):

    connect_str = str("dbname='" + dbname_inp + "' user='" + user_inp + "' host='" + host_inp +
                      "' password='" + password_inp + "'")
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor


def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for question in list_labels:
        user_input = input(question)
        inputs.append(user_input)
    return inputs if len(inputs) > 1 else inputs[0]


def print_menu(title, list_options, exit_message):
    print(title)
    for option in enumerate(list_options):
        print("({0}) {1}".format(option[0] + 1, option[1]))
    print("({0}) {1}".format("0", exit_message))

