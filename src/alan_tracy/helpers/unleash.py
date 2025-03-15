"""Unleash module providing access to an appropriately configured Unleash client."""

import UnleashClient
from dotenv import load_dotenv
import os

load_dotenv()


def get_unleash() -> UnleashClient.UnleashClient:
    """Initialise Unleash client for feature toggling.

    https://docs.getunleash.io/unleash-client-python/usage.html#using-unleashclient-with-gitlab

    The url is included as a parameter to allow for testing.
    For this to work with Gitlab the following settings are required:

    - `app_name=the environment that are set in Gitlab` (e.g. `development`, `production`)
    - `disable_metrics=True`
    - `disable_registration=True`
    """
    unleash_instance_id=os.getenv("UNLEASH_INSTANCE_ID", "default-alan-tracy")
    unleash_url=os.getenv("UNLEASH_URL", "default-alan-tracy")
    unleash_client = UnleashClient.UnleashClient(
        url=unleash_url,
        app_name="production",
        instance_id=unleash_instance_id,
        disable_metrics=True,  # Disable metrics to work with Gitlab
        disable_registration=True,  # Disable registration to work with Gitlab
    )
    unleash_client.initialize_client()
    return unleash_client


def toggle(
    feature_name: str,
    context: dict = None,
    unleash_client: UnleashClient.UnleashClient = get_unleash(),  # type: ignore
) -> bool:
    """Check if a feature toggle is enabled."""
    if context is None:
        context = {}
    toggle_enabled = unleash_client.is_enabled(feature_name, context)
    return bool(toggle_enabled)
