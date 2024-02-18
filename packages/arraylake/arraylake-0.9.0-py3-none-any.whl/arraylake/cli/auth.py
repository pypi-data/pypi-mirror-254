from typing import Optional, Union
from webbrowser import open_new

import typer
from rich.prompt import Prompt

from arraylake import config
from arraylake.api_utils import ArraylakeHttpClient
from arraylake.cli.utils import coro, error_console, print_logo, rich_console
from arraylake.token import AuthException, TokenHandler
from arraylake.types import ApiTokenInfo, UserInfo

auth = typer.Typer(help="Manage Arraylake authentication")


def _get_auth_handler(org: Optional[str] = None) -> TokenHandler:
    return TokenHandler(api_endpoint=config.get("service.uri"), hint=org or config.get("user.org", None))


async def _get_user() -> Union[ApiTokenInfo, UserInfo]:
    client = ArraylakeHttpClient(api_url=config.get("service.uri"))
    user = await client.get_user()
    return user


@auth.command()
@coro  # type: ignore
async def login(
    browser: bool = typer.Option(True, help="Whether to automatically open a browser window."),
    org: str = typer.Option(None, help="Org identifier for custom login provider"),
):
    """**Log in** to Arraylake

    This will automatically open a browser window. If **--no-browser** is specified, a link will be printed.

    **Examples**

    - Log in without automatically opening a browser window

        ```
        $ arraylake auth login --no-browser
        ```
    """
    print_logo()
    handler = _get_auth_handler(org)
    has_tokens = False

    if handler.tokens is not None:
        # try to refresh tokens if they are present but fail gracefully, the user is already expecting to log in
        try:
            await handler.refresh_token()
            has_tokens = True
        except Exception:
            pass

    if not has_tokens:
        url = await handler.get_authorize_url()
        if browser:
            open_new(url)
        else:
            docs_link = "https://docs.earthmover.io/arraylake/org_access#authenticating-as-a-user"

            rich_console.print("\n")
            rich_console.rule(":key: [bold]Authorize[/bold]", style="dim", align="left")
            rich_console.print(f"\n[dim]Copy and paste the following [link={url}]:link: link[/link] into your browser:[/dim]\n")
            rich_console.print(f"[blue]{url}[/blue]\n", soft_wrap=True)
            rich_console.print(
                f"[dim]:down_arrow: Then enter the code below. Visit [link={docs_link}]docs.earthmover.io[/link] for help.[/dim]"
            )
        code = Prompt.ask("\n:sunglasses: [bold]Enter your code[/bold]")

        await handler.get_token(code)

    user = await _get_user()
    rich_console.print(user.model_dump_json())
    rich_console.print(f"✅ Token stored at {handler.token_path}")


@auth.command()
@coro
async def refresh():
    """**Refresh** Arraylake's auth token"""
    print_logo()
    handler = _get_auth_handler()
    if handler.tokens is not None:
        await handler.refresh_token()
        user = await _get_user()  # checks that the new tokens are valid
        rich_console.print(user.model_dump_json())
        rich_console.print(f"✅ Token stored at {handler.token_path}")
    else:
        error_console.print("Not logged in, log in with `arraylake auth login`")
        raise typer.Exit(code=1)


@auth.command()
def logout(browser: bool = typer.Option(True, help="Whether to also remove the browsers auth cookie.")):
    """**Logout** of Arraylake

    **Examples**

    - Logout of arraylake

        ```
        $ arraylake auth logout
        ```
    """
    print_logo()
    handler = _get_auth_handler()
    try:
        url = handler.get_logout_url()
        if browser:
            open_new(url)
        else:
            rich_console.print(f"To completely log out, open this URL in your browser: {url}")
        handler.purge_cache()
        rich_console.print(f"✅ Token removed from {handler.token_path}")
    except FileNotFoundError:
        error_console.print("Not logged in")
        raise typer.Exit(code=1)


@auth.command()
@coro
async def status():
    """Verify and display information about your authentication **status**"""
    print_logo()

    rich_console.print(f"Arraylake API Endpoint: {config.get('service.uri')}")
    try:
        user = await _get_user()
        rich_console.print(f"  → logged in as {user.email}")
    except AuthException:
        error_console.print("Not logged in, log in with `arraylake auth login`")
        raise typer.Exit(code=1)


@auth.command()
def token():
    """Display your authentication **token**"""
    print_logo()
    handler = _get_auth_handler()
    if handler.tokens is None:
        error_console.print("Not logged in, log in with `arraylake auth login`")
        raise typer.Exit(code=1)
    try:
        rich_console.print(handler.tokens.id_token.get_secret_value())
    except (AuthException, AttributeError):
        error_console.print("Not logged in, log in with `arraylake auth login`")
        raise typer.Exit(code=1)
