class NoSecDef(Exception):
    super().__init__("No security definition found.")


class ConnError(Exception):
    super().__init__("Couldn't connect to TWS.")
