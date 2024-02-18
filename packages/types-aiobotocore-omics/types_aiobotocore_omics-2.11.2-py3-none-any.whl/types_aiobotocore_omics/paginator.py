"""
Type annotations for omics service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_omics.client import OmicsClient
    from types_aiobotocore_omics.paginator import (
        ListAnnotationImportJobsPaginator,
        ListAnnotationStoreVersionsPaginator,
        ListAnnotationStoresPaginator,
        ListMultipartReadSetUploadsPaginator,
        ListReadSetActivationJobsPaginator,
        ListReadSetExportJobsPaginator,
        ListReadSetImportJobsPaginator,
        ListReadSetUploadPartsPaginator,
        ListReadSetsPaginator,
        ListReferenceImportJobsPaginator,
        ListReferenceStoresPaginator,
        ListReferencesPaginator,
        ListRunGroupsPaginator,
        ListRunTasksPaginator,
        ListRunsPaginator,
        ListSequenceStoresPaginator,
        ListSharesPaginator,
        ListVariantImportJobsPaginator,
        ListVariantStoresPaginator,
        ListWorkflowsPaginator,
    )

    session = get_session()
    with session.create_client("omics") as client:
        client: OmicsClient

        list_annotation_import_jobs_paginator: ListAnnotationImportJobsPaginator = client.get_paginator("list_annotation_import_jobs")
        list_annotation_store_versions_paginator: ListAnnotationStoreVersionsPaginator = client.get_paginator("list_annotation_store_versions")
        list_annotation_stores_paginator: ListAnnotationStoresPaginator = client.get_paginator("list_annotation_stores")
        list_multipart_read_set_uploads_paginator: ListMultipartReadSetUploadsPaginator = client.get_paginator("list_multipart_read_set_uploads")
        list_read_set_activation_jobs_paginator: ListReadSetActivationJobsPaginator = client.get_paginator("list_read_set_activation_jobs")
        list_read_set_export_jobs_paginator: ListReadSetExportJobsPaginator = client.get_paginator("list_read_set_export_jobs")
        list_read_set_import_jobs_paginator: ListReadSetImportJobsPaginator = client.get_paginator("list_read_set_import_jobs")
        list_read_set_upload_parts_paginator: ListReadSetUploadPartsPaginator = client.get_paginator("list_read_set_upload_parts")
        list_read_sets_paginator: ListReadSetsPaginator = client.get_paginator("list_read_sets")
        list_reference_import_jobs_paginator: ListReferenceImportJobsPaginator = client.get_paginator("list_reference_import_jobs")
        list_reference_stores_paginator: ListReferenceStoresPaginator = client.get_paginator("list_reference_stores")
        list_references_paginator: ListReferencesPaginator = client.get_paginator("list_references")
        list_run_groups_paginator: ListRunGroupsPaginator = client.get_paginator("list_run_groups")
        list_run_tasks_paginator: ListRunTasksPaginator = client.get_paginator("list_run_tasks")
        list_runs_paginator: ListRunsPaginator = client.get_paginator("list_runs")
        list_sequence_stores_paginator: ListSequenceStoresPaginator = client.get_paginator("list_sequence_stores")
        list_shares_paginator: ListSharesPaginator = client.get_paginator("list_shares")
        list_variant_import_jobs_paginator: ListVariantImportJobsPaginator = client.get_paginator("list_variant_import_jobs")
        list_variant_stores_paginator: ListVariantStoresPaginator = client.get_paginator("list_variant_stores")
        list_workflows_paginator: ListWorkflowsPaginator = client.get_paginator("list_workflows")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import (
    ReadSetPartSourceType,
    ResourceOwnerType,
    RunStatusType,
    TaskStatusType,
    WorkflowTypeType,
)
from .type_defs import (
    ActivateReadSetFilterTypeDef,
    ExportReadSetFilterTypeDef,
    FilterTypeDef,
    ImportReadSetFilterTypeDef,
    ImportReferenceFilterTypeDef,
    ListAnnotationImportJobsFilterTypeDef,
    ListAnnotationImportJobsResponseTypeDef,
    ListAnnotationStoresFilterTypeDef,
    ListAnnotationStoresResponseTypeDef,
    ListAnnotationStoreVersionsFilterTypeDef,
    ListAnnotationStoreVersionsResponseTypeDef,
    ListMultipartReadSetUploadsResponseTypeDef,
    ListReadSetActivationJobsResponseTypeDef,
    ListReadSetExportJobsResponseTypeDef,
    ListReadSetImportJobsResponseTypeDef,
    ListReadSetsResponseTypeDef,
    ListReadSetUploadPartsResponseTypeDef,
    ListReferenceImportJobsResponseTypeDef,
    ListReferencesResponseTypeDef,
    ListReferenceStoresResponseTypeDef,
    ListRunGroupsResponseTypeDef,
    ListRunsResponseTypeDef,
    ListRunTasksResponseTypeDef,
    ListSequenceStoresResponseTypeDef,
    ListSharesResponseTypeDef,
    ListVariantImportJobsFilterTypeDef,
    ListVariantImportJobsResponseTypeDef,
    ListVariantStoresFilterTypeDef,
    ListVariantStoresResponseTypeDef,
    ListWorkflowsResponseTypeDef,
    PaginatorConfigTypeDef,
    ReadSetFilterTypeDef,
    ReadSetUploadPartListFilterTypeDef,
    ReferenceFilterTypeDef,
    ReferenceStoreFilterTypeDef,
    SequenceStoreFilterTypeDef,
)

__all__ = (
    "ListAnnotationImportJobsPaginator",
    "ListAnnotationStoreVersionsPaginator",
    "ListAnnotationStoresPaginator",
    "ListMultipartReadSetUploadsPaginator",
    "ListReadSetActivationJobsPaginator",
    "ListReadSetExportJobsPaginator",
    "ListReadSetImportJobsPaginator",
    "ListReadSetUploadPartsPaginator",
    "ListReadSetsPaginator",
    "ListReferenceImportJobsPaginator",
    "ListReferenceStoresPaginator",
    "ListReferencesPaginator",
    "ListRunGroupsPaginator",
    "ListRunTasksPaginator",
    "ListRunsPaginator",
    "ListSequenceStoresPaginator",
    "ListSharesPaginator",
    "ListVariantImportJobsPaginator",
    "ListVariantStoresPaginator",
    "ListWorkflowsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListAnnotationImportJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListAnnotationImportJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listannotationimportjobspaginator)
    """

    def paginate(
        self,
        *,
        ids: Sequence[str] = ...,
        filter: ListAnnotationImportJobsFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAnnotationImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListAnnotationImportJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listannotationimportjobspaginator)
        """


class ListAnnotationStoreVersionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListAnnotationStoreVersions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listannotationstoreversionspaginator)
    """

    def paginate(
        self,
        *,
        name: str,
        filter: ListAnnotationStoreVersionsFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAnnotationStoreVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListAnnotationStoreVersions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listannotationstoreversionspaginator)
        """


class ListAnnotationStoresPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListAnnotationStores)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listannotationstorespaginator)
    """

    def paginate(
        self,
        *,
        ids: Sequence[str] = ...,
        filter: ListAnnotationStoresFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAnnotationStoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListAnnotationStores.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listannotationstorespaginator)
        """


class ListMultipartReadSetUploadsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListMultipartReadSetUploads)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listmultipartreadsetuploadspaginator)
    """

    def paginate(
        self, *, sequenceStoreId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListMultipartReadSetUploadsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListMultipartReadSetUploads.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listmultipartreadsetuploadspaginator)
        """


class ListReadSetActivationJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReadSetActivationJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreadsetactivationjobspaginator)
    """

    def paginate(
        self,
        *,
        sequenceStoreId: str,
        filter: ActivateReadSetFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListReadSetActivationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReadSetActivationJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreadsetactivationjobspaginator)
        """


class ListReadSetExportJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReadSetExportJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreadsetexportjobspaginator)
    """

    def paginate(
        self,
        *,
        sequenceStoreId: str,
        filter: ExportReadSetFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListReadSetExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReadSetExportJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreadsetexportjobspaginator)
        """


class ListReadSetImportJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReadSetImportJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreadsetimportjobspaginator)
    """

    def paginate(
        self,
        *,
        sequenceStoreId: str,
        filter: ImportReadSetFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListReadSetImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReadSetImportJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreadsetimportjobspaginator)
        """


class ListReadSetUploadPartsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReadSetUploadParts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreadsetuploadpartspaginator)
    """

    def paginate(
        self,
        *,
        sequenceStoreId: str,
        uploadId: str,
        partSource: ReadSetPartSourceType,
        filter: ReadSetUploadPartListFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListReadSetUploadPartsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReadSetUploadParts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreadsetuploadpartspaginator)
        """


class ListReadSetsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReadSets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreadsetspaginator)
    """

    def paginate(
        self,
        *,
        sequenceStoreId: str,
        filter: ReadSetFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListReadSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReadSets.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreadsetspaginator)
        """


class ListReferenceImportJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReferenceImportJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreferenceimportjobspaginator)
    """

    def paginate(
        self,
        *,
        referenceStoreId: str,
        filter: ImportReferenceFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListReferenceImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReferenceImportJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreferenceimportjobspaginator)
        """


class ListReferenceStoresPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReferenceStores)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreferencestorespaginator)
    """

    def paginate(
        self,
        *,
        filter: ReferenceStoreFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListReferenceStoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReferenceStores.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreferencestorespaginator)
        """


class ListReferencesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReferences)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreferencespaginator)
    """

    def paginate(
        self,
        *,
        referenceStoreId: str,
        filter: ReferenceFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListReferencesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListReferences.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listreferencespaginator)
        """


class ListRunGroupsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListRunGroups)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listrungroupspaginator)
    """

    def paginate(
        self, *, name: str = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListRunGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListRunGroups.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listrungroupspaginator)
        """


class ListRunTasksPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListRunTasks)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listruntaskspaginator)
    """

    def paginate(
        self,
        *,
        id: str,
        status: TaskStatusType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListRunTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListRunTasks.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listruntaskspaginator)
        """


class ListRunsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListRuns)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listrunspaginator)
    """

    def paginate(
        self,
        *,
        name: str = ...,
        runGroupId: str = ...,
        status: RunStatusType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListRuns.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listrunspaginator)
        """


class ListSequenceStoresPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListSequenceStores)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listsequencestorespaginator)
    """

    def paginate(
        self,
        *,
        filter: SequenceStoreFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListSequenceStoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListSequenceStores.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listsequencestorespaginator)
        """


class ListSharesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListShares)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listsharespaginator)
    """

    def paginate(
        self,
        *,
        resourceOwner: ResourceOwnerType,
        filter: FilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListSharesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListShares.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listsharespaginator)
        """


class ListVariantImportJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListVariantImportJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listvariantimportjobspaginator)
    """

    def paginate(
        self,
        *,
        ids: Sequence[str] = ...,
        filter: ListVariantImportJobsFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListVariantImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListVariantImportJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listvariantimportjobspaginator)
        """


class ListVariantStoresPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListVariantStores)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listvariantstorespaginator)
    """

    def paginate(
        self,
        *,
        ids: Sequence[str] = ...,
        filter: ListVariantStoresFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListVariantStoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListVariantStores.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listvariantstorespaginator)
        """


class ListWorkflowsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListWorkflows)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listworkflowspaginator)
    """

    def paginate(
        self,
        *,
        type: WorkflowTypeType = ...,
        name: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListWorkflowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/omics.html#Omics.Paginator.ListWorkflows.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_omics/paginators/#listworkflowspaginator)
        """
