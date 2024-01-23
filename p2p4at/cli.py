import click

cli = click.Group("p2p4at")


@cli.command("rendezvous")
def rendezvous():
    ...


@cli.command("server")
def server():
    ...
