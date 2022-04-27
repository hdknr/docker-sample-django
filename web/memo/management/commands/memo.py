import djclick as click
from ... import models
from django.contrib.auth import get_user_model

User = get_user_model()


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.argument("text")
@click.option("--user_id", "-u", default=None)
@click.pass_context
def memo_create(ctx, text, user_id):
    user = user_id and User.objects.filter(id=user_id).first() or User.objects.first()
    models.Memo.objects.create(
        user=user,
        text=text,
    )
