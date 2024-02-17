import click


@click.group()
def auth_group():
    pass

@auth_group.command("authenticate")
def cli_authenticate():
    """Authenticate to the Hectiq Console."""
    from hectiq_console.functional import authenticate
    from hectiq_console import CONSOLE_APP_URL
    from pathlib import Path
    import requests
    import os
    import toml
    is_logged = authenticate()
    
    if is_logged:
        # Ask if the user wants to add a new key
        click.secho("You are already logged in.", fg="green")
        should_continue = click.prompt("Do you still want to continue and create a new API key?",
                                        default="y", 
                                        show_default=True, 
                                        type=click.Choice(["y", "n"]))
        if should_continue=="n":
            return
    
    email = click.prompt("Email address", type=str)
    password = click.prompt("Password", type=str, hide_input=True)
    try:
        import socket
        name = socket.gethostname()
    except:
        name = "[unknown hostname]"
    
    name = click.prompt("Alias for the API key:", type=str, default=name)

    # Get the organizations
    res = requests.post(f"{CONSOLE_APP_URL}/app/auth/login", 
                 json={"email": email, "password": password})
    if res.status_code!=200:
        click.echo("Authentication failed.")
        return
    
    user = res.json()
    if user.get("organizations") is None:
        click.echo("You are not part of any organization. Please contact your administrator.")
        return
    
    click.echo("Select an organization:")
    for i, org in enumerate(user.get("organizations")):
        click.echo(f"[{i}] - {org.get('name')}")
    index = click.prompt("Enter the index of the organization:", 
                 type=click.Choice([str(i) for i in range(len(user.get("organizations")))]))
    organization_slug = user.get("organizations")[int(index)]["slug"]

    res = requests.post(f"{CONSOLE_APP_URL}/app/auth/api-keys", 
                  json={"email": email, "password": password, "name": name, "organization": organization_slug})
    
    if res.status_code!=200:
        click.echo("Authentication failed.")
        return
    
    api_key = res.json()
    path = os.getenv("HECTIQ_CONSOLE_CREDENTIALS_FILE", 
                         os.path.join(Path.home(),".hectiq-console", "credentials.toml"))
    
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Save the key in .hectiq-console/credentials
    with open(path, "a") as f:
        # Dump as TOML
        data = {}
        data[organization_slug] = api_key
        toml.dump(data, f)


    click.echo(f"A new API key has been added to {path}.")
    click.secho("You are now logged in.", fg="green")