"""
Type annotations for athena service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_athena.client import AthenaClient

    session = get_session()
    async with session.create_client("athena") as client:
        client: AthenaClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    CalculationExecutionStateType,
    DataCatalogTypeType,
    ExecutorStateType,
    SessionStateType,
    WorkGroupStateType,
)
from .paginator import (
    GetQueryResultsPaginator,
    ListDatabasesPaginator,
    ListDataCatalogsPaginator,
    ListNamedQueriesPaginator,
    ListQueryExecutionsPaginator,
    ListTableMetadataPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    BatchGetNamedQueryOutputTypeDef,
    BatchGetPreparedStatementOutputTypeDef,
    BatchGetQueryExecutionOutputTypeDef,
    CalculationConfigurationTypeDef,
    CapacityAssignmentTypeDef,
    CreateNamedQueryOutputTypeDef,
    CreateNotebookOutputTypeDef,
    CreatePresignedNotebookUrlResponseTypeDef,
    EngineConfigurationTypeDef,
    ExportNotebookOutputTypeDef,
    FilterDefinitionTypeDef,
    GetCalculationExecutionCodeResponseTypeDef,
    GetCalculationExecutionResponseTypeDef,
    GetCalculationExecutionStatusResponseTypeDef,
    GetCapacityAssignmentConfigurationOutputTypeDef,
    GetCapacityReservationOutputTypeDef,
    GetDatabaseOutputTypeDef,
    GetDataCatalogOutputTypeDef,
    GetNamedQueryOutputTypeDef,
    GetNotebookMetadataOutputTypeDef,
    GetPreparedStatementOutputTypeDef,
    GetQueryExecutionOutputTypeDef,
    GetQueryResultsOutputTypeDef,
    GetQueryRuntimeStatisticsOutputTypeDef,
    GetSessionResponseTypeDef,
    GetSessionStatusResponseTypeDef,
    GetTableMetadataOutputTypeDef,
    GetWorkGroupOutputTypeDef,
    ImportNotebookOutputTypeDef,
    ListApplicationDPUSizesOutputTypeDef,
    ListCalculationExecutionsResponseTypeDef,
    ListCapacityReservationsOutputTypeDef,
    ListDatabasesOutputTypeDef,
    ListDataCatalogsOutputTypeDef,
    ListEngineVersionsOutputTypeDef,
    ListExecutorsResponseTypeDef,
    ListNamedQueriesOutputTypeDef,
    ListNotebookMetadataOutputTypeDef,
    ListNotebookSessionsResponseTypeDef,
    ListPreparedStatementsOutputTypeDef,
    ListQueryExecutionsOutputTypeDef,
    ListSessionsResponseTypeDef,
    ListTableMetadataOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListWorkGroupsOutputTypeDef,
    QueryExecutionContextTypeDef,
    ResultConfigurationTypeDef,
    ResultReuseConfigurationTypeDef,
    StartCalculationExecutionResponseTypeDef,
    StartQueryExecutionOutputTypeDef,
    StartSessionResponseTypeDef,
    StopCalculationExecutionResponseTypeDef,
    TagTypeDef,
    TerminateSessionResponseTypeDef,
    WorkGroupConfigurationTypeDef,
    WorkGroupConfigurationUpdatesTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AthenaClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    MetadataException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    SessionAlreadyExistsException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class AthenaClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AthenaClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#exceptions)
        """

    async def batch_get_named_query(
        self, *, NamedQueryIds: Sequence[str]
    ) -> BatchGetNamedQueryOutputTypeDef:
        """
        Returns the details of a single named query or a list of up to 50 queries,
        which you provide as an array of query ID
        strings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.batch_get_named_query)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#batch_get_named_query)
        """

    async def batch_get_prepared_statement(
        self, *, PreparedStatementNames: Sequence[str], WorkGroup: str
    ) -> BatchGetPreparedStatementOutputTypeDef:
        """
        Returns the details of a single prepared statement or a list of up to 256
        prepared statements for the array of prepared statement names that you
        provide.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.batch_get_prepared_statement)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#batch_get_prepared_statement)
        """

    async def batch_get_query_execution(
        self, *, QueryExecutionIds: Sequence[str]
    ) -> BatchGetQueryExecutionOutputTypeDef:
        """
        Returns the details of a single query execution or a list of up to 50 query
        executions, which you provide as an array of query execution ID
        strings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.batch_get_query_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#batch_get_query_execution)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#can_paginate)
        """

    async def cancel_capacity_reservation(self, *, Name: str) -> Dict[str, Any]:
        """
        Cancels the capacity reservation with the specified name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.cancel_capacity_reservation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#cancel_capacity_reservation)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#close)
        """

    async def create_capacity_reservation(
        self, *, TargetDpus: int, Name: str, Tags: Sequence[TagTypeDef] = ...
    ) -> Dict[str, Any]:
        """
        Creates a capacity reservation with the specified name and number of requested
        data processing
        units.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.create_capacity_reservation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#create_capacity_reservation)
        """

    async def create_data_catalog(
        self,
        *,
        Name: str,
        Type: DataCatalogTypeType,
        Description: str = ...,
        Parameters: Mapping[str, str] = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> Dict[str, Any]:
        """
        Creates (registers) a data catalog with the specified name and properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.create_data_catalog)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#create_data_catalog)
        """

    async def create_named_query(
        self,
        *,
        Name: str,
        Database: str,
        QueryString: str,
        Description: str = ...,
        ClientRequestToken: str = ...,
        WorkGroup: str = ...,
    ) -> CreateNamedQueryOutputTypeDef:
        """
        Creates a named query in the specified workgroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.create_named_query)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#create_named_query)
        """

    async def create_notebook(
        self, *, WorkGroup: str, Name: str, ClientRequestToken: str = ...
    ) -> CreateNotebookOutputTypeDef:
        """
        Creates an empty `ipynb` file in the specified Apache Spark enabled workgroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.create_notebook)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#create_notebook)
        """

    async def create_prepared_statement(
        self, *, StatementName: str, WorkGroup: str, QueryStatement: str, Description: str = ...
    ) -> Dict[str, Any]:
        """
        Creates a prepared statement for use with SQL queries in Athena.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.create_prepared_statement)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#create_prepared_statement)
        """

    async def create_presigned_notebook_url(
        self, *, SessionId: str
    ) -> CreatePresignedNotebookUrlResponseTypeDef:
        """
        Gets an authentication token and the URL at which the notebook can be accessed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.create_presigned_notebook_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#create_presigned_notebook_url)
        """

    async def create_work_group(
        self,
        *,
        Name: str,
        Configuration: WorkGroupConfigurationTypeDef = ...,
        Description: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> Dict[str, Any]:
        """
        Creates a workgroup with the specified name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.create_work_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#create_work_group)
        """

    async def delete_capacity_reservation(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes a cancelled capacity reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.delete_capacity_reservation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#delete_capacity_reservation)
        """

    async def delete_data_catalog(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes a data catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.delete_data_catalog)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#delete_data_catalog)
        """

    async def delete_named_query(self, *, NamedQueryId: str) -> Dict[str, Any]:
        """
        Deletes the named query if you have access to the workgroup in which the query
        was
        saved.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.delete_named_query)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#delete_named_query)
        """

    async def delete_notebook(self, *, NotebookId: str) -> Dict[str, Any]:
        """
        Deletes the specified notebook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.delete_notebook)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#delete_notebook)
        """

    async def delete_prepared_statement(
        self, *, StatementName: str, WorkGroup: str
    ) -> Dict[str, Any]:
        """
        Deletes the prepared statement with the specified name from the specified
        workgroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.delete_prepared_statement)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#delete_prepared_statement)
        """

    async def delete_work_group(
        self, *, WorkGroup: str, RecursiveDeleteOption: bool = ...
    ) -> Dict[str, Any]:
        """
        Deletes the workgroup with the specified name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.delete_work_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#delete_work_group)
        """

    async def export_notebook(self, *, NotebookId: str) -> ExportNotebookOutputTypeDef:
        """
        Exports the specified notebook and its metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.export_notebook)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#export_notebook)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#generate_presigned_url)
        """

    async def get_calculation_execution(
        self, *, CalculationExecutionId: str
    ) -> GetCalculationExecutionResponseTypeDef:
        """
        Describes a previously submitted calculation execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_calculation_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_calculation_execution)
        """

    async def get_calculation_execution_code(
        self, *, CalculationExecutionId: str
    ) -> GetCalculationExecutionCodeResponseTypeDef:
        """
        Retrieves the unencrypted code that was executed for the calculation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_calculation_execution_code)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_calculation_execution_code)
        """

    async def get_calculation_execution_status(
        self, *, CalculationExecutionId: str
    ) -> GetCalculationExecutionStatusResponseTypeDef:
        """
        Gets the status of a current calculation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_calculation_execution_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_calculation_execution_status)
        """

    async def get_capacity_assignment_configuration(
        self, *, CapacityReservationName: str
    ) -> GetCapacityAssignmentConfigurationOutputTypeDef:
        """
        Gets the capacity assignment configuration for a capacity reservation, if one
        exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_capacity_assignment_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_capacity_assignment_configuration)
        """

    async def get_capacity_reservation(self, *, Name: str) -> GetCapacityReservationOutputTypeDef:
        """
        Returns information about the capacity reservation with the specified name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_capacity_reservation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_capacity_reservation)
        """

    async def get_data_catalog(
        self, *, Name: str, WorkGroup: str = ...
    ) -> GetDataCatalogOutputTypeDef:
        """
        Returns the specified data catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_data_catalog)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_data_catalog)
        """

    async def get_database(
        self, *, CatalogName: str, DatabaseName: str, WorkGroup: str = ...
    ) -> GetDatabaseOutputTypeDef:
        """
        Returns a database object for the specified database and data catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_database)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_database)
        """

    async def get_named_query(self, *, NamedQueryId: str) -> GetNamedQueryOutputTypeDef:
        """
        Returns information about a single query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_named_query)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_named_query)
        """

    async def get_notebook_metadata(self, *, NotebookId: str) -> GetNotebookMetadataOutputTypeDef:
        """
        Retrieves notebook metadata for the specified notebook ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_notebook_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_notebook_metadata)
        """

    async def get_prepared_statement(
        self, *, StatementName: str, WorkGroup: str
    ) -> GetPreparedStatementOutputTypeDef:
        """
        Retrieves the prepared statement with the specified name from the specified
        workgroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_prepared_statement)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_prepared_statement)
        """

    async def get_query_execution(self, *, QueryExecutionId: str) -> GetQueryExecutionOutputTypeDef:
        """
        Returns information about a single execution of a query if you have access to
        the workgroup in which the query
        ran.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_query_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_query_execution)
        """

    async def get_query_results(
        self, *, QueryExecutionId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> GetQueryResultsOutputTypeDef:
        """
        Streams the results of a single query execution specified by `QueryExecutionId`
        from the Athena query results location in Amazon
        S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_query_results)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_query_results)
        """

    async def get_query_runtime_statistics(
        self, *, QueryExecutionId: str
    ) -> GetQueryRuntimeStatisticsOutputTypeDef:
        """
        Returns query execution runtime statistics related to a single execution of a
        query if you have access to the workgroup in which the query
        ran.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_query_runtime_statistics)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_query_runtime_statistics)
        """

    async def get_session(self, *, SessionId: str) -> GetSessionResponseTypeDef:
        """
        Gets the full details of a previously created session, including the session
        status and
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_session)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_session)
        """

    async def get_session_status(self, *, SessionId: str) -> GetSessionStatusResponseTypeDef:
        """
        Gets the current status of a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_session_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_session_status)
        """

    async def get_table_metadata(
        self, *, CatalogName: str, DatabaseName: str, TableName: str, WorkGroup: str = ...
    ) -> GetTableMetadataOutputTypeDef:
        """
        Returns table metadata for the specified catalog, database, and table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_table_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_table_metadata)
        """

    async def get_work_group(self, *, WorkGroup: str) -> GetWorkGroupOutputTypeDef:
        """
        Returns information about the workgroup with the specified name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_work_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_work_group)
        """

    async def import_notebook(
        self,
        *,
        WorkGroup: str,
        Name: str,
        Type: Literal["IPYNB"],
        Payload: str = ...,
        NotebookS3LocationUri: str = ...,
        ClientRequestToken: str = ...,
    ) -> ImportNotebookOutputTypeDef:
        """
        Imports a single `ipynb` file to a Spark enabled workgroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.import_notebook)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#import_notebook)
        """

    async def list_application_dpu_sizes(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListApplicationDPUSizesOutputTypeDef:
        """
        Returns the supported DPU sizes for the supported application runtimes (for
        example, `Athena notebook version
        1`).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_application_dpu_sizes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_application_dpu_sizes)
        """

    async def list_calculation_executions(
        self,
        *,
        SessionId: str,
        StateFilter: CalculationExecutionStateType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListCalculationExecutionsResponseTypeDef:
        """
        Lists the calculations that have been submitted to a session in descending
        order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_calculation_executions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_calculation_executions)
        """

    async def list_capacity_reservations(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListCapacityReservationsOutputTypeDef:
        """
        Lists the capacity reservations for the current account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_capacity_reservations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_capacity_reservations)
        """

    async def list_data_catalogs(
        self, *, NextToken: str = ..., MaxResults: int = ..., WorkGroup: str = ...
    ) -> ListDataCatalogsOutputTypeDef:
        """
        Lists the data catalogs in the current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_data_catalogs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_data_catalogs)
        """

    async def list_databases(
        self, *, CatalogName: str, NextToken: str = ..., MaxResults: int = ..., WorkGroup: str = ...
    ) -> ListDatabasesOutputTypeDef:
        """
        Lists the databases in the specified data catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_databases)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_databases)
        """

    async def list_engine_versions(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListEngineVersionsOutputTypeDef:
        """
        Returns a list of engine versions that are available to choose from, including
        the Auto
        option.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_engine_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_engine_versions)
        """

    async def list_executors(
        self,
        *,
        SessionId: str,
        ExecutorStateFilter: ExecutorStateType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListExecutorsResponseTypeDef:
        """
        Lists, in descending order, the executors that joined a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_executors)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_executors)
        """

    async def list_named_queries(
        self, *, NextToken: str = ..., MaxResults: int = ..., WorkGroup: str = ...
    ) -> ListNamedQueriesOutputTypeDef:
        """
        Provides a list of available query IDs only for queries saved in the specified
        workgroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_named_queries)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_named_queries)
        """

    async def list_notebook_metadata(
        self,
        *,
        WorkGroup: str,
        Filters: FilterDefinitionTypeDef = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListNotebookMetadataOutputTypeDef:
        """
        Displays the notebook files for the specified workgroup in paginated format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_notebook_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_notebook_metadata)
        """

    async def list_notebook_sessions(
        self, *, NotebookId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListNotebookSessionsResponseTypeDef:
        """
        Lists, in descending order, the sessions that have been created in a notebook
        that are in an active state like `CREATING`, `CREATED`, `IDLE` or
        `BUSY`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_notebook_sessions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_notebook_sessions)
        """

    async def list_prepared_statements(
        self, *, WorkGroup: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListPreparedStatementsOutputTypeDef:
        """
        Lists the prepared statements in the specified workgroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_prepared_statements)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_prepared_statements)
        """

    async def list_query_executions(
        self, *, NextToken: str = ..., MaxResults: int = ..., WorkGroup: str = ...
    ) -> ListQueryExecutionsOutputTypeDef:
        """
        Provides a list of available query execution IDs for the queries in the
        specified
        workgroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_query_executions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_query_executions)
        """

    async def list_sessions(
        self,
        *,
        WorkGroup: str,
        StateFilter: SessionStateType = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListSessionsResponseTypeDef:
        """
        Lists the sessions in a workgroup that are in an active state like `CREATING`,
        `CREATED`, `IDLE`, or
        `BUSY`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_sessions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_sessions)
        """

    async def list_table_metadata(
        self,
        *,
        CatalogName: str,
        DatabaseName: str,
        Expression: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        WorkGroup: str = ...,
    ) -> ListTableMetadataOutputTypeDef:
        """
        Lists the metadata for the tables in the specified data catalog database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_table_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_table_metadata)
        """

    async def list_tags_for_resource(
        self, *, ResourceARN: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags associated with an Athena resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_tags_for_resource)
        """

    async def list_work_groups(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListWorkGroupsOutputTypeDef:
        """
        Lists available workgroups for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.list_work_groups)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#list_work_groups)
        """

    async def put_capacity_assignment_configuration(
        self,
        *,
        CapacityReservationName: str,
        CapacityAssignments: Sequence[CapacityAssignmentTypeDef],
    ) -> Dict[str, Any]:
        """
        Puts a new capacity assignment configuration for a specified capacity
        reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.put_capacity_assignment_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#put_capacity_assignment_configuration)
        """

    async def start_calculation_execution(
        self,
        *,
        SessionId: str,
        Description: str = ...,
        CalculationConfiguration: CalculationConfigurationTypeDef = ...,
        CodeBlock: str = ...,
        ClientRequestToken: str = ...,
    ) -> StartCalculationExecutionResponseTypeDef:
        """
        Submits calculations for execution within a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.start_calculation_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#start_calculation_execution)
        """

    async def start_query_execution(
        self,
        *,
        QueryString: str,
        ClientRequestToken: str = ...,
        QueryExecutionContext: QueryExecutionContextTypeDef = ...,
        ResultConfiguration: ResultConfigurationTypeDef = ...,
        WorkGroup: str = ...,
        ExecutionParameters: Sequence[str] = ...,
        ResultReuseConfiguration: ResultReuseConfigurationTypeDef = ...,
    ) -> StartQueryExecutionOutputTypeDef:
        """
        Runs the SQL query statements contained in the `Query`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.start_query_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#start_query_execution)
        """

    async def start_session(
        self,
        *,
        WorkGroup: str,
        EngineConfiguration: EngineConfigurationTypeDef,
        Description: str = ...,
        NotebookVersion: str = ...,
        SessionIdleTimeoutInMinutes: int = ...,
        ClientRequestToken: str = ...,
    ) -> StartSessionResponseTypeDef:
        """
        Creates a session for running calculations within a workgroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.start_session)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#start_session)
        """

    async def stop_calculation_execution(
        self, *, CalculationExecutionId: str
    ) -> StopCalculationExecutionResponseTypeDef:
        """
        Requests the cancellation of a calculation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.stop_calculation_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#stop_calculation_execution)
        """

    async def stop_query_execution(self, *, QueryExecutionId: str) -> Dict[str, Any]:
        """
        Stops a query execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.stop_query_execution)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#stop_query_execution)
        """

    async def tag_resource(self, *, ResourceARN: str, Tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more tags to an Athena resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#tag_resource)
        """

    async def terminate_session(self, *, SessionId: str) -> TerminateSessionResponseTypeDef:
        """
        Terminates an active session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.terminate_session)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#terminate_session)
        """

    async def untag_resource(self, *, ResourceARN: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from an Athena resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#untag_resource)
        """

    async def update_capacity_reservation(self, *, TargetDpus: int, Name: str) -> Dict[str, Any]:
        """
        Updates the number of requested data processing units for the capacity
        reservation with the specified
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.update_capacity_reservation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#update_capacity_reservation)
        """

    async def update_data_catalog(
        self,
        *,
        Name: str,
        Type: DataCatalogTypeType,
        Description: str = ...,
        Parameters: Mapping[str, str] = ...,
    ) -> Dict[str, Any]:
        """
        Updates the data catalog that has the specified name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.update_data_catalog)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#update_data_catalog)
        """

    async def update_named_query(
        self, *, NamedQueryId: str, Name: str, QueryString: str, Description: str = ...
    ) -> Dict[str, Any]:
        """
        Updates a  NamedQuery object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.update_named_query)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#update_named_query)
        """

    async def update_notebook(
        self,
        *,
        NotebookId: str,
        Payload: str,
        Type: Literal["IPYNB"],
        SessionId: str = ...,
        ClientRequestToken: str = ...,
    ) -> Dict[str, Any]:
        """
        Updates the contents of a Spark notebook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.update_notebook)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#update_notebook)
        """

    async def update_notebook_metadata(
        self, *, NotebookId: str, Name: str, ClientRequestToken: str = ...
    ) -> Dict[str, Any]:
        """
        Updates the metadata for a notebook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.update_notebook_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#update_notebook_metadata)
        """

    async def update_prepared_statement(
        self, *, StatementName: str, WorkGroup: str, QueryStatement: str, Description: str = ...
    ) -> Dict[str, Any]:
        """
        Updates a prepared statement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.update_prepared_statement)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#update_prepared_statement)
        """

    async def update_work_group(
        self,
        *,
        WorkGroup: str,
        Description: str = ...,
        ConfigurationUpdates: WorkGroupConfigurationUpdatesTypeDef = ...,
        State: WorkGroupStateType = ...,
    ) -> Dict[str, Any]:
        """
        Updates the workgroup with the specified name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.update_work_group)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#update_work_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_query_results"]
    ) -> GetQueryResultsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_catalogs"]
    ) -> ListDataCatalogsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_databases"]) -> ListDatabasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_named_queries"]
    ) -> ListNamedQueriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_query_executions"]
    ) -> ListQueryExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_table_metadata"]
    ) -> ListTableMetadataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/#get_paginator)
        """

    async def __aenter__(self) -> "AthenaClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html#Athena.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_athena/client/)
        """
