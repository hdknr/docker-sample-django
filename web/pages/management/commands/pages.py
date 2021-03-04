from django.utils import timezone
import socket
import djclick as click
import json
from pages.utils import open_fixture


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.argument("message")
@click.pass_context
def make_message(ctx, message):
    data = {
        "hostname": socket.gethostname(),
        "datetime": str(timezone.now()),
        "message": message,
    }
    output = open_fixture("message.json", "w")
    json.dump(data, output)
