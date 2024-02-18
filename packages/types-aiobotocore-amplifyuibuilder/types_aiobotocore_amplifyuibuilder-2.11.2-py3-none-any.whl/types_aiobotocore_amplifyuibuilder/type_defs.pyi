"""
Type annotations for amplifyuibuilder service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_amplifyuibuilder/type_defs/)

Usage::

    ```python
    from types_aiobotocore_amplifyuibuilder.type_defs import MutationActionSetStateParameterPaginatorTypeDef

    data: MutationActionSetStateParameterPaginatorTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence

from .literals import (
    CodegenGenericDataFieldDataTypeType,
    CodegenJobStatusType,
    FormActionTypeType,
    FormButtonsPositionType,
    FormDataSourceTypeType,
    GenericDataRelationshipTypeType,
    JSModuleType,
    JSScriptType,
    JSTargetType,
    LabelDecoratorType,
    SortDirectionType,
    StorageAccessLevelType,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "MutationActionSetStateParameterPaginatorTypeDef",
    "MutationActionSetStateParameterTypeDef",
    "GraphQLRenderConfigTypeDef",
    "CodegenDependencyTypeDef",
    "CodegenFeatureFlagsTypeDef",
    "CodegenGenericDataEnumTypeDef",
    "CodegenGenericDataRelationshipTypeTypeDef",
    "CodegenJobAssetTypeDef",
    "CodegenJobSummaryTypeDef",
    "ComponentBindingPropertiesValuePropertiesPaginatorTypeDef",
    "ComponentBindingPropertiesValuePropertiesTypeDef",
    "ComponentConditionPropertyTypeDef",
    "SortPropertyTypeDef",
    "ComponentVariantPaginatorTypeDef",
    "ComponentPropertyBindingPropertiesTypeDef",
    "FormBindingElementTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentVariantTypeDef",
    "ResponseMetadataTypeDef",
    "FormDataTypeConfigTypeDef",
    "CreateThemeDataTypeDef",
    "ThemeTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteFormRequestRequestTypeDef",
    "DeleteThemeRequestRequestTypeDef",
    "ExchangeCodeForTokenRequestBodyTypeDef",
    "PaginatorConfigTypeDef",
    "ExportComponentsRequestRequestTypeDef",
    "ExportFormsRequestRequestTypeDef",
    "ExportThemesRequestRequestTypeDef",
    "ThemePaginatorTypeDef",
    "FieldPositionTypeDef",
    "FieldValidationConfigurationPaginatorTypeDef",
    "FieldValidationConfigurationTypeDef",
    "FileUploaderFieldConfigPaginatorTypeDef",
    "FileUploaderFieldConfigTypeDef",
    "FormInputBindingPropertiesValuePropertiesTypeDef",
    "FormInputValuePropertyBindingPropertiesTypeDef",
    "FormStyleConfigTypeDef",
    "GetCodegenJobRequestRequestTypeDef",
    "GetComponentRequestRequestTypeDef",
    "GetFormRequestRequestTypeDef",
    "GetMetadataRequestRequestTypeDef",
    "GetThemeRequestRequestTypeDef",
    "ListCodegenJobsRequestRequestTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListFormsRequestRequestTypeDef",
    "ListThemesRequestRequestTypeDef",
    "ThemeSummaryTypeDef",
    "PredicatePaginatorTypeDef",
    "PredicateTypeDef",
    "PutMetadataFlagBodyTypeDef",
    "RefreshTokenRequestBodyTypeDef",
    "ThemeValuePaginatorTypeDef",
    "ThemeValueTypeDef",
    "ThemeValuesPaginatorTypeDef",
    "ThemeValuesTypeDef",
    "UpdateThemeDataTypeDef",
    "ValueMappingPaginatorTypeDef",
    "ValueMappingTypeDef",
    "ActionParametersPaginatorTypeDef",
    "ActionParametersTypeDef",
    "ApiConfigurationTypeDef",
    "CodegenGenericDataFieldTypeDef",
    "ComponentBindingPropertiesValuePaginatorTypeDef",
    "ComponentBindingPropertiesValueTypeDef",
    "ComponentDataConfigurationPaginatorTypeDef",
    "ComponentDataConfigurationTypeDef",
    "ComponentPropertyPaginatorTypeDef",
    "ComponentPropertyTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExchangeCodeForTokenResponseTypeDef",
    "GetMetadataResponseTypeDef",
    "ListCodegenJobsResponseTypeDef",
    "ListComponentsResponseTypeDef",
    "RefreshTokenResponseTypeDef",
    "FormSummaryTypeDef",
    "CreateThemeRequestRequestTypeDef",
    "CreateThemeResponseTypeDef",
    "ExportThemesResponseTypeDef",
    "GetThemeResponseTypeDef",
    "UpdateThemeResponseTypeDef",
    "ExchangeCodeForTokenRequestRequestTypeDef",
    "ExportComponentsRequestExportComponentsPaginateTypeDef",
    "ExportFormsRequestExportFormsPaginateTypeDef",
    "ExportThemesRequestExportThemesPaginateTypeDef",
    "ListCodegenJobsRequestListCodegenJobsPaginateTypeDef",
    "ListComponentsRequestListComponentsPaginateTypeDef",
    "ListFormsRequestListFormsPaginateTypeDef",
    "ListThemesRequestListThemesPaginateTypeDef",
    "ExportThemesResponsePaginatorTypeDef",
    "FormButtonTypeDef",
    "SectionalElementTypeDef",
    "FormInputBindingPropertiesValueTypeDef",
    "FormInputValuePropertyPaginatorTypeDef",
    "FormInputValuePropertyTypeDef",
    "FormStyleTypeDef",
    "ListThemesResponseTypeDef",
    "PutMetadataFlagRequestRequestTypeDef",
    "RefreshTokenRequestRequestTypeDef",
    "UpdateThemeRequestRequestTypeDef",
    "ComponentEventPaginatorTypeDef",
    "ComponentEventTypeDef",
    "ReactStartCodegenJobDataTypeDef",
    "CodegenGenericDataModelTypeDef",
    "CodegenGenericDataNonModelTypeDef",
    "ListFormsResponseTypeDef",
    "FormCTATypeDef",
    "ValueMappingsPaginatorTypeDef",
    "ValueMappingsTypeDef",
    "ComponentChildPaginatorTypeDef",
    "ComponentPaginatorTypeDef",
    "ComponentChildTypeDef",
    "ComponentTypeDef",
    "CreateComponentDataTypeDef",
    "UpdateComponentDataTypeDef",
    "CodegenJobRenderConfigTypeDef",
    "CodegenJobGenericDataSchemaTypeDef",
    "FieldInputConfigPaginatorTypeDef",
    "FieldInputConfigTypeDef",
    "ExportComponentsResponsePaginatorTypeDef",
    "CreateComponentResponseTypeDef",
    "ExportComponentsResponseTypeDef",
    "GetComponentResponseTypeDef",
    "UpdateComponentResponseTypeDef",
    "CreateComponentRequestRequestTypeDef",
    "UpdateComponentRequestRequestTypeDef",
    "CodegenJobTypeDef",
    "StartCodegenJobDataTypeDef",
    "FieldConfigPaginatorTypeDef",
    "FieldConfigTypeDef",
    "GetCodegenJobResponseTypeDef",
    "StartCodegenJobResponseTypeDef",
    "StartCodegenJobRequestRequestTypeDef",
    "FormPaginatorTypeDef",
    "CreateFormDataTypeDef",
    "FormTypeDef",
    "UpdateFormDataTypeDef",
    "ExportFormsResponsePaginatorTypeDef",
    "CreateFormRequestRequestTypeDef",
    "CreateFormResponseTypeDef",
    "ExportFormsResponseTypeDef",
    "GetFormResponseTypeDef",
    "UpdateFormResponseTypeDef",
    "UpdateFormRequestRequestTypeDef",
)

MutationActionSetStateParameterPaginatorTypeDef = TypedDict(
    "MutationActionSetStateParameterPaginatorTypeDef",
    {
        "componentName": str,
        "property": str,
        "set": "ComponentPropertyPaginatorTypeDef",
    },
)
MutationActionSetStateParameterTypeDef = TypedDict(
    "MutationActionSetStateParameterTypeDef",
    {
        "componentName": str,
        "property": str,
        "set": "ComponentPropertyTypeDef",
    },
)
GraphQLRenderConfigTypeDef = TypedDict(
    "GraphQLRenderConfigTypeDef",
    {
        "typesFilePath": str,
        "queriesFilePath": str,
        "mutationsFilePath": str,
        "subscriptionsFilePath": str,
        "fragmentsFilePath": str,
    },
)
CodegenDependencyTypeDef = TypedDict(
    "CodegenDependencyTypeDef",
    {
        "name": NotRequired[str],
        "supportedVersion": NotRequired[str],
        "isSemVer": NotRequired[bool],
        "reason": NotRequired[str],
    },
)
CodegenFeatureFlagsTypeDef = TypedDict(
    "CodegenFeatureFlagsTypeDef",
    {
        "isRelationshipSupported": NotRequired[bool],
        "isNonModelSupported": NotRequired[bool],
    },
)
CodegenGenericDataEnumTypeDef = TypedDict(
    "CodegenGenericDataEnumTypeDef",
    {
        "values": List[str],
    },
)
CodegenGenericDataRelationshipTypeTypeDef = TypedDict(
    "CodegenGenericDataRelationshipTypeTypeDef",
    {
        "type": GenericDataRelationshipTypeType,
        "relatedModelName": str,
        "relatedModelFields": NotRequired[List[str]],
        "canUnlinkAssociatedModel": NotRequired[bool],
        "relatedJoinFieldName": NotRequired[str],
        "relatedJoinTableName": NotRequired[str],
        "belongsToFieldOnRelatedModel": NotRequired[str],
        "associatedFields": NotRequired[List[str]],
        "isHasManyIndex": NotRequired[bool],
    },
)
CodegenJobAssetTypeDef = TypedDict(
    "CodegenJobAssetTypeDef",
    {
        "downloadUrl": NotRequired[str],
    },
)
CodegenJobSummaryTypeDef = TypedDict(
    "CodegenJobSummaryTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "createdAt": NotRequired[datetime],
        "modifiedAt": NotRequired[datetime],
    },
)
ComponentBindingPropertiesValuePropertiesPaginatorTypeDef = TypedDict(
    "ComponentBindingPropertiesValuePropertiesPaginatorTypeDef",
    {
        "model": NotRequired[str],
        "field": NotRequired[str],
        "predicates": NotRequired[List["PredicatePaginatorTypeDef"]],
        "userAttribute": NotRequired[str],
        "bucket": NotRequired[str],
        "key": NotRequired[str],
        "defaultValue": NotRequired[str],
        "slotName": NotRequired[str],
    },
)
ComponentBindingPropertiesValuePropertiesTypeDef = TypedDict(
    "ComponentBindingPropertiesValuePropertiesTypeDef",
    {
        "model": NotRequired[str],
        "field": NotRequired[str],
        "predicates": NotRequired[Sequence["PredicateTypeDef"]],
        "userAttribute": NotRequired[str],
        "bucket": NotRequired[str],
        "key": NotRequired[str],
        "defaultValue": NotRequired[str],
        "slotName": NotRequired[str],
    },
)
ComponentConditionPropertyTypeDef = TypedDict(
    "ComponentConditionPropertyTypeDef",
    {
        "property": NotRequired[str],
        "field": NotRequired[str],
        "operator": NotRequired[str],
        "operand": NotRequired[str],
        "then": NotRequired["ComponentPropertyTypeDef"],
        "else": NotRequired["ComponentPropertyTypeDef"],
        "operandType": NotRequired[str],
    },
)
SortPropertyTypeDef = TypedDict(
    "SortPropertyTypeDef",
    {
        "field": str,
        "direction": SortDirectionType,
    },
)
ComponentVariantPaginatorTypeDef = TypedDict(
    "ComponentVariantPaginatorTypeDef",
    {
        "variantValues": NotRequired[Dict[str, str]],
        "overrides": NotRequired[Dict[str, Dict[str, str]]],
    },
)
ComponentPropertyBindingPropertiesTypeDef = TypedDict(
    "ComponentPropertyBindingPropertiesTypeDef",
    {
        "property": str,
        "field": NotRequired[str],
    },
)
FormBindingElementTypeDef = TypedDict(
    "FormBindingElementTypeDef",
    {
        "element": str,
        "property": str,
    },
)
ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "componentType": str,
    },
)
ComponentVariantTypeDef = TypedDict(
    "ComponentVariantTypeDef",
    {
        "variantValues": NotRequired[Mapping[str, str]],
        "overrides": NotRequired[Mapping[str, Mapping[str, str]]],
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)
FormDataTypeConfigTypeDef = TypedDict(
    "FormDataTypeConfigTypeDef",
    {
        "dataSourceType": FormDataSourceTypeType,
        "dataTypeName": str,
    },
)
CreateThemeDataTypeDef = TypedDict(
    "CreateThemeDataTypeDef",
    {
        "name": str,
        "values": Sequence["ThemeValuesTypeDef"],
        "overrides": NotRequired[Sequence["ThemeValuesTypeDef"]],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ThemeTypeDef = TypedDict(
    "ThemeTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "createdAt": datetime,
        "values": List["ThemeValuesTypeDef"],
        "modifiedAt": NotRequired[datetime],
        "overrides": NotRequired[List["ThemeValuesTypeDef"]],
        "tags": NotRequired[Dict[str, str]],
    },
)
DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
DeleteFormRequestRequestTypeDef = TypedDict(
    "DeleteFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
DeleteThemeRequestRequestTypeDef = TypedDict(
    "DeleteThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
ExchangeCodeForTokenRequestBodyTypeDef = TypedDict(
    "ExchangeCodeForTokenRequestBodyTypeDef",
    {
        "code": str,
        "redirectUri": str,
        "clientId": NotRequired[str],
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
ExportComponentsRequestRequestTypeDef = TypedDict(
    "ExportComponentsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
    },
)
ExportFormsRequestRequestTypeDef = TypedDict(
    "ExportFormsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
    },
)
ExportThemesRequestRequestTypeDef = TypedDict(
    "ExportThemesRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
    },
)
ThemePaginatorTypeDef = TypedDict(
    "ThemePaginatorTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "createdAt": datetime,
        "values": List["ThemeValuesPaginatorTypeDef"],
        "modifiedAt": NotRequired[datetime],
        "overrides": NotRequired[List["ThemeValuesPaginatorTypeDef"]],
        "tags": NotRequired[Dict[str, str]],
    },
)
FieldPositionTypeDef = TypedDict(
    "FieldPositionTypeDef",
    {
        "fixed": NotRequired[Literal["first"]],
        "rightOf": NotRequired[str],
        "below": NotRequired[str],
    },
)
FieldValidationConfigurationPaginatorTypeDef = TypedDict(
    "FieldValidationConfigurationPaginatorTypeDef",
    {
        "type": str,
        "strValues": NotRequired[List[str]],
        "numValues": NotRequired[List[int]],
        "validationMessage": NotRequired[str],
    },
)
FieldValidationConfigurationTypeDef = TypedDict(
    "FieldValidationConfigurationTypeDef",
    {
        "type": str,
        "strValues": NotRequired[Sequence[str]],
        "numValues": NotRequired[Sequence[int]],
        "validationMessage": NotRequired[str],
    },
)
FileUploaderFieldConfigPaginatorTypeDef = TypedDict(
    "FileUploaderFieldConfigPaginatorTypeDef",
    {
        "accessLevel": StorageAccessLevelType,
        "acceptedFileTypes": List[str],
        "showThumbnails": NotRequired[bool],
        "isResumable": NotRequired[bool],
        "maxFileCount": NotRequired[int],
        "maxSize": NotRequired[int],
    },
)
FileUploaderFieldConfigTypeDef = TypedDict(
    "FileUploaderFieldConfigTypeDef",
    {
        "accessLevel": StorageAccessLevelType,
        "acceptedFileTypes": Sequence[str],
        "showThumbnails": NotRequired[bool],
        "isResumable": NotRequired[bool],
        "maxFileCount": NotRequired[int],
        "maxSize": NotRequired[int],
    },
)
FormInputBindingPropertiesValuePropertiesTypeDef = TypedDict(
    "FormInputBindingPropertiesValuePropertiesTypeDef",
    {
        "model": NotRequired[str],
    },
)
FormInputValuePropertyBindingPropertiesTypeDef = TypedDict(
    "FormInputValuePropertyBindingPropertiesTypeDef",
    {
        "property": str,
        "field": NotRequired[str],
    },
)
FormStyleConfigTypeDef = TypedDict(
    "FormStyleConfigTypeDef",
    {
        "tokenReference": NotRequired[str],
        "value": NotRequired[str],
    },
)
GetCodegenJobRequestRequestTypeDef = TypedDict(
    "GetCodegenJobRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
GetComponentRequestRequestTypeDef = TypedDict(
    "GetComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
GetFormRequestRequestTypeDef = TypedDict(
    "GetFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
GetMetadataRequestRequestTypeDef = TypedDict(
    "GetMetadataRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
GetThemeRequestRequestTypeDef = TypedDict(
    "GetThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
ListCodegenJobsRequestRequestTypeDef = TypedDict(
    "ListCodegenJobsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListComponentsRequestRequestTypeDef = TypedDict(
    "ListComponentsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListFormsRequestRequestTypeDef = TypedDict(
    "ListFormsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListThemesRequestRequestTypeDef = TypedDict(
    "ListThemesRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ThemeSummaryTypeDef = TypedDict(
    "ThemeSummaryTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
    },
)
PredicatePaginatorTypeDef = TypedDict(
    "PredicatePaginatorTypeDef",
    {
        "or": NotRequired[List[Dict[str, Any]]],
        "and": NotRequired[List[Dict[str, Any]]],
        "field": NotRequired[str],
        "operator": NotRequired[str],
        "operand": NotRequired[str],
        "operandType": NotRequired[str],
    },
)
PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {
        "or": NotRequired[Sequence[Dict[str, Any]]],
        "and": NotRequired[Sequence[Dict[str, Any]]],
        "field": NotRequired[str],
        "operator": NotRequired[str],
        "operand": NotRequired[str],
        "operandType": NotRequired[str],
    },
)
PutMetadataFlagBodyTypeDef = TypedDict(
    "PutMetadataFlagBodyTypeDef",
    {
        "newValue": str,
    },
)
RefreshTokenRequestBodyTypeDef = TypedDict(
    "RefreshTokenRequestBodyTypeDef",
    {
        "token": str,
        "clientId": NotRequired[str],
    },
)
ThemeValuePaginatorTypeDef = TypedDict(
    "ThemeValuePaginatorTypeDef",
    {
        "value": NotRequired[str],
        "children": NotRequired[List["ThemeValuesPaginatorTypeDef"]],
    },
)
ThemeValueTypeDef = TypedDict(
    "ThemeValueTypeDef",
    {
        "value": NotRequired[str],
        "children": NotRequired[Sequence["ThemeValuesTypeDef"]],
    },
)
ThemeValuesPaginatorTypeDef = TypedDict(
    "ThemeValuesPaginatorTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[Dict[str, Any]],
    },
)
ThemeValuesTypeDef = TypedDict(
    "ThemeValuesTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[Dict[str, Any]],
    },
)
UpdateThemeDataTypeDef = TypedDict(
    "UpdateThemeDataTypeDef",
    {
        "values": Sequence["ThemeValuesTypeDef"],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "overrides": NotRequired[Sequence["ThemeValuesTypeDef"]],
    },
)
ValueMappingPaginatorTypeDef = TypedDict(
    "ValueMappingPaginatorTypeDef",
    {
        "value": "FormInputValuePropertyPaginatorTypeDef",
        "displayValue": NotRequired["FormInputValuePropertyPaginatorTypeDef"],
    },
)
ValueMappingTypeDef = TypedDict(
    "ValueMappingTypeDef",
    {
        "value": "FormInputValuePropertyTypeDef",
        "displayValue": NotRequired["FormInputValuePropertyTypeDef"],
    },
)
ActionParametersPaginatorTypeDef = TypedDict(
    "ActionParametersPaginatorTypeDef",
    {
        "type": NotRequired["ComponentPropertyPaginatorTypeDef"],
        "url": NotRequired["ComponentPropertyPaginatorTypeDef"],
        "anchor": NotRequired["ComponentPropertyPaginatorTypeDef"],
        "target": NotRequired["ComponentPropertyPaginatorTypeDef"],
        "global": NotRequired["ComponentPropertyPaginatorTypeDef"],
        "model": NotRequired[str],
        "id": NotRequired["ComponentPropertyPaginatorTypeDef"],
        "fields": NotRequired[Dict[str, "ComponentPropertyPaginatorTypeDef"]],
        "state": NotRequired[MutationActionSetStateParameterPaginatorTypeDef],
    },
)
ActionParametersTypeDef = TypedDict(
    "ActionParametersTypeDef",
    {
        "type": NotRequired["ComponentPropertyTypeDef"],
        "url": NotRequired["ComponentPropertyTypeDef"],
        "anchor": NotRequired["ComponentPropertyTypeDef"],
        "target": NotRequired["ComponentPropertyTypeDef"],
        "global": NotRequired["ComponentPropertyTypeDef"],
        "model": NotRequired[str],
        "id": NotRequired["ComponentPropertyTypeDef"],
        "fields": NotRequired[Mapping[str, "ComponentPropertyTypeDef"]],
        "state": NotRequired[MutationActionSetStateParameterTypeDef],
    },
)
ApiConfigurationTypeDef = TypedDict(
    "ApiConfigurationTypeDef",
    {
        "graphQLConfig": NotRequired[GraphQLRenderConfigTypeDef],
        "dataStoreConfig": NotRequired[Dict[str, Any]],
        "noApiConfig": NotRequired[Dict[str, Any]],
    },
)
CodegenGenericDataFieldTypeDef = TypedDict(
    "CodegenGenericDataFieldTypeDef",
    {
        "dataType": CodegenGenericDataFieldDataTypeType,
        "dataTypeValue": str,
        "required": bool,
        "readOnly": bool,
        "isArray": bool,
        "relationship": NotRequired[CodegenGenericDataRelationshipTypeTypeDef],
    },
)
ComponentBindingPropertiesValuePaginatorTypeDef = TypedDict(
    "ComponentBindingPropertiesValuePaginatorTypeDef",
    {
        "type": NotRequired[str],
        "bindingProperties": NotRequired[ComponentBindingPropertiesValuePropertiesPaginatorTypeDef],
        "defaultValue": NotRequired[str],
    },
)
ComponentBindingPropertiesValueTypeDef = TypedDict(
    "ComponentBindingPropertiesValueTypeDef",
    {
        "type": NotRequired[str],
        "bindingProperties": NotRequired[ComponentBindingPropertiesValuePropertiesTypeDef],
        "defaultValue": NotRequired[str],
    },
)
ComponentDataConfigurationPaginatorTypeDef = TypedDict(
    "ComponentDataConfigurationPaginatorTypeDef",
    {
        "model": str,
        "sort": NotRequired[List[SortPropertyTypeDef]],
        "predicate": NotRequired["PredicatePaginatorTypeDef"],
        "identifiers": NotRequired[List[str]],
    },
)
ComponentDataConfigurationTypeDef = TypedDict(
    "ComponentDataConfigurationTypeDef",
    {
        "model": str,
        "sort": NotRequired[Sequence[SortPropertyTypeDef]],
        "predicate": NotRequired["PredicateTypeDef"],
        "identifiers": NotRequired[Sequence[str]],
    },
)
ComponentPropertyPaginatorTypeDef = TypedDict(
    "ComponentPropertyPaginatorTypeDef",
    {
        "value": NotRequired[str],
        "bindingProperties": NotRequired[ComponentPropertyBindingPropertiesTypeDef],
        "collectionBindingProperties": NotRequired[ComponentPropertyBindingPropertiesTypeDef],
        "defaultValue": NotRequired[str],
        "model": NotRequired[str],
        "bindings": NotRequired[Dict[str, FormBindingElementTypeDef]],
        "event": NotRequired[str],
        "userAttribute": NotRequired[str],
        "concat": NotRequired[List[Dict[str, Any]]],
        "condition": NotRequired[ComponentConditionPropertyTypeDef],
        "configured": NotRequired[bool],
        "type": NotRequired[str],
        "importedValue": NotRequired[str],
        "componentName": NotRequired[str],
        "property": NotRequired[str],
    },
)
ComponentPropertyTypeDef = TypedDict(
    "ComponentPropertyTypeDef",
    {
        "value": NotRequired[str],
        "bindingProperties": NotRequired[ComponentPropertyBindingPropertiesTypeDef],
        "collectionBindingProperties": NotRequired[ComponentPropertyBindingPropertiesTypeDef],
        "defaultValue": NotRequired[str],
        "model": NotRequired[str],
        "bindings": NotRequired[Mapping[str, FormBindingElementTypeDef]],
        "event": NotRequired[str],
        "userAttribute": NotRequired[str],
        "concat": NotRequired[Sequence[Dict[str, Any]]],
        "condition": NotRequired[Dict[str, Any]],
        "configured": NotRequired[bool],
        "type": NotRequired[str],
        "importedValue": NotRequired[str],
        "componentName": NotRequired[str],
        "property": NotRequired[str],
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExchangeCodeForTokenResponseTypeDef = TypedDict(
    "ExchangeCodeForTokenResponseTypeDef",
    {
        "accessToken": str,
        "expiresIn": int,
        "refreshToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMetadataResponseTypeDef = TypedDict(
    "GetMetadataResponseTypeDef",
    {
        "features": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCodegenJobsResponseTypeDef = TypedDict(
    "ListCodegenJobsResponseTypeDef",
    {
        "entities": List[CodegenJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "entities": List[ComponentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RefreshTokenResponseTypeDef = TypedDict(
    "RefreshTokenResponseTypeDef",
    {
        "accessToken": str,
        "expiresIn": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FormSummaryTypeDef = TypedDict(
    "FormSummaryTypeDef",
    {
        "appId": str,
        "dataType": FormDataTypeConfigTypeDef,
        "environmentName": str,
        "formActionType": FormActionTypeType,
        "id": str,
        "name": str,
    },
)
CreateThemeRequestRequestTypeDef = TypedDict(
    "CreateThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "themeToCreate": CreateThemeDataTypeDef,
        "clientToken": NotRequired[str],
    },
)
CreateThemeResponseTypeDef = TypedDict(
    "CreateThemeResponseTypeDef",
    {
        "entity": ThemeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportThemesResponseTypeDef = TypedDict(
    "ExportThemesResponseTypeDef",
    {
        "entities": List[ThemeTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetThemeResponseTypeDef = TypedDict(
    "GetThemeResponseTypeDef",
    {
        "theme": ThemeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateThemeResponseTypeDef = TypedDict(
    "UpdateThemeResponseTypeDef",
    {
        "entity": ThemeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExchangeCodeForTokenRequestRequestTypeDef = TypedDict(
    "ExchangeCodeForTokenRequestRequestTypeDef",
    {
        "provider": Literal["figma"],
        "request": ExchangeCodeForTokenRequestBodyTypeDef,
    },
)
ExportComponentsRequestExportComponentsPaginateTypeDef = TypedDict(
    "ExportComponentsRequestExportComponentsPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ExportFormsRequestExportFormsPaginateTypeDef = TypedDict(
    "ExportFormsRequestExportFormsPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ExportThemesRequestExportThemesPaginateTypeDef = TypedDict(
    "ExportThemesRequestExportThemesPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCodegenJobsRequestListCodegenJobsPaginateTypeDef = TypedDict(
    "ListCodegenJobsRequestListCodegenJobsPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListComponentsRequestListComponentsPaginateTypeDef = TypedDict(
    "ListComponentsRequestListComponentsPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListFormsRequestListFormsPaginateTypeDef = TypedDict(
    "ListFormsRequestListFormsPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListThemesRequestListThemesPaginateTypeDef = TypedDict(
    "ListThemesRequestListThemesPaginateTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ExportThemesResponsePaginatorTypeDef = TypedDict(
    "ExportThemesResponsePaginatorTypeDef",
    {
        "entities": List[ThemePaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FormButtonTypeDef = TypedDict(
    "FormButtonTypeDef",
    {
        "excluded": NotRequired[bool],
        "children": NotRequired[str],
        "position": NotRequired[FieldPositionTypeDef],
    },
)
SectionalElementTypeDef = TypedDict(
    "SectionalElementTypeDef",
    {
        "type": str,
        "position": NotRequired[FieldPositionTypeDef],
        "text": NotRequired[str],
        "level": NotRequired[int],
        "orientation": NotRequired[str],
        "excluded": NotRequired[bool],
    },
)
FormInputBindingPropertiesValueTypeDef = TypedDict(
    "FormInputBindingPropertiesValueTypeDef",
    {
        "type": NotRequired[str],
        "bindingProperties": NotRequired[FormInputBindingPropertiesValuePropertiesTypeDef],
    },
)
FormInputValuePropertyPaginatorTypeDef = TypedDict(
    "FormInputValuePropertyPaginatorTypeDef",
    {
        "value": NotRequired[str],
        "bindingProperties": NotRequired[FormInputValuePropertyBindingPropertiesTypeDef],
        "concat": NotRequired[List[Dict[str, Any]]],
    },
)
FormInputValuePropertyTypeDef = TypedDict(
    "FormInputValuePropertyTypeDef",
    {
        "value": NotRequired[str],
        "bindingProperties": NotRequired[FormInputValuePropertyBindingPropertiesTypeDef],
        "concat": NotRequired[Sequence[Dict[str, Any]]],
    },
)
FormStyleTypeDef = TypedDict(
    "FormStyleTypeDef",
    {
        "horizontalGap": NotRequired[FormStyleConfigTypeDef],
        "verticalGap": NotRequired[FormStyleConfigTypeDef],
        "outerPadding": NotRequired[FormStyleConfigTypeDef],
    },
)
ListThemesResponseTypeDef = TypedDict(
    "ListThemesResponseTypeDef",
    {
        "entities": List[ThemeSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutMetadataFlagRequestRequestTypeDef = TypedDict(
    "PutMetadataFlagRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "featureName": str,
        "body": PutMetadataFlagBodyTypeDef,
    },
)
RefreshTokenRequestRequestTypeDef = TypedDict(
    "RefreshTokenRequestRequestTypeDef",
    {
        "provider": Literal["figma"],
        "refreshTokenBody": RefreshTokenRequestBodyTypeDef,
    },
)
UpdateThemeRequestRequestTypeDef = TypedDict(
    "UpdateThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedTheme": UpdateThemeDataTypeDef,
        "clientToken": NotRequired[str],
    },
)
ComponentEventPaginatorTypeDef = TypedDict(
    "ComponentEventPaginatorTypeDef",
    {
        "action": NotRequired[str],
        "parameters": NotRequired[ActionParametersPaginatorTypeDef],
        "bindingEvent": NotRequired[str],
    },
)
ComponentEventTypeDef = TypedDict(
    "ComponentEventTypeDef",
    {
        "action": NotRequired[str],
        "parameters": NotRequired[ActionParametersTypeDef],
        "bindingEvent": NotRequired[str],
    },
)
ReactStartCodegenJobDataTypeDef = TypedDict(
    "ReactStartCodegenJobDataTypeDef",
    {
        "module": NotRequired[JSModuleType],
        "target": NotRequired[JSTargetType],
        "script": NotRequired[JSScriptType],
        "renderTypeDeclarations": NotRequired[bool],
        "inlineSourceMap": NotRequired[bool],
        "apiConfiguration": NotRequired[ApiConfigurationTypeDef],
        "dependencies": NotRequired[Dict[str, str]],
    },
)
CodegenGenericDataModelTypeDef = TypedDict(
    "CodegenGenericDataModelTypeDef",
    {
        "fields": Dict[str, CodegenGenericDataFieldTypeDef],
        "primaryKeys": List[str],
        "isJoinTable": NotRequired[bool],
    },
)
CodegenGenericDataNonModelTypeDef = TypedDict(
    "CodegenGenericDataNonModelTypeDef",
    {
        "fields": Dict[str, CodegenGenericDataFieldTypeDef],
    },
)
ListFormsResponseTypeDef = TypedDict(
    "ListFormsResponseTypeDef",
    {
        "entities": List[FormSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FormCTATypeDef = TypedDict(
    "FormCTATypeDef",
    {
        "position": NotRequired[FormButtonsPositionType],
        "clear": NotRequired[FormButtonTypeDef],
        "cancel": NotRequired[FormButtonTypeDef],
        "submit": NotRequired[FormButtonTypeDef],
    },
)
ValueMappingsPaginatorTypeDef = TypedDict(
    "ValueMappingsPaginatorTypeDef",
    {
        "values": List[ValueMappingPaginatorTypeDef],
        "bindingProperties": NotRequired[Dict[str, FormInputBindingPropertiesValueTypeDef]],
    },
)
ValueMappingsTypeDef = TypedDict(
    "ValueMappingsTypeDef",
    {
        "values": Sequence[ValueMappingTypeDef],
        "bindingProperties": NotRequired[Mapping[str, FormInputBindingPropertiesValueTypeDef]],
    },
)
ComponentChildPaginatorTypeDef = TypedDict(
    "ComponentChildPaginatorTypeDef",
    {
        "componentType": str,
        "name": str,
        "properties": Dict[str, "ComponentPropertyPaginatorTypeDef"],
        "children": NotRequired[List[Dict[str, Any]]],
        "events": NotRequired[Dict[str, ComponentEventPaginatorTypeDef]],
        "sourceId": NotRequired[str],
    },
)
ComponentPaginatorTypeDef = TypedDict(
    "ComponentPaginatorTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "componentType": str,
        "properties": Dict[str, "ComponentPropertyPaginatorTypeDef"],
        "variants": List[ComponentVariantPaginatorTypeDef],
        "overrides": Dict[str, Dict[str, str]],
        "bindingProperties": Dict[str, ComponentBindingPropertiesValuePaginatorTypeDef],
        "createdAt": datetime,
        "sourceId": NotRequired[str],
        "children": NotRequired[List["ComponentChildPaginatorTypeDef"]],
        "collectionProperties": NotRequired[Dict[str, ComponentDataConfigurationPaginatorTypeDef]],
        "modifiedAt": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "events": NotRequired[Dict[str, ComponentEventPaginatorTypeDef]],
        "schemaVersion": NotRequired[str],
    },
)
ComponentChildTypeDef = TypedDict(
    "ComponentChildTypeDef",
    {
        "componentType": str,
        "name": str,
        "properties": Mapping[str, "ComponentPropertyTypeDef"],
        "children": NotRequired[Sequence[Dict[str, Any]]],
        "events": NotRequired[Mapping[str, ComponentEventTypeDef]],
        "sourceId": NotRequired[str],
    },
)
ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "componentType": str,
        "properties": Dict[str, "ComponentPropertyTypeDef"],
        "variants": List[ComponentVariantTypeDef],
        "overrides": Dict[str, Dict[str, str]],
        "bindingProperties": Dict[str, ComponentBindingPropertiesValueTypeDef],
        "createdAt": datetime,
        "sourceId": NotRequired[str],
        "children": NotRequired[List["ComponentChildTypeDef"]],
        "collectionProperties": NotRequired[Dict[str, ComponentDataConfigurationTypeDef]],
        "modifiedAt": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "events": NotRequired[Dict[str, ComponentEventTypeDef]],
        "schemaVersion": NotRequired[str],
    },
)
CreateComponentDataTypeDef = TypedDict(
    "CreateComponentDataTypeDef",
    {
        "name": str,
        "componentType": str,
        "properties": Mapping[str, "ComponentPropertyTypeDef"],
        "variants": Sequence[ComponentVariantTypeDef],
        "overrides": Mapping[str, Mapping[str, str]],
        "bindingProperties": Mapping[str, ComponentBindingPropertiesValueTypeDef],
        "sourceId": NotRequired[str],
        "children": NotRequired[Sequence["ComponentChildTypeDef"]],
        "collectionProperties": NotRequired[Mapping[str, ComponentDataConfigurationTypeDef]],
        "tags": NotRequired[Mapping[str, str]],
        "events": NotRequired[Mapping[str, ComponentEventTypeDef]],
        "schemaVersion": NotRequired[str],
    },
)
UpdateComponentDataTypeDef = TypedDict(
    "UpdateComponentDataTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "sourceId": NotRequired[str],
        "componentType": NotRequired[str],
        "properties": NotRequired[Mapping[str, "ComponentPropertyTypeDef"]],
        "children": NotRequired[Sequence["ComponentChildTypeDef"]],
        "variants": NotRequired[Sequence[ComponentVariantTypeDef]],
        "overrides": NotRequired[Mapping[str, Mapping[str, str]]],
        "bindingProperties": NotRequired[Mapping[str, ComponentBindingPropertiesValueTypeDef]],
        "collectionProperties": NotRequired[Mapping[str, ComponentDataConfigurationTypeDef]],
        "events": NotRequired[Mapping[str, ComponentEventTypeDef]],
        "schemaVersion": NotRequired[str],
    },
)
CodegenJobRenderConfigTypeDef = TypedDict(
    "CodegenJobRenderConfigTypeDef",
    {
        "react": NotRequired[ReactStartCodegenJobDataTypeDef],
    },
)
CodegenJobGenericDataSchemaTypeDef = TypedDict(
    "CodegenJobGenericDataSchemaTypeDef",
    {
        "dataSourceType": Literal["DataStore"],
        "models": Dict[str, CodegenGenericDataModelTypeDef],
        "enums": Dict[str, CodegenGenericDataEnumTypeDef],
        "nonModels": Dict[str, CodegenGenericDataNonModelTypeDef],
    },
)
FieldInputConfigPaginatorTypeDef = TypedDict(
    "FieldInputConfigPaginatorTypeDef",
    {
        "type": str,
        "required": NotRequired[bool],
        "readOnly": NotRequired[bool],
        "placeholder": NotRequired[str],
        "defaultValue": NotRequired[str],
        "descriptiveText": NotRequired[str],
        "defaultChecked": NotRequired[bool],
        "defaultCountryCode": NotRequired[str],
        "valueMappings": NotRequired[ValueMappingsPaginatorTypeDef],
        "name": NotRequired[str],
        "minValue": NotRequired[float],
        "maxValue": NotRequired[float],
        "step": NotRequired[float],
        "value": NotRequired[str],
        "isArray": NotRequired[bool],
        "fileUploaderConfig": NotRequired[FileUploaderFieldConfigPaginatorTypeDef],
    },
)
FieldInputConfigTypeDef = TypedDict(
    "FieldInputConfigTypeDef",
    {
        "type": str,
        "required": NotRequired[bool],
        "readOnly": NotRequired[bool],
        "placeholder": NotRequired[str],
        "defaultValue": NotRequired[str],
        "descriptiveText": NotRequired[str],
        "defaultChecked": NotRequired[bool],
        "defaultCountryCode": NotRequired[str],
        "valueMappings": NotRequired[ValueMappingsTypeDef],
        "name": NotRequired[str],
        "minValue": NotRequired[float],
        "maxValue": NotRequired[float],
        "step": NotRequired[float],
        "value": NotRequired[str],
        "isArray": NotRequired[bool],
        "fileUploaderConfig": NotRequired[FileUploaderFieldConfigTypeDef],
    },
)
ExportComponentsResponsePaginatorTypeDef = TypedDict(
    "ExportComponentsResponsePaginatorTypeDef",
    {
        "entities": List[ComponentPaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateComponentResponseTypeDef = TypedDict(
    "CreateComponentResponseTypeDef",
    {
        "entity": ComponentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportComponentsResponseTypeDef = TypedDict(
    "ExportComponentsResponseTypeDef",
    {
        "entities": List[ComponentTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetComponentResponseTypeDef = TypedDict(
    "GetComponentResponseTypeDef",
    {
        "component": ComponentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateComponentResponseTypeDef = TypedDict(
    "UpdateComponentResponseTypeDef",
    {
        "entity": ComponentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateComponentRequestRequestTypeDef = TypedDict(
    "CreateComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "componentToCreate": CreateComponentDataTypeDef,
        "clientToken": NotRequired[str],
    },
)
UpdateComponentRequestRequestTypeDef = TypedDict(
    "UpdateComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedComponent": UpdateComponentDataTypeDef,
        "clientToken": NotRequired[str],
    },
)
CodegenJobTypeDef = TypedDict(
    "CodegenJobTypeDef",
    {
        "id": str,
        "appId": str,
        "environmentName": str,
        "renderConfig": NotRequired[CodegenJobRenderConfigTypeDef],
        "genericDataSchema": NotRequired[CodegenJobGenericDataSchemaTypeDef],
        "autoGenerateForms": NotRequired[bool],
        "features": NotRequired[CodegenFeatureFlagsTypeDef],
        "status": NotRequired[CodegenJobStatusType],
        "statusMessage": NotRequired[str],
        "asset": NotRequired[CodegenJobAssetTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "createdAt": NotRequired[datetime],
        "modifiedAt": NotRequired[datetime],
        "dependencies": NotRequired[List[CodegenDependencyTypeDef]],
    },
)
StartCodegenJobDataTypeDef = TypedDict(
    "StartCodegenJobDataTypeDef",
    {
        "renderConfig": CodegenJobRenderConfigTypeDef,
        "genericDataSchema": NotRequired[CodegenJobGenericDataSchemaTypeDef],
        "autoGenerateForms": NotRequired[bool],
        "features": NotRequired[CodegenFeatureFlagsTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
FieldConfigPaginatorTypeDef = TypedDict(
    "FieldConfigPaginatorTypeDef",
    {
        "label": NotRequired[str],
        "position": NotRequired[FieldPositionTypeDef],
        "excluded": NotRequired[bool],
        "inputType": NotRequired[FieldInputConfigPaginatorTypeDef],
        "validations": NotRequired[List[FieldValidationConfigurationPaginatorTypeDef]],
    },
)
FieldConfigTypeDef = TypedDict(
    "FieldConfigTypeDef",
    {
        "label": NotRequired[str],
        "position": NotRequired[FieldPositionTypeDef],
        "excluded": NotRequired[bool],
        "inputType": NotRequired[FieldInputConfigTypeDef],
        "validations": NotRequired[Sequence[FieldValidationConfigurationTypeDef]],
    },
)
GetCodegenJobResponseTypeDef = TypedDict(
    "GetCodegenJobResponseTypeDef",
    {
        "job": CodegenJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartCodegenJobResponseTypeDef = TypedDict(
    "StartCodegenJobResponseTypeDef",
    {
        "entity": CodegenJobTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartCodegenJobRequestRequestTypeDef = TypedDict(
    "StartCodegenJobRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "codegenJobToCreate": StartCodegenJobDataTypeDef,
        "clientToken": NotRequired[str],
    },
)
FormPaginatorTypeDef = TypedDict(
    "FormPaginatorTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "formActionType": FormActionTypeType,
        "style": FormStyleTypeDef,
        "dataType": FormDataTypeConfigTypeDef,
        "fields": Dict[str, FieldConfigPaginatorTypeDef],
        "sectionalElements": Dict[str, SectionalElementTypeDef],
        "schemaVersion": str,
        "tags": NotRequired[Dict[str, str]],
        "cta": NotRequired[FormCTATypeDef],
        "labelDecorator": NotRequired[LabelDecoratorType],
    },
)
CreateFormDataTypeDef = TypedDict(
    "CreateFormDataTypeDef",
    {
        "name": str,
        "dataType": FormDataTypeConfigTypeDef,
        "formActionType": FormActionTypeType,
        "fields": Mapping[str, FieldConfigTypeDef],
        "style": FormStyleTypeDef,
        "sectionalElements": Mapping[str, SectionalElementTypeDef],
        "schemaVersion": str,
        "cta": NotRequired[FormCTATypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "labelDecorator": NotRequired[LabelDecoratorType],
    },
)
FormTypeDef = TypedDict(
    "FormTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "formActionType": FormActionTypeType,
        "style": FormStyleTypeDef,
        "dataType": FormDataTypeConfigTypeDef,
        "fields": Dict[str, FieldConfigTypeDef],
        "sectionalElements": Dict[str, SectionalElementTypeDef],
        "schemaVersion": str,
        "tags": NotRequired[Dict[str, str]],
        "cta": NotRequired[FormCTATypeDef],
        "labelDecorator": NotRequired[LabelDecoratorType],
    },
)
UpdateFormDataTypeDef = TypedDict(
    "UpdateFormDataTypeDef",
    {
        "name": NotRequired[str],
        "dataType": NotRequired[FormDataTypeConfigTypeDef],
        "formActionType": NotRequired[FormActionTypeType],
        "fields": NotRequired[Mapping[str, FieldConfigTypeDef]],
        "style": NotRequired[FormStyleTypeDef],
        "sectionalElements": NotRequired[Mapping[str, SectionalElementTypeDef]],
        "schemaVersion": NotRequired[str],
        "cta": NotRequired[FormCTATypeDef],
        "labelDecorator": NotRequired[LabelDecoratorType],
    },
)
ExportFormsResponsePaginatorTypeDef = TypedDict(
    "ExportFormsResponsePaginatorTypeDef",
    {
        "entities": List[FormPaginatorTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFormRequestRequestTypeDef = TypedDict(
    "CreateFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "formToCreate": CreateFormDataTypeDef,
        "clientToken": NotRequired[str],
    },
)
CreateFormResponseTypeDef = TypedDict(
    "CreateFormResponseTypeDef",
    {
        "entity": FormTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportFormsResponseTypeDef = TypedDict(
    "ExportFormsResponseTypeDef",
    {
        "entities": List[FormTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFormResponseTypeDef = TypedDict(
    "GetFormResponseTypeDef",
    {
        "form": FormTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFormResponseTypeDef = TypedDict(
    "UpdateFormResponseTypeDef",
    {
        "entity": FormTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFormRequestRequestTypeDef = TypedDict(
    "UpdateFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedForm": UpdateFormDataTypeDef,
        "clientToken": NotRequired[str],
    },
)
