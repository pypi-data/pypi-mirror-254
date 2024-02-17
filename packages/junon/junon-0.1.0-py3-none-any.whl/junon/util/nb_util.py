import argparse
import io

# argparseのヘルプメッセージを文字列として取得する関数
def get_help_message(parser: argparse.ArgumentParser):
    with io.StringIO() as buf:
        parser.print_help(file=buf)
        return buf.getvalue()


def create_argument_parser(prog: str, line: str, description: str):
    arguments_parser = argparse.ArgumentParser(description=description, add_help=False, prog=prog)
    arguments_parser.add_argument('-h', '--help', action='store_true',
                                  help='このヘルプを表示する。')

    def get_arguments():
        arguments = arguments_parser.parse_args(line.split())
        if arguments.help:
            print(get_help_message(arguments_parser))
            return None
        else:
            return arguments

    arguments_parser.get_arguments = get_arguments
    return arguments_parser
