"""
Type annotations for amplifyuibuilder service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_amplifyuibuilder.client import AmplifyUIBuilderClient

    session = get_session()
    async with session.create_client("amplifyuibuilder") as client:
        client: AmplifyUIBuilderClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .paginator import (
    ExportComponentsPaginator,
    ExportFormsPaginator,
    ExportThemesPaginator,
    ListCodegenJobsPaginator,
    ListComponentsPaginator,
    ListFormsPaginator,
    ListThemesPaginator,
)
from .type_defs import (
    CreateComponentDataTypeDef,
    CreateComponentResponseTypeDef,
    CreateFormDataTypeDef,
    CreateFormResponseTypeDef,
    CreateThemeDataTypeDef,
    CreateThemeResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    ExchangeCodeForTokenRequestBodyTypeDef,
    ExchangeCodeForTokenResponseTypeDef,
    ExportComponentsResponseTypeDef,
    ExportFormsResponseTypeDef,
    ExportThemesResponseTypeDef,
    GetCodegenJobResponseTypeDef,
    GetComponentResponseTypeDef,
    GetFormResponseTypeDef,
    GetMetadataResponseTypeDef,
    GetThemeResponseTypeDef,
    ListCodegenJobsResponseTypeDef,
    ListComponentsResponseTypeDef,
    ListFormsResponseTypeDef,
    ListThemesResponseTypeDef,
    PutMetadataFlagBodyTypeDef,
    RefreshTokenRequestBodyTypeDef,
    RefreshTokenResponseTypeDef,
    StartCodegenJobDataTypeDef,
    StartCodegenJobResponseTypeDef,
    UpdateComponentDataTypeDef,
    UpdateComponentResponseTypeDef,
    UpdateFormDataTypeDef,
    UpdateFormResponseTypeDef,
    UpdateThemeDataTypeDef,
    UpdateThemeResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AmplifyUIBuilderClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    ResourceConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]


class AmplifyUIBuilderClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AmplifyUIBuilderClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#close)
        """

    async def create_component(
        self,
        *,
        appId: str,
        environmentName: str,
        componentToCreate: CreateComponentDataTypeDef,
        clientToken: str = ...,
    ) -> CreateComponentResponseTypeDef:
        """
        Creates a new component for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.create_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#create_component)
        """

    async def create_form(
        self,
        *,
        appId: str,
        environmentName: str,
        formToCreate: CreateFormDataTypeDef,
        clientToken: str = ...,
    ) -> CreateFormResponseTypeDef:
        """
        Creates a new form for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.create_form)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#create_form)
        """

    async def create_theme(
        self,
        *,
        appId: str,
        environmentName: str,
        themeToCreate: CreateThemeDataTypeDef,
        clientToken: str = ...,
    ) -> CreateThemeResponseTypeDef:
        """
        Creates a theme to apply to the components in an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.create_theme)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#create_theme)
        """

    async def delete_component(
        self, *, appId: str, environmentName: str, id: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a component from an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.delete_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#delete_component)
        """

    async def delete_form(
        self, *, appId: str, environmentName: str, id: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a form from an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.delete_form)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#delete_form)
        """

    async def delete_theme(
        self, *, appId: str, environmentName: str, id: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a theme from an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.delete_theme)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#delete_theme)
        """

    async def exchange_code_for_token(
        self, *, provider: Literal["figma"], request: ExchangeCodeForTokenRequestBodyTypeDef
    ) -> ExchangeCodeForTokenResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.exchange_code_for_token)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#exchange_code_for_token)
        """

    async def export_components(
        self, *, appId: str, environmentName: str, nextToken: str = ...
    ) -> ExportComponentsResponseTypeDef:
        """
        Exports component configurations to code that is ready to integrate into an
        Amplify
        app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.export_components)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#export_components)
        """

    async def export_forms(
        self, *, appId: str, environmentName: str, nextToken: str = ...
    ) -> ExportFormsResponseTypeDef:
        """
        Exports form configurations to code that is ready to integrate into an Amplify
        app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.export_forms)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#export_forms)
        """

    async def export_themes(
        self, *, appId: str, environmentName: str, nextToken: str = ...
    ) -> ExportThemesResponseTypeDef:
        """
        Exports theme configurations to code that is ready to integrate into an Amplify
        app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.export_themes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#export_themes)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#generate_presigned_url)
        """

    async def get_codegen_job(
        self, *, appId: str, environmentName: str, id: str
    ) -> GetCodegenJobResponseTypeDef:
        """
        Returns an existing code generation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.get_codegen_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#get_codegen_job)
        """

    async def get_component(
        self, *, appId: str, environmentName: str, id: str
    ) -> GetComponentResponseTypeDef:
        """
        Returns an existing component for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.get_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#get_component)
        """

    async def get_form(
        self, *, appId: str, environmentName: str, id: str
    ) -> GetFormResponseTypeDef:
        """
        Returns an existing form for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.get_form)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#get_form)
        """

    async def get_metadata(self, *, appId: str, environmentName: str) -> GetMetadataResponseTypeDef:
        """
        Returns existing metadata for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.get_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#get_metadata)
        """

    async def get_theme(
        self, *, appId: str, environmentName: str, id: str
    ) -> GetThemeResponseTypeDef:
        """
        Returns an existing theme for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.get_theme)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#get_theme)
        """

    async def list_codegen_jobs(
        self, *, appId: str, environmentName: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListCodegenJobsResponseTypeDef:
        """
        Retrieves a list of code generation jobs for a specified Amplify app and
        backend
        environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.list_codegen_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#list_codegen_jobs)
        """

    async def list_components(
        self, *, appId: str, environmentName: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListComponentsResponseTypeDef:
        """
        Retrieves a list of components for a specified Amplify app and backend
        environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.list_components)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#list_components)
        """

    async def list_forms(
        self, *, appId: str, environmentName: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListFormsResponseTypeDef:
        """
        Retrieves a list of forms for a specified Amplify app and backend environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.list_forms)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#list_forms)
        """

    async def list_themes(
        self, *, appId: str, environmentName: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListThemesResponseTypeDef:
        """
        Retrieves a list of themes for a specified Amplify app and backend environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.list_themes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#list_themes)
        """

    async def put_metadata_flag(
        self,
        *,
        appId: str,
        environmentName: str,
        featureName: str,
        body: PutMetadataFlagBodyTypeDef,
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stores the metadata information about a feature on a form.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.put_metadata_flag)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#put_metadata_flag)
        """

    async def refresh_token(
        self, *, provider: Literal["figma"], refreshTokenBody: RefreshTokenRequestBodyTypeDef
    ) -> RefreshTokenResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.refresh_token)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#refresh_token)
        """

    async def start_codegen_job(
        self,
        *,
        appId: str,
        environmentName: str,
        codegenJobToCreate: StartCodegenJobDataTypeDef,
        clientToken: str = ...,
    ) -> StartCodegenJobResponseTypeDef:
        """
        Starts a code generation job for a specified Amplify app and backend
        environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.start_codegen_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#start_codegen_job)
        """

    async def update_component(
        self,
        *,
        appId: str,
        environmentName: str,
        id: str,
        updatedComponent: UpdateComponentDataTypeDef,
        clientToken: str = ...,
    ) -> UpdateComponentResponseTypeDef:
        """
        Updates an existing component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.update_component)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#update_component)
        """

    async def update_form(
        self,
        *,
        appId: str,
        environmentName: str,
        id: str,
        updatedForm: UpdateFormDataTypeDef,
        clientToken: str = ...,
    ) -> UpdateFormResponseTypeDef:
        """
        Updates an existing form.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.update_form)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#update_form)
        """

    async def update_theme(
        self,
        *,
        appId: str,
        environmentName: str,
        id: str,
        updatedTheme: UpdateThemeDataTypeDef,
        clientToken: str = ...,
    ) -> UpdateThemeResponseTypeDef:
        """
        Updates an existing theme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.update_theme)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#update_theme)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["export_components"]
    ) -> ExportComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["export_forms"]) -> ExportFormsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["export_themes"]) -> ExportThemesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_codegen_jobs"]
    ) -> ListCodegenJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_components"]) -> ListComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_forms"]) -> ListFormsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_themes"]) -> ListThemesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/#get_paginator)
        """

    async def __aenter__(self) -> "AmplifyUIBuilderClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplifyuibuilder.html#AmplifyUIBuilder.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/client/)
        """
