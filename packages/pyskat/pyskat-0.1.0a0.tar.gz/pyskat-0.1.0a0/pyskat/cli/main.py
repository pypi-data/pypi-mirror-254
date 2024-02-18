from pathlib import Path

import click

from ..backend import Backend

pass_backend = click.make_pass_decorator(Backend)


@click.group()
@click.pass_context
@click.option(
    "-f", "--database-file",
    type=click.Path(dir_okay=False, path_type=Path),
    default=Path("pyskat_db.json")
)
def main(ctx, database_file: Path):
    ctx.obj = Backend(database_file)
