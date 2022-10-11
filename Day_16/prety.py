from prettytable import PrettyTable
table = PrettyTable()
table.align = "l"
table.field_names = ["Pokemon Name","Type"]

table.add_rows(
    [
        ["Pikachu", "Lightining"],
        ["Charmander","Fire"],

    ]
)

print(table)