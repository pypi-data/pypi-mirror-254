import sys
import click

from .auth import auth_group

def main():
    cli = click.CommandCollection(
        sources=[
            auth_group
        ]
    )
    # Standalone mode is False so that the errors can be caught by the runs
    cli(standalone_mode=False)
    sys.exit()

if __name__ == "__main__":
    main()
