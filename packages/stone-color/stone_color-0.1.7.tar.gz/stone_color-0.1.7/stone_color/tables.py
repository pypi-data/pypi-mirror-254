import io

def ascii_table(header: list[str], data: list[list[str]], spaces=4, lspace=2, start_end="") -> str:
    table = io.StringIO()
    
    div = " "*spaces
    ldiv = " "*lspace

    col_widths = [max(len(str(cell)) for cell in col) for col in zip(header, *data)]

    header_row = div.join(f"{header: <{width}}" for header, width in zip(header, col_widths))
    table.write(start_end + ldiv + header_row + "\n")

    separator_row = div.join("-" * width for width in col_widths)
    table.write(ldiv + separator_row + "\n")

    for row in data:
        row_str = div.join(f"{cell: <{width}}" for cell, width in zip(row, col_widths))
        table.write(ldiv + row_str + "\n")

    table.write(start_end)

    return table.getvalue()

def unicode_light_table(header: list[str], data: list[list[str]], lspace=0, start_end="") -> str:
    table = io.StringIO()

    ldiv = " "*lspace
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data, header)]

    table.write(start_end + ldiv + "┌" + "─" * (sum(col_widths) + len(col_widths) * 3 - 1) + "┐\n")
    table.write(ldiv + "│")
    for header_item, width in zip(header, col_widths):
        table.write(f" {header_item.ljust(width)} │")
    table.write("\n" + ldiv + "├" + "─" * (sum(col_widths) + len(col_widths) * 3 - 1) + "┤\n")

    for row in data:
        table.write(ldiv + "│")
        for item, width in zip(row, col_widths):
            table.write(f" {item.ljust(width)} │")
        table.write("\n")

    table.write(ldiv + "└" + "─" * (sum(col_widths) + len(col_widths) * 3 - 1) + "┘" + start_end)

    return table.getvalue()


def unicode_heavy_table(header: list[str], data: list[list[str]], lspace=0, start_end="") -> str:
    table = io.StringIO()

    ldiv = " "*lspace
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data, header)]

    table.write(start_end + ldiv + "╔" + "═" * (sum(col_widths) + len(col_widths) * 3 - 1) + "╗\n")
    table.write(ldiv + "║")
    for header_item, width in zip(header, col_widths):
        table.write(f" {header_item.ljust(width)} ║")
    table.write("\n" + ldiv + "╠" + "═" * (sum(col_widths) + len(col_widths) * 3 - 1) + "╣\n")

    for row in data:
        table.write(ldiv + "║")
        for item, width in zip(row, col_widths):
            table.write(f" {item.ljust(width)} ║")
        table.write("\n")

    table.write(ldiv + "╚" + "═" * (sum(col_widths) + len(col_widths) * 3 - 1) + "╝" + start_end)

    return table.getvalue()
