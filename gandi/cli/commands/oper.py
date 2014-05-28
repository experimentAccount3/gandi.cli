
import click

from gandi.cli.core.cli import cli
from gandi.cli.core.conf import pass_gandi
from gandi.cli.core.utils import output_oper


@cli.command(name='opers')
@pass_gandi
def list(gandi):
    """List operations."""

    output_keys = ['id', 'type', 'step']

    options = {
        'step': ['BILL', 'WAIT', 'RUN'],
    }

    result = gandi.oper.list(options)
    for oper in result:
        gandi.echo('-' * 10)
        output_oper(gandi, oper, output_keys)

    return result


@cli.command(name='oper')
@click.argument('id', type=click.INT)
@pass_gandi
def info(gandi, id):
    """Display information about an operation."""

    output_keys = ['id', 'type', 'step']

    oper = gandi.oper.info(id)
    output_oper(gandi, oper, output_keys)

    return oper