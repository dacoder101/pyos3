from func.io import list_input, tprint, key, cls


def personal():
    tprint("Configuring for personal...")
    cls()
    tprint("Successfully finished configuring for personal system type.")
    key()


def administrative():
    tprint("Configuring for administrative...")
    cls()
    tprint("Successfully finished configuring for administrative system type.")
    key()


def system_type():
    while True:
        cls()
        tprint(
            "What system type will pyos3 be configured for?\nThis cannot be changed without reseting pyos."
        )
        match list_input({"1": "Personal Use", "2": "Administrative/School"}):
            case "1":
                personal()
                break
            case "2":
                administrative()
                break
            case _:
                pass


def main():
    tprint("Welcome to pyos3.\nLet's configure your pyos3 setup to fit your needs.")
    key()
    system_type()


main()
