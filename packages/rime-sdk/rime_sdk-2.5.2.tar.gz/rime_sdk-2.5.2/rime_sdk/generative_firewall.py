"""Library defining the interface to the generative firewall."""
import atexit
from typing import List, Optional

from urllib3.util import Retry

from rime_sdk.authenticator import Authenticator
from rime_sdk.client import RETRY_HTTP_STATUS
from rime_sdk.internal.rest_error_handler import RESTErrorHandler
from rime_sdk.swagger.swagger_client import (
    ApiClient,
    Configuration,
    FirewallApi,
    FirewallConfigurationApi,
    GenerativefirewallFirewallRuleConfig,
    GenerativefirewallIndividualRulesConfig,
    GenerativefirewallValidateRequest,
    ValidateRequestInput,
    ValidateRequestOutput,
)
from rime_sdk.swagger.swagger_client.models.rime_language import RimeLanguage

_DEFAULT_CHANNEL_TIMEOUT = 60.0


VALID_LANGUAGES = [
    RimeLanguage.EN,
    RimeLanguage.JA,
]


class GenerativeFirewall:
    """An interface to a Generative Firewall object.

    To initialize the GenerativeFirewall, provide the address of your RI firewall instance.

    Args:
        domain: str
            The base domain/address of the firewall.
        api_key: str
            The API key used to authenticate to the firewall.
        auth_token: str
            The Auth Token used to authenticate to backend services. Optional.
        channel_timeout: float
            The amount of time in seconds to wait for responses from the firewall.

    Example:
        .. code-block:: python

            firewall = GenerativeFirewall(
                "my_vpc.rime.com", "api-key")   # using api-key
            firewall = GenerativeFirewall("my_vpc.rime.com", auth-token="auth-token")
    """

    def __init__(
        self,
        domain: str,
        api_key: str = "",
        auth_token: str = "",
        channel_timeout: float = _DEFAULT_CHANNEL_TIMEOUT,
    ):
        """Create a new Client connected to the services available at `domain`."""
        configuration = Configuration()
        configuration.api_key["X-Firewall-Api-Key"] = api_key
        configuration.api_key["X-Firewall-Auth-Token"] = auth_token
        if domain.endswith("/"):
            domain = domain[:-1]
        if not domain.startswith("https://") and not domain.startswith("http://"):
            domain = "https://" + domain
        configuration.host = domain
        self._api_client = ApiClient(configuration)
        # Prevent race condition in pool.close() triggered by swagger generated code
        atexit.register(self._api_client.pool.close)
        # Sets the timeout and hardcoded retries parameter for the api client.
        self._api_client.rest_client.pool_manager.connection_pool_kw[
            "timeout"
        ] = channel_timeout
        self._api_client.rest_client.pool_manager.connection_pool_kw["retries"] = Retry(
            total=3, status_forcelist=RETRY_HTTP_STATUS
        )
        self._firewall_client = FirewallApi(self._api_client)
        self._configuration_client = FirewallConfigurationApi(self._api_client)

    def validate(
        self,
        user_input_text: Optional[str] = None,
        output_text: Optional[str] = None,
        contexts: Optional[List[str]] = None,
    ) -> dict:
        """Validate model input and/or output text.

        Args:
            user_input_text: Optional[str]
                The user input text to validate.
            output_text: Optional[str]
                The model output text to validate.
            contexts: Optional[List[str]]
                The context documents used as a model input. In a RAG application the
                contexts will be the documents loaded during the RAG Retrieval phase to
                augment the LLM's response.

        Returns:
            A dictionary of results keyed by validation type: "input_results" will contain all
            results for input rules, and "output_results" will contain all results for output rules.

        Raises:
            ValueError:
                If neither input nor output text is provided or when there was an error
                in the validation request to the firewall backend.

        Example:
            .. code-block:: python

                results = firewall.validate(
                    user_input_text="Hello!", output_text="Hi, how can I help you?"
                )
        """
        if user_input_text is None and output_text is None and contexts is None:
            raise ValueError(
                "Must provide either input text, output text, or context documents to validate."
            )

        body = GenerativefirewallValidateRequest(
            input=ValidateRequestInput(
                user_input_text=user_input_text, contexts=contexts
            ),
            output=ValidateRequestOutput(output_text=output_text),
        )
        with RESTErrorHandler():
            response = self._firewall_client.firewall_validate(body=body)
        return response.to_dict()

    def get_config(self) -> dict:
        """Get the configuration of the Firewall.

        Returns:
            dict:
                The firewall configuration.

        Example:
             .. code-block:: python

                config = firewall.get_config()
        """
        with RESTErrorHandler():
            response = (
                self._configuration_client.firewall_configuration_get_firewall_config()
            )
        if response.config is not None:
            return response.config.to_dict()
        else:
            return {}

    def get_effective_config(self) -> dict:
        """Get the effective configuration of the Firewall.

        Returns:
            dict:
                The firewall effective configuration.

        Example:
             .. code-block:: python

                config = firewall.get_effective_config()
        """
        with RESTErrorHandler():
            response = self._firewall_client.firewall_get_firewall_effective_config()
        return response.config.to_dict()

    def update_config(self, firewall_config: dict, overwrite: bool = False) -> dict:
        """Update the firewall configuration.

        The update is performed via a PATCH request by merging the provided
        `firewall_config` with the existing config, meaning that any fields not
        explicitly provided in `firewall_config` will not be overwritten.

        Args:
            firewall_config: dict
                A dictionary containing the firewall configuration components to update.
            overwrite: bool
                A flag determining whether the config should be overwritten with exactly
                the new config provided, as opposed to patching the existing config.
                Default is False.

        Returns:
            dict:
                The updated firewall configuration.

        Raises:
            ValueError:
                If `firewall_config` is empty or contains unexpected keys, or when there
                was an error in the update request to the firewall backend.

        Example:
             .. code-block:: python

                updated_config = firewall.update_config(firewall_config)
        """
        _config = firewall_config.copy()
        language = _config.pop("language", None)
        if language is not None and language not in VALID_LANGUAGES:
            raise ValueError(
                f"Provided language {language} is invalid, please choose one of the "
                f"following values {VALID_LANGUAGES}"
            )

        # In the PATCH case, if `individual_rules_config` is explicitly set to None,
        # all fields should be reset to defaults, but if it is not provided, we should
        # not update anything.
        if (
            not overwrite
            and "individual_rules_config" in _config
            and _config["individual_rules_config"] is None
        ):
            individual_rules_config: Optional[dict] = {
                key: None
                for key in GenerativefirewallIndividualRulesConfig.attribute_map
            }
            _config.pop("individual_rules_config")
        else:
            individual_rules_config = _config.pop("individual_rules_config", None)

        body = GenerativefirewallFirewallRuleConfig(
            individual_rules_config=individual_rules_config,
            selected_rules=_config.pop("selected_rules", None),
            language=language,
        )

        if _config:
            raise ValueError(
                f"Found unexpected keys in firewall_config: {list(_config.keys())}"
            )

        with RESTErrorHandler():
            if overwrite:
                response = (
                    # PUT request
                    self._configuration_client.firewall_configuration_configure_firewall2(
                        body
                    )
                )
            else:
                if all(val is None for val in body.to_dict().values()):
                    raise ValueError(
                        "Must provide a non-empty firewall_config to patch config."
                    )
                response = (
                    # PATCH request
                    self._configuration_client.firewall_configuration_configure_firewall(
                        body
                    )
                )

        return response.config.to_dict()

    def login(self, email: str, system_account: bool = False) -> None:
        """Login to obtain an auth token.

        Args:
            email: str
                The user's email address that is used to authenticate.

            system_account: bool
                This flag specifies whether it is for a system account token or not.

        Example:
             .. code-block:: python

                firewall.login("dev@robustintelligence.com", True)
        """
        authenticator = Authenticator()
        authenticator.auth(self._api_client.configuration.host, email, system_account)
        with open("./token.txt", "r+") as file1:
            self._api_client.configuration.api_key[
                "X-Firewall-Auth-Token"
            ] = file1.read()
