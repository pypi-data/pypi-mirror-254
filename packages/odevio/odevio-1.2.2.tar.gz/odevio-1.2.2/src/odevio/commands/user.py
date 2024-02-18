import click

from odevio.helpers import login_required_warning_decorator, terminal_menu


@click.command()
@click.option('--email', prompt=True)
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
def signup(email, password, username):
    """ Creates an Odevio user account.

    E-mail, username and password are required
    """
    from odevio import api
    from odevio.settings import console

    user = api.post('/register/', authorization=False, json_data={
        "email": email,
        "password": password,
        "username": username
    })

    if user:
        api.get_authorization_header(email, password)
        console.print(f"Welcome to Odevio [green underline]{user['username']}[/green underline]")
        # TODO add a reset password option on this command


@click.command()
@click.option('--email', prompt=True)
@click.option('--password', prompt=True, hide_input=True)
def signin(email, password):
    """ Logs in to your Odevio account.

    \f
    Login is based on e-mail and password. This command stores the connection token for future commands in
    a config.ini file. To get the location of the config.ini file run :option:`odevio profile --ini` once connected.
    """
    from odevio import api
    from odevio.settings import console

    # TODO verify that the user is not already signed in
    user = api.get("/my-account/", auth_data={
        "email": email,
        "password": password,
    })
    if user:
        console.print(f"Welcome back to Odevio [green underline]{user['username']}[/green underline]")
        # TODO add a reset password option on this command
        # TODO maybe show the profile output after the login


@click.command()
def signout():
    """ Log out of your Odevio account.

    \f
    This command deletes the connection token from the config.ini file associated with Odevio. To get the location of
    the config.ini file run :option:`odevio profile --ini`
    """
    from odevio import api
    api.disconnect()


@click.command()
@login_required_warning_decorator
@click.option('--ini', is_flag=True, help="Highlight config.ini path")
def profile(ini):
    """ Profile of the logged in user.

    \f
    Example output :

    .. image:: /img/odevio-profile.png
        :alt: example output of the odevio profile command
        :align: center

    The top part displays the user account information and the location of the Odevio config.ini file on your system.

    The bottom part either :

        * Displays the list of Teams to which the logged in user has access. The Admin field is shown in green if
          the logged in user is the admin of the team.
        * Is not shown if the logged in user has no teams or has not been added to any teams.

    Usage :

    """
    from rich.text import Text
    from rich.panel import Panel
    from rich.table import Table

    from odevio import api
    from odevio.settings import console, get_config_path

    user = api.get("/my-account/")
    teams = api.get("/teams/")

    if user:
        config_path = f"<[bold purple]{get_config_path()}[/bold purple]>" if ini else f"<{get_config_path()}>"
        console.print(Panel(Text.from_markup(
            f"""
            Username: [bold]{user["username"]}[/bold]
            E-mail: [bold]{user["email"]}[/bold]
            Account type: [bold]{user["type"]}[/bold]
            """
        ), title="User", subtitle=config_path))

        if len(teams) > 0:
            table_teams = Table(expand=True, title="Teams to which you have access")
            table_teams.add_column("Name")
            table_teams.add_column("Admin")
            for team in teams:
                admin = f"{team['manager']['username']} <[italic]{team['manager']['email']}[/italic]>"
                table_teams.add_row(team['name'], Text.from_markup(
                    f"[green bold]{admin}[/green bold]" if team["manager"]["username"] == user["username"] else admin))
            console.print(table_teams)

        # TODO add a change password option on this command
        # TODO add a reset password option on this command


@click.group()
def apikey():
    """ Manage your API keys.

    \f
    API keys are used to authenticate to the Odevio API with external programs.

    Usage:
    """
    pass


@apikey.command()
@login_required_warning_decorator
def ls():
    """
    List your API keys.

    \f
    Only the first 8 characters of the API key are shown. It is not possible to retrieve the full API key after it has been created.
    """
    from rich.table import Table

    from odevio import api
    from odevio.settings import console

    apikeys = api.get("/apikeys/")
    if len(apikeys) > 0:
        table_apikeys = Table(expand=True, title="API keys")
        table_apikeys.add_column("First 8 characters of the key")
        for apikey in apikeys:
            table_apikeys.add_row(apikey)
        console.print(table_apikeys)
    else:
        console.print("You have no API keys")


@apikey.command()
@login_required_warning_decorator
def new():
    """
    Create a new API key.

    \f
    The key will only be shown once so be sure to copy it.
    """
    from odevio import api
    from odevio.settings import console

    apikey = api.post("/apikeys/new")
    console.print(f"API key: [bold]{apikey['key']}[/bold]")
    console.print("This key will only be shown once so be sure to copy it.")


@apikey.command()
@login_required_warning_decorator
@click.argument('key', required=False)
def rm(key):
    """
    Delete an API key.

    \f
    You only need to provide the first 8 characters of the API key.
    """
    from odevio import api
    from odevio.settings import console

    if key is None:
        key = terminal_menu("/apikeys/", "Which key do you want to delete?", name=lambda apikey: apikey,
                            does_not_exist_msg="You have no API keys", key_fieldname=None)
        if key is None:
            return

    try:
        api.delete(f"/apikeys/{key}", json_decode=False)
        console.print(f"API key [bold]{key}[/bold] deleted")
    except api.NotFoundException:
        console.print("This key does not exist or isn't linked to your account.")
