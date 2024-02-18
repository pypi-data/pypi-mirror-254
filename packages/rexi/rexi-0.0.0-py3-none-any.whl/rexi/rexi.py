import dataclasses
import re
import sys
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Input, Static, Header
import os


@dataclasses.dataclass
class GroupMatch:
    keys: list[int | str]
    value: str
    start: int
    end: int

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __repr__(self):
        return f"[bold]Group \"{'|'.join(map(str, self.keys))}\"[/]: \"{self.value}\""


# noinspection SpellCheckingInspection
class RexiApp(App):
    CSS_PATH = "rexi.tcss"

    def __init__(self, input_content: str):
        super().__init__()
        self.input_content = input_content

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter regex pattern")
        with ScrollableContainer(id="result"):
            with ScrollableContainer(id="output-container"):
                with Header():
                    yield Static("Result")
                yield Static(self.input_content, id="output")
            with ScrollableContainer(id="groups-container"):
                with Header():
                    yield Static("Groups")
                yield Static(id="groups")

    async def on_input_changed(self, message: Input.Changed) -> None:
        self.run_worker(self.update_regex(message.value), exclusive=True)

    async def update_regex(self, str_pattern: str) -> None:
        output_widget = self.query_one("#output", Static)
        groups_widget = self.query_one("#groups", Static)
        output_result = ""
        groups_result = ""
        if str_pattern:
            try:
                pattern = re.compile(str_pattern)
                output_result = self.create_highlight_output(pattern)
                groups_result = self.create_groups_output(pattern)
            except Exception as e:
                self.log(e)
                pass

        output_widget.update(output_result or self.input_content)
        groups_widget.update(groups_result)

    def create_highlight_output(self, pattern: re.Pattern) -> str:
        return pattern.sub(self.highlight_match, self.input_content)

    @staticmethod
    def highlight_match(match: re.Match):
        return '[red uu]{}[/]'.format(match.group(0))

    def create_groups_output(self, pattern: re.Pattern) -> str:
        match = pattern.match(self.input_content)
        groups = self.combine_groups(match)
        return "\n".join(map(repr, groups))

    def combine_groups(self, match: re.Match) -> list["GroupMatch"]:
        groups = [GroupMatch([index], group, start, end) for index, (group, (start, end))  in enumerate(zip(match.groups(), match.regs))]
        self.log(groups)
        for group_name, group in match.groupdict().items():
            start, end = match.span(group_name)
            group_match = GroupMatch([group_name], group, start, end)
            if group_match in groups:
                groups[groups.index(group_match)].keys.append(group_name)
        return groups


def main():
    stdin = sys.stdin.read()
    os.close(sys.stdin.fileno())
    sys.stdin = open('/dev/tty', 'rb')

    app = RexiApp(stdin)
    app.run()


if __name__ == "__main__":
    main()
