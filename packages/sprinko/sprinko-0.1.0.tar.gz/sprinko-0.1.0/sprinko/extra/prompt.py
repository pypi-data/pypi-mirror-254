from prompt_toolkit.application import Application, get_app
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import Dialog, Button, Box
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.formatted_text import HTML, merge_formatted_text
from prompt_toolkit.layout import Window
from prompt_toolkit.layout.dimension import Dimension
from prompt_toolkit.layout.margins import ScrollbarMargin

class TableSelector:
    """
    This class represents a table selector that uses the prompt toolkit to display a table in the terminal.

    :param table_data: The data for populating the table.
    :ivar table_data: The data to populate the table with.
    :ivar selected_line: The currently selected line in the table.
    :ivar column_widths: The calculated widths of the table columns.
    :ivar container: The window container for displaying the table.
    :method confirm_selection: Handles the confirmation action and saves the selected row.
    """
    def __init__(self, table_data):
        self.table_data = table_data
        self.selected_line = 1
        self.column_widths = self._calculate_column_widths()
        self.container = Window(
            content=FormattedTextControl(
                text=self._get_formatted_text,
                focusable=True,
                key_bindings=self._get_key_bindings(),
            ),
            style="class:select-box",
            height=Dimension(preferred=5, max=5),
            cursorline=True,
            right_margins=[ScrollbarMargin(display_arrows=True)],
        )

    def confirm_selection(self):
        """Handle the confirmation action and save the selected row."""
        if 0 <= self.selected_line < len(self.table_data):
            self.selected_row_data = self.table_data[self.selected_line]

    def _calculate_column_widths(self):
        # Calculate maximum width for each column
        widths = [0] * len(self.table_data[0])
        for row in self.table_data:
            for i, cell in enumerate(row):
                widths[i] = max(widths[i], len(str(cell)))
        return widths

    def _get_formatted_text(self):
        result = []
        for i, row in enumerate(self.table_data):
            if i == self.selected_line:
                result.append([("[SetCursorPosition]", "")])
            formatted_row = " | ".join(str(cell).ljust(width) for cell, width in zip(row, self.column_widths))
            result.append(HTML(formatted_row))
            result.append("\n")

        return merge_formatted_text(result)

    def _get_key_bindings(self):
        kb = KeyBindings()

        @kb.add("up")
        def _go_up(event):
            if self.selected_line == 0:
                self.selected_line = len(self.table_data) - 1
            elif self.selected_line == 1:
                self.selected_line = len(self.table_data) - 1
            else:
                self.selected_line = (self.selected_line - 1) % len(self.table_data)

        @kb.add("down")
        def _go_down(event):
            if self.selected_line == len(self.table_data) - 1:
                self.selected_line = 1
            else:
                self.selected_line = (self.selected_line + 1) % len(self.table_data)

        return kb

    def __pt_container__(self):
        return self.container

def create_table_selector(table_data, run : bool = True, returnDialog = False, title : str = "Table Selection Dialog") -> Application:
    """
    Create a table selector dialog with the given table data and options.

    Args:
        table_data (Any): The data to be displayed in the table selector.
        run (bool, optional): Flag to indicate whether to run the application. Defaults to True.
        returnDialog (bool, optional): Flag to indicate whether to return the table selector dialog. Defaults to False.
        title (str, optional): The title of the table selection dialog. Defaults to "Table Selection Dialog".

    Returns:
        Application or TableSelector: The application if returnDialog is False, otherwise the table selector dialog.
    """
    def confirm_clicked():
        table_selector.confirm_selection()  # Call the method to save the selection
        get_app().exit()

    def exit_clicked():
        get_app().exit()

    # Create the table selector
    table_selector = TableSelector(table_data)

    # Create the dialog body with buttons
    dialog_body = HSplit([
        Box(table_selector, padding=0, padding_left=1, padding_right=1),
        HSplit([
            Button("Confirm", handler=confirm_clicked),
            Button("Exit", handler=exit_clicked)
        ], padding=1)
    ])

    # Create the root container with dialog
    root_container = Dialog(
        title=title,
        body=dialog_body,
        with_background=True,
    )

    # Define and run the application
    application = Application(layout=Layout(root_container), full_screen=True)
    
    if run:
        application.run()
    
    if returnDialog:
        return table_selector
    else:
        return application    
        