import sys
from dataclasses import KW_ONLY, dataclass
from typing import *  # type: ignore

from . import argument_parser, common
from .errors import (
    AmbiguousOptionError,
    ArgumentError,
    NoOptionGivenError,
    NoSuchOptionError,
)
from .legacy import error, print, warning


@dataclass(frozen=True)
class Parameter:
    name: str
    _ = KW_ONLY
    summary: str | None = None
    prompt: str | None = None


@dataclass(frozen=True)
class AppCommand:
    # The name to use for this command
    name: str

    # Additional names that can be used to invoke this command
    aliases: Set[str]

    # Short description of the command
    summary: str | None

    # Longer, detailed description of the command
    details: str | None

    # Any parameters the user has provided to describe this command. These may
    # be fewer than the function's parameters, or empty altogether.
    user_provided_parameters: list[Parameter]

    # The function to call when this command is invoked
    function: Callable


class App:
    def __init__(
        self,
        *,
        name: str | None = None,
        summary: str | None = None,
        details: str | None = None,
        add_help_command: bool = True,
        add_version_command: bool = True,
    ):
        if name is None:
            self.name = "TODO-auto-detect-app-name"
        else:
            self.name = name.strip()

        self.summary = None if summary is None else summary.strip()
        self.details = None if details is None else common.multiline_strip(details)
        self._commands: list[AppCommand] = []

        # Add built-in commands
        if add_help_command:
            self.command(
                name="help",
                summary="Display help for a command",
                details="""
If not command is provided, this command will show general help for the
application. If a command is provided, shows help for that command instead.
                """,
            )(self._display_help)

        if add_version_command:
            self.command(
                name="version",
                summary=f"Display version information for {self.name}",
            )(self._display_version)

    def _display_help(self, command: str | None = None) -> None:
        # Was a valid command specified?
        cmd_instance: AppCommand | None = None

        if command is not None:
            try:
                all_names_and_aliases: list[list[str]] = []

                for cmd in self._commands:
                    all_names_and_aliases.append([cmd.name] + list(cmd.aliases))

                cmd_index = common.choose_string(
                    all_names_and_aliases,
                    command,
                )
            except NoSuchOptionError as err:
                error(f"There is no command named `{err.entered_command}`")
                print()
            except AmbiguousOptionError as err:
                error(err.message)
                print()
            else:
                cmd_instance = self._commands[cmd_index]

        # If not command was provided, or the given one doesn't exist, display
        # general help
        if cmd_instance is None:
            # Summary
            if self.summary is not None:
                print(self.summary)

            # Usage
            print()
            print(f"[dim]Usage:[/] {sys.argv[0]} <command> [dim][[options ...][/]")

            # Commands
            print()
            print(f"Available commands are:")
            align_len = max(len(cmd.name) for cmd in self._commands)
            self._commands.sort(key=lambda cmd: cmd.name.lower())

            for cmd_instance in self._commands:
                if cmd_instance.summary is None:
                    summary = ""
                else:
                    summary = f"  ...  {cmd_instance.summary}"

                print(f"  [primary]{cmd_instance.name:<{align_len}}[/]{summary}")

            # Details
            if self.details is not None:
                print()
                print(self.details)

            return

        # If the command was referenced via an alias, point the user to the
        # canonical name
        if command != cmd_instance.name:
            warning(
                f"Showing help for command [primary]{cmd_instance.name}[/], since there is no command named [primary]{command}[/]"
            )
            print()

        # A command was provided. Display information about that command
        # specifically
        assert cmd_instance is not None, cmd_instance
        if cmd_instance.summary is None:
            print(f"[bold primary]{cmd_instance.name}[/]")
        else:
            print(
                f"[bold primary]{cmd_instance.name}[/]  \u2014  {cmd_instance.summary}"
            )

        # Usage
        print()
        parsed_parameters = list(
            argument_parser.parameters_from_function(cmd_instance.function)
        )

        params_str = ""
        for inspect_param, revel_param in parsed_parameters:
            # Format the parameter
            is_optional = revel_param.default_value is not argument_parser.NO_DEFAULT

            if not is_optional and not revel_param.is_flag:
                param_str = f"<{revel_param.name}>"
            else:
                if revel_param.is_flag:
                    if revel_param.type is bool:
                        param_str = f"--{revel_param.name}"
                    else:
                        param_str = f"--{revel_param.name} <value>"
                else:
                    param_str = revel_param.name

                if is_optional:
                    param_str = f"[[{param_str}]"

            params_str += f" {param_str}"

        print(f"[dim]Usage:[/] {sys.argv[0]} {cmd_instance.name}{params_str}")

        # Parameter descriptions
        if parsed_parameters:
            print()
            name_to_user_param = {
                param.name: param for param in cmd_instance.user_provided_parameters
            }

            align_len = max(len(params[1].name) for params in parsed_parameters)

            for inspect_param, revel_param in parsed_parameters:
                line = f"  [primary]{revel_param.name:<{align_len}}[/]"

                # Summary
                try:
                    user_param = name_to_user_param[inspect_param.name]
                except KeyError:
                    pass
                else:
                    if user_param.summary is not None:
                        line += f"  ...  {user_param.summary}"

                # Default value
                if isinstance(
                    revel_param.default_value, (bool, int, float, str, type(None))
                ):
                    line += f"  [dim](defaults to {revel_param.default_value})[/]"
                elif revel_param.default_value is not argument_parser.NO_DEFAULT:
                    line += f"  [dim](optional)[/]"

                print(line)

        # Details
        if cmd_instance.details is not None:
            print()
            print(cmd_instance.details)

    def _display_version(self) -> None:
        # TODO: Find the version
        name = "<TODO: Name>"
        version = "<TODO: Version>"

        # Display it
        print(f"{name} {version}")

    def command(
        self,
        *,
        name: str | None = None,
        aliases: Iterable[str] = [],
        summary: str | None = None,
        details: str | None = None,
        parameters: Iterable[Parameter] = [],
    ):
        """
        Register a function as a command, allowing users to call the function
        from the CLI. The function's name will be used as the command's name.
        """

        # Prepare the arguments
        if name is not None:
            name = name.strip()

        if summary is not None:
            summary = summary.strip()

        if details is not None:
            details = common.multiline_strip(details)

        parameters = list(parameters)

        # Create the decorator
        def result(func: Callable) -> Callable:
            # Parse all parameters this function has
            parsed_parameters = {
                params[0].name: params[0]
                for params in argument_parser.parameters_from_function(func)
            }

            # Make sure the user-provided parameters match the function's
            for uparam in parameters:
                if uparam.name not in parsed_parameters:
                    raise ValueError(
                        f"This function has no parameter named `{uparam.name}`"
                    )

            # Register the command
            self._commands.append(
                AppCommand(
                    name=(
                        common.python_name_to_console(func.__name__)
                        if name is None
                        else name
                    ),
                    aliases=set(aliases),
                    summary=summary,
                    details=details,
                    function=func,
                    user_provided_parameters=parameters,
                )
            )

            return func

        return result

    def run(self, args: Iterable[str] | None = None) -> None:
        if args is None:
            args = sys.argv[1:]
        else:
            args = list(args)

        # Which command should be run?
        #
        # TODO: What if there is only one command? Should it still have to be
        # specified?
        #
        # FIXME: This is imperfect, as it actually allows the user to specify
        # "exit" as a command, despite that obviously not being one.
        self._commands.sort(key=lambda cmd: cmd.name.lower())

        function_names = [cmd.name for cmd in self._commands] + ["Exit"]
        function_aliases = [cmd.aliases for cmd in self._commands] + [set()]
        function_summaries = [cmd.summary for cmd in self._commands] + [None]

        try:
            command_name, args = argument_parser.parse_function_name(
                function_names=function_names,
                function_aliases=function_aliases,
                function_summaries=function_summaries,
                raw_args=args,
                interactive=True,
            )

        # The user has cancelled the command
        except KeyboardInterrupt:
            print()
            print("[yellow]Canceled[/]")
            sys.exit(1)

        # The user has chosen to exit
        if command_name == "Exit":
            sys.exit(0)

        # Find the command instance
        for command in self._commands:
            if command.name == command_name:
                break
        else:
            assert False, "Unreachable"

        # Build the list of parameters for the command
        param_pairs = argument_parser.parameters_from_function(command.function)
        parser_params = [param[1] for param in param_pairs]

        for parser_param, user_param in zip(
            parser_params, command.user_provided_parameters
        ):
            parser_param.prompt = user_param.prompt

        # Parse & run the command. These can easily fail, so catch exceptions.
        try:
            # Parse the parameters for the command
            by_position_args, by_name_args = argument_parser.parse_function_parameters(
                parser_params,
                args,
                interactive=True,
            )

            # Call the command
            command.function(*by_position_args, **by_name_args)

        # The user has cancelled the command
        except KeyboardInterrupt:
            print()
            print("[yellow]Canceled[/]")
            sys.exit(1)

        # Invalid Arguments
        except ArgumentError as err:
            error(err.message)
            sys.exit(1)
