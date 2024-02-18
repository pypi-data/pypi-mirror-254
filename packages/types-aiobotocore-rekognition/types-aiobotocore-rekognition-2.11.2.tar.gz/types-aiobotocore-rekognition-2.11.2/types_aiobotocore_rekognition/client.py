"""
Type annotations for rekognition service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_rekognition.client import RekognitionClient

    session = get_session()
    async with session.create_client("rekognition") as client:
        client: RekognitionClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    AttributeType,
    CelebrityRecognitionSortByType,
    ContentModerationAggregateByType,
    ContentModerationSortByType,
    CustomizationFeatureType,
    DatasetTypeType,
    DetectLabelsFeatureNameType,
    FaceAttributesType,
    FaceSearchSortByType,
    LabelDetectionAggregateByType,
    LabelDetectionSortByType,
    PersonTrackingSortByType,
    ProjectAutoUpdateType,
    QualityFilterType,
    SegmentTypeType,
    StreamProcessorParameterToDeleteType,
)
from .paginator import (
    DescribeProjectsPaginator,
    DescribeProjectVersionsPaginator,
    ListCollectionsPaginator,
    ListDatasetEntriesPaginator,
    ListDatasetLabelsPaginator,
    ListFacesPaginator,
    ListProjectPoliciesPaginator,
    ListStreamProcessorsPaginator,
    ListUsersPaginator,
)
from .type_defs import (
    AssociateFacesResponseTypeDef,
    CompareFacesResponseTypeDef,
    CopyProjectVersionResponseTypeDef,
    CreateCollectionResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateFaceLivenessSessionRequestSettingsTypeDef,
    CreateFaceLivenessSessionResponseTypeDef,
    CreateProjectResponseTypeDef,
    CreateProjectVersionResponseTypeDef,
    CreateStreamProcessorResponseTypeDef,
    CustomizationFeatureConfigTypeDef,
    DatasetChangesTypeDef,
    DatasetSourceTypeDef,
    DeleteCollectionResponseTypeDef,
    DeleteFacesResponseTypeDef,
    DeleteProjectResponseTypeDef,
    DeleteProjectVersionResponseTypeDef,
    DescribeCollectionResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeProjectsResponseTypeDef,
    DescribeProjectVersionsResponseTypeDef,
    DescribeStreamProcessorResponseTypeDef,
    DetectCustomLabelsResponseTypeDef,
    DetectFacesResponseTypeDef,
    DetectLabelsResponseTypeDef,
    DetectLabelsSettingsTypeDef,
    DetectModerationLabelsResponseTypeDef,
    DetectProtectiveEquipmentResponseTypeDef,
    DetectTextFiltersTypeDef,
    DetectTextResponseTypeDef,
    DisassociateFacesResponseTypeDef,
    DistributeDatasetTypeDef,
    GetCelebrityInfoResponseTypeDef,
    GetCelebrityRecognitionResponseTypeDef,
    GetContentModerationResponseTypeDef,
    GetFaceDetectionResponseTypeDef,
    GetFaceLivenessSessionResultsResponseTypeDef,
    GetFaceSearchResponseTypeDef,
    GetLabelDetectionResponseTypeDef,
    GetMediaAnalysisJobResponseTypeDef,
    GetPersonTrackingResponseTypeDef,
    GetSegmentDetectionResponseTypeDef,
    GetTextDetectionResponseTypeDef,
    HumanLoopConfigTypeDef,
    ImageTypeDef,
    IndexFacesResponseTypeDef,
    LabelDetectionSettingsTypeDef,
    ListCollectionsResponseTypeDef,
    ListDatasetEntriesResponseTypeDef,
    ListDatasetLabelsResponseTypeDef,
    ListFacesResponseTypeDef,
    ListMediaAnalysisJobsResponseTypeDef,
    ListProjectPoliciesResponseTypeDef,
    ListStreamProcessorsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsersResponseTypeDef,
    MediaAnalysisInputTypeDef,
    MediaAnalysisOperationsConfigTypeDef,
    MediaAnalysisOutputConfigTypeDef,
    NotificationChannelTypeDef,
    OutputConfigTypeDef,
    ProtectiveEquipmentSummarizationAttributesTypeDef,
    PutProjectPolicyResponseTypeDef,
    RecognizeCelebritiesResponseTypeDef,
    RegionOfInterestTypeDef,
    SearchFacesByImageResponseTypeDef,
    SearchFacesResponseTypeDef,
    SearchUsersByImageResponseTypeDef,
    SearchUsersResponseTypeDef,
    StartCelebrityRecognitionResponseTypeDef,
    StartContentModerationResponseTypeDef,
    StartFaceDetectionResponseTypeDef,
    StartFaceSearchResponseTypeDef,
    StartLabelDetectionResponseTypeDef,
    StartMediaAnalysisJobResponseTypeDef,
    StartPersonTrackingResponseTypeDef,
    StartProjectVersionResponseTypeDef,
    StartSegmentDetectionFiltersTypeDef,
    StartSegmentDetectionResponseTypeDef,
    StartStreamProcessorResponseTypeDef,
    StartTextDetectionFiltersTypeDef,
    StartTextDetectionResponseTypeDef,
    StopProjectVersionResponseTypeDef,
    StreamProcessingStartSelectorTypeDef,
    StreamProcessingStopSelectorTypeDef,
    StreamProcessorDataSharingPreferenceTypeDef,
    StreamProcessorInputTypeDef,
    StreamProcessorNotificationChannelTypeDef,
    StreamProcessorOutputTypeDef,
    StreamProcessorSettingsForUpdateTypeDef,
    StreamProcessorSettingsTypeDef,
    TestingDataTypeDef,
    TrainingDataTypeDef,
    VideoTypeDef,
)
from .waiter import ProjectVersionRunningWaiter, ProjectVersionTrainingCompletedWaiter

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("RekognitionClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    HumanLoopQuotaExceededException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    ImageTooLargeException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidImageFormatException: Type[BotocoreClientError]
    InvalidManifestException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidPolicyRevisionIdException: Type[BotocoreClientError]
    InvalidS3ObjectException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    ProvisionedThroughputExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceNotReadyException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    SessionNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    VideoTooLargeException: Type[BotocoreClientError]


class RekognitionClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RekognitionClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#exceptions)
        """

    async def associate_faces(
        self,
        *,
        CollectionId: str,
        UserId: str,
        FaceIds: Sequence[str],
        UserMatchThreshold: float = ...,
        ClientRequestToken: str = ...,
    ) -> AssociateFacesResponseTypeDef:
        """
        Associates one or more faces with an existing UserID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.associate_faces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#associate_faces)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#close)
        """

    async def compare_faces(
        self,
        *,
        SourceImage: ImageTypeDef,
        TargetImage: ImageTypeDef,
        SimilarityThreshold: float = ...,
        QualityFilter: QualityFilterType = ...,
    ) -> CompareFacesResponseTypeDef:
        """
        Compares a face in the *source* input image with each of the 100 largest faces
        detected in the *target* input
        image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.compare_faces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#compare_faces)
        """

    async def copy_project_version(
        self,
        *,
        SourceProjectArn: str,
        SourceProjectVersionArn: str,
        DestinationProjectArn: str,
        VersionName: str,
        OutputConfig: OutputConfigTypeDef,
        Tags: Mapping[str, str] = ...,
        KmsKeyId: str = ...,
    ) -> CopyProjectVersionResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.copy_project_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#copy_project_version)
        """

    async def create_collection(
        self, *, CollectionId: str, Tags: Mapping[str, str] = ...
    ) -> CreateCollectionResponseTypeDef:
        """
        Creates a collection in an AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.create_collection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#create_collection)
        """

    async def create_dataset(
        self,
        *,
        DatasetType: DatasetTypeType,
        ProjectArn: str,
        DatasetSource: DatasetSourceTypeDef = ...,
    ) -> CreateDatasetResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.create_dataset)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#create_dataset)
        """

    async def create_face_liveness_session(
        self,
        *,
        KmsKeyId: str = ...,
        Settings: CreateFaceLivenessSessionRequestSettingsTypeDef = ...,
        ClientRequestToken: str = ...,
    ) -> CreateFaceLivenessSessionResponseTypeDef:
        """
        This API operation initiates a Face Liveness session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.create_face_liveness_session)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#create_face_liveness_session)
        """

    async def create_project(
        self,
        *,
        ProjectName: str,
        Feature: CustomizationFeatureType = ...,
        AutoUpdate: ProjectAutoUpdateType = ...,
    ) -> CreateProjectResponseTypeDef:
        """
        Creates a new Amazon Rekognition project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.create_project)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#create_project)
        """

    async def create_project_version(
        self,
        *,
        ProjectArn: str,
        VersionName: str,
        OutputConfig: OutputConfigTypeDef,
        TrainingData: TrainingDataTypeDef = ...,
        TestingData: TestingDataTypeDef = ...,
        Tags: Mapping[str, str] = ...,
        KmsKeyId: str = ...,
        VersionDescription: str = ...,
        FeatureConfig: CustomizationFeatureConfigTypeDef = ...,
    ) -> CreateProjectVersionResponseTypeDef:
        """
        Creates a new version of Amazon Rekognition project (like a Custom Labels model
        or a custom adapter) and begins
        training.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.create_project_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#create_project_version)
        """

    async def create_stream_processor(
        self,
        *,
        Input: StreamProcessorInputTypeDef,
        Output: StreamProcessorOutputTypeDef,
        Name: str,
        Settings: StreamProcessorSettingsTypeDef,
        RoleArn: str,
        Tags: Mapping[str, str] = ...,
        NotificationChannel: StreamProcessorNotificationChannelTypeDef = ...,
        KmsKeyId: str = ...,
        RegionsOfInterest: Sequence[RegionOfInterestTypeDef] = ...,
        DataSharingPreference: StreamProcessorDataSharingPreferenceTypeDef = ...,
    ) -> CreateStreamProcessorResponseTypeDef:
        """
        Creates an Amazon Rekognition stream processor that you can use to detect and
        recognize faces or to detect labels in a streaming
        video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.create_stream_processor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#create_stream_processor)
        """

    async def create_user(
        self, *, CollectionId: str, UserId: str, ClientRequestToken: str = ...
    ) -> Dict[str, Any]:
        """
        Creates a new User within a collection specified by `CollectionId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.create_user)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#create_user)
        """

    async def delete_collection(self, *, CollectionId: str) -> DeleteCollectionResponseTypeDef:
        """
        Deletes the specified collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.delete_collection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#delete_collection)
        """

    async def delete_dataset(self, *, DatasetArn: str) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.delete_dataset)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#delete_dataset)
        """

    async def delete_faces(
        self, *, CollectionId: str, FaceIds: Sequence[str]
    ) -> DeleteFacesResponseTypeDef:
        """
        Deletes faces from a collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.delete_faces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#delete_faces)
        """

    async def delete_project(self, *, ProjectArn: str) -> DeleteProjectResponseTypeDef:
        """
        Deletes a Amazon Rekognition project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.delete_project)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#delete_project)
        """

    async def delete_project_policy(
        self, *, ProjectArn: str, PolicyName: str, PolicyRevisionId: str = ...
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.delete_project_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#delete_project_policy)
        """

    async def delete_project_version(
        self, *, ProjectVersionArn: str
    ) -> DeleteProjectVersionResponseTypeDef:
        """
        Deletes a Rekognition project model or project version, like a Amazon
        Rekognition Custom Labels model or a custom
        adapter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.delete_project_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#delete_project_version)
        """

    async def delete_stream_processor(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes the stream processor identified by `Name`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.delete_stream_processor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#delete_stream_processor)
        """

    async def delete_user(
        self, *, CollectionId: str, UserId: str, ClientRequestToken: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes the specified UserID within the collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.delete_user)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#delete_user)
        """

    async def describe_collection(self, *, CollectionId: str) -> DescribeCollectionResponseTypeDef:
        """
        Describes the specified collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.describe_collection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#describe_collection)
        """

    async def describe_dataset(self, *, DatasetArn: str) -> DescribeDatasetResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.describe_dataset)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#describe_dataset)
        """

    async def describe_project_versions(
        self,
        *,
        ProjectArn: str,
        VersionNames: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> DescribeProjectVersionsResponseTypeDef:
        """
        Lists and describes the versions of an Amazon Rekognition project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.describe_project_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#describe_project_versions)
        """

    async def describe_projects(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        ProjectNames: Sequence[str] = ...,
        Features: Sequence[CustomizationFeatureType] = ...,
    ) -> DescribeProjectsResponseTypeDef:
        """
        Gets information about your Rekognition projects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.describe_projects)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#describe_projects)
        """

    async def describe_stream_processor(
        self, *, Name: str
    ) -> DescribeStreamProcessorResponseTypeDef:
        """
        Provides information about a stream processor created by  CreateStreamProcessor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.describe_stream_processor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#describe_stream_processor)
        """

    async def detect_custom_labels(
        self,
        *,
        ProjectVersionArn: str,
        Image: ImageTypeDef,
        MaxResults: int = ...,
        MinConfidence: float = ...,
    ) -> DetectCustomLabelsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_custom_labels)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#detect_custom_labels)
        """

    async def detect_faces(
        self, *, Image: ImageTypeDef, Attributes: Sequence[AttributeType] = ...
    ) -> DetectFacesResponseTypeDef:
        """
        Detects faces within an image that is provided as input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_faces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#detect_faces)
        """

    async def detect_labels(
        self,
        *,
        Image: ImageTypeDef,
        MaxLabels: int = ...,
        MinConfidence: float = ...,
        Features: Sequence[DetectLabelsFeatureNameType] = ...,
        Settings: DetectLabelsSettingsTypeDef = ...,
    ) -> DetectLabelsResponseTypeDef:
        """
        Detects instances of real-world entities within an image (JPEG or PNG) provided
        as
        input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_labels)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#detect_labels)
        """

    async def detect_moderation_labels(
        self,
        *,
        Image: ImageTypeDef,
        MinConfidence: float = ...,
        HumanLoopConfig: HumanLoopConfigTypeDef = ...,
        ProjectVersion: str = ...,
    ) -> DetectModerationLabelsResponseTypeDef:
        """
        Detects unsafe content in a specified JPEG or PNG format image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_moderation_labels)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#detect_moderation_labels)
        """

    async def detect_protective_equipment(
        self,
        *,
        Image: ImageTypeDef,
        SummarizationAttributes: ProtectiveEquipmentSummarizationAttributesTypeDef = ...,
    ) -> DetectProtectiveEquipmentResponseTypeDef:
        """
        Detects Personal Protective Equipment (PPE) worn by people detected in an image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_protective_equipment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#detect_protective_equipment)
        """

    async def detect_text(
        self, *, Image: ImageTypeDef, Filters: DetectTextFiltersTypeDef = ...
    ) -> DetectTextResponseTypeDef:
        """
        Detects text in the input image and converts it into machine-readable text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_text)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#detect_text)
        """

    async def disassociate_faces(
        self,
        *,
        CollectionId: str,
        UserId: str,
        FaceIds: Sequence[str],
        ClientRequestToken: str = ...,
    ) -> DisassociateFacesResponseTypeDef:
        """
        Removes the association between a `Face` supplied in an array of `FaceIds` and
        the
        User.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.disassociate_faces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#disassociate_faces)
        """

    async def distribute_dataset_entries(
        self, *, Datasets: Sequence[DistributeDatasetTypeDef]
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.distribute_dataset_entries)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#distribute_dataset_entries)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#generate_presigned_url)
        """

    async def get_celebrity_info(self, *, Id: str) -> GetCelebrityInfoResponseTypeDef:
        """
        Gets the name and additional information about a celebrity based on their
        Amazon Rekognition
        ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_celebrity_info)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_celebrity_info)
        """

    async def get_celebrity_recognition(
        self,
        *,
        JobId: str,
        MaxResults: int = ...,
        NextToken: str = ...,
        SortBy: CelebrityRecognitionSortByType = ...,
    ) -> GetCelebrityRecognitionResponseTypeDef:
        """
        Gets the celebrity recognition results for a Amazon Rekognition Video analysis
        started by
        StartCelebrityRecognition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_celebrity_recognition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_celebrity_recognition)
        """

    async def get_content_moderation(
        self,
        *,
        JobId: str,
        MaxResults: int = ...,
        NextToken: str = ...,
        SortBy: ContentModerationSortByType = ...,
        AggregateBy: ContentModerationAggregateByType = ...,
    ) -> GetContentModerationResponseTypeDef:
        """
        Gets the inappropriate, unwanted, or offensive content analysis results for a
        Amazon Rekognition Video analysis started by
        StartContentModeration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_content_moderation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_content_moderation)
        """

    async def get_face_detection(
        self, *, JobId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> GetFaceDetectionResponseTypeDef:
        """
        Gets face detection results for a Amazon Rekognition Video analysis started by
        StartFaceDetection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_face_detection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_face_detection)
        """

    async def get_face_liveness_session_results(
        self, *, SessionId: str
    ) -> GetFaceLivenessSessionResultsResponseTypeDef:
        """
        Retrieves the results of a specific Face Liveness session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_face_liveness_session_results)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_face_liveness_session_results)
        """

    async def get_face_search(
        self,
        *,
        JobId: str,
        MaxResults: int = ...,
        NextToken: str = ...,
        SortBy: FaceSearchSortByType = ...,
    ) -> GetFaceSearchResponseTypeDef:
        """
        Gets the face search results for Amazon Rekognition Video face search started
        by
        StartFaceSearch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_face_search)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_face_search)
        """

    async def get_label_detection(
        self,
        *,
        JobId: str,
        MaxResults: int = ...,
        NextToken: str = ...,
        SortBy: LabelDetectionSortByType = ...,
        AggregateBy: LabelDetectionAggregateByType = ...,
    ) -> GetLabelDetectionResponseTypeDef:
        """
        Gets the label detection results of a Amazon Rekognition Video analysis started
        by
        StartLabelDetection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_label_detection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_label_detection)
        """

    async def get_media_analysis_job(self, *, JobId: str) -> GetMediaAnalysisJobResponseTypeDef:
        """
        Retrieves the results for a given media analysis job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_media_analysis_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_media_analysis_job)
        """

    async def get_person_tracking(
        self,
        *,
        JobId: str,
        MaxResults: int = ...,
        NextToken: str = ...,
        SortBy: PersonTrackingSortByType = ...,
    ) -> GetPersonTrackingResponseTypeDef:
        """
        Gets the path tracking results of a Amazon Rekognition Video analysis started
        by
        StartPersonTracking.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_person_tracking)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_person_tracking)
        """

    async def get_segment_detection(
        self, *, JobId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> GetSegmentDetectionResponseTypeDef:
        """
        Gets the segment detection results of a Amazon Rekognition Video analysis
        started by
        StartSegmentDetection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_segment_detection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_segment_detection)
        """

    async def get_text_detection(
        self, *, JobId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> GetTextDetectionResponseTypeDef:
        """
        Gets the text detection results of a Amazon Rekognition Video analysis started
        by
        StartTextDetection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_text_detection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_text_detection)
        """

    async def index_faces(
        self,
        *,
        CollectionId: str,
        Image: ImageTypeDef,
        ExternalImageId: str = ...,
        DetectionAttributes: Sequence[AttributeType] = ...,
        MaxFaces: int = ...,
        QualityFilter: QualityFilterType = ...,
    ) -> IndexFacesResponseTypeDef:
        """
        Detects faces in the input image and adds them to the specified collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.index_faces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#index_faces)
        """

    async def list_collections(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListCollectionsResponseTypeDef:
        """
        Returns list of collection IDs in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.list_collections)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#list_collections)
        """

    async def list_dataset_entries(
        self,
        *,
        DatasetArn: str,
        ContainsLabels: Sequence[str] = ...,
        Labeled: bool = ...,
        SourceRefContains: str = ...,
        HasErrors: bool = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListDatasetEntriesResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.list_dataset_entries)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#list_dataset_entries)
        """

    async def list_dataset_labels(
        self, *, DatasetArn: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListDatasetLabelsResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.list_dataset_labels)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#list_dataset_labels)
        """

    async def list_faces(
        self,
        *,
        CollectionId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        UserId: str = ...,
        FaceIds: Sequence[str] = ...,
    ) -> ListFacesResponseTypeDef:
        """
        Returns metadata for faces in the specified collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.list_faces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#list_faces)
        """

    async def list_media_analysis_jobs(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListMediaAnalysisJobsResponseTypeDef:
        """
        Returns a list of media analysis jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.list_media_analysis_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#list_media_analysis_jobs)
        """

    async def list_project_policies(
        self, *, ProjectArn: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListProjectPoliciesResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.list_project_policies)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#list_project_policies)
        """

    async def list_stream_processors(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListStreamProcessorsResponseTypeDef:
        """
        Gets a list of stream processors that you have created with
        CreateStreamProcessor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.list_stream_processors)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#list_stream_processors)
        """

    async def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags in an Amazon Rekognition collection, stream processor,
        or Custom Labels
        model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#list_tags_for_resource)
        """

    async def list_users(
        self, *, CollectionId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListUsersResponseTypeDef:
        """
        Returns metadata of the User such as `UserID` in the specified collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.list_users)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#list_users)
        """

    async def put_project_policy(
        self, *, ProjectArn: str, PolicyName: str, PolicyDocument: str, PolicyRevisionId: str = ...
    ) -> PutProjectPolicyResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.put_project_policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#put_project_policy)
        """

    async def recognize_celebrities(
        self, *, Image: ImageTypeDef
    ) -> RecognizeCelebritiesResponseTypeDef:
        """
        Returns an array of celebrities recognized in the input image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.recognize_celebrities)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#recognize_celebrities)
        """

    async def search_faces(
        self,
        *,
        CollectionId: str,
        FaceId: str,
        MaxFaces: int = ...,
        FaceMatchThreshold: float = ...,
    ) -> SearchFacesResponseTypeDef:
        """
        For a given input face ID, searches for matching faces in the collection the
        face belongs
        to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.search_faces)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#search_faces)
        """

    async def search_faces_by_image(
        self,
        *,
        CollectionId: str,
        Image: ImageTypeDef,
        MaxFaces: int = ...,
        FaceMatchThreshold: float = ...,
        QualityFilter: QualityFilterType = ...,
    ) -> SearchFacesByImageResponseTypeDef:
        """
        For a given input image, first detects the largest face in the image, and then
        searches the specified collection for matching
        faces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.search_faces_by_image)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#search_faces_by_image)
        """

    async def search_users(
        self,
        *,
        CollectionId: str,
        UserId: str = ...,
        FaceId: str = ...,
        UserMatchThreshold: float = ...,
        MaxUsers: int = ...,
    ) -> SearchUsersResponseTypeDef:
        """
        Searches for UserIDs within a collection based on a `FaceId` or `UserId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.search_users)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#search_users)
        """

    async def search_users_by_image(
        self,
        *,
        CollectionId: str,
        Image: ImageTypeDef,
        UserMatchThreshold: float = ...,
        MaxUsers: int = ...,
        QualityFilter: QualityFilterType = ...,
    ) -> SearchUsersByImageResponseTypeDef:
        """
        Searches for UserIDs using a supplied image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.search_users_by_image)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#search_users_by_image)
        """

    async def start_celebrity_recognition(
        self,
        *,
        Video: VideoTypeDef,
        ClientRequestToken: str = ...,
        NotificationChannel: NotificationChannelTypeDef = ...,
        JobTag: str = ...,
    ) -> StartCelebrityRecognitionResponseTypeDef:
        """
        Starts asynchronous recognition of celebrities in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_celebrity_recognition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#start_celebrity_recognition)
        """

    async def start_content_moderation(
        self,
        *,
        Video: VideoTypeDef,
        MinConfidence: float = ...,
        ClientRequestToken: str = ...,
        NotificationChannel: NotificationChannelTypeDef = ...,
        JobTag: str = ...,
    ) -> StartContentModerationResponseTypeDef:
        """
        Starts asynchronous detection of inappropriate, unwanted, or offensive content
        in a stored
        video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_content_moderation)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#start_content_moderation)
        """

    async def start_face_detection(
        self,
        *,
        Video: VideoTypeDef,
        ClientRequestToken: str = ...,
        NotificationChannel: NotificationChannelTypeDef = ...,
        FaceAttributes: FaceAttributesType = ...,
        JobTag: str = ...,
    ) -> StartFaceDetectionResponseTypeDef:
        """
        Starts asynchronous detection of faces in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_face_detection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#start_face_detection)
        """

    async def start_face_search(
        self,
        *,
        Video: VideoTypeDef,
        CollectionId: str,
        ClientRequestToken: str = ...,
        FaceMatchThreshold: float = ...,
        NotificationChannel: NotificationChannelTypeDef = ...,
        JobTag: str = ...,
    ) -> StartFaceSearchResponseTypeDef:
        """
        Starts the asynchronous search for faces in a collection that match the faces
        of persons detected in a stored
        video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_face_search)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#start_face_search)
        """

    async def start_label_detection(
        self,
        *,
        Video: VideoTypeDef,
        ClientRequestToken: str = ...,
        MinConfidence: float = ...,
        NotificationChannel: NotificationChannelTypeDef = ...,
        JobTag: str = ...,
        Features: Sequence[Literal["GENERAL_LABELS"]] = ...,
        Settings: LabelDetectionSettingsTypeDef = ...,
    ) -> StartLabelDetectionResponseTypeDef:
        """
        Starts asynchronous detection of labels in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_label_detection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#start_label_detection)
        """

    async def start_media_analysis_job(
        self,
        *,
        OperationsConfig: MediaAnalysisOperationsConfigTypeDef,
        Input: MediaAnalysisInputTypeDef,
        OutputConfig: MediaAnalysisOutputConfigTypeDef,
        ClientRequestToken: str = ...,
        JobName: str = ...,
        KmsKeyId: str = ...,
    ) -> StartMediaAnalysisJobResponseTypeDef:
        """
        Initiates a new media analysis job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_media_analysis_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#start_media_analysis_job)
        """

    async def start_person_tracking(
        self,
        *,
        Video: VideoTypeDef,
        ClientRequestToken: str = ...,
        NotificationChannel: NotificationChannelTypeDef = ...,
        JobTag: str = ...,
    ) -> StartPersonTrackingResponseTypeDef:
        """
        Starts the asynchronous tracking of a person's path in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_person_tracking)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#start_person_tracking)
        """

    async def start_project_version(
        self, *, ProjectVersionArn: str, MinInferenceUnits: int, MaxInferenceUnits: int = ...
    ) -> StartProjectVersionResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_project_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#start_project_version)
        """

    async def start_segment_detection(
        self,
        *,
        Video: VideoTypeDef,
        SegmentTypes: Sequence[SegmentTypeType],
        ClientRequestToken: str = ...,
        NotificationChannel: NotificationChannelTypeDef = ...,
        JobTag: str = ...,
        Filters: StartSegmentDetectionFiltersTypeDef = ...,
    ) -> StartSegmentDetectionResponseTypeDef:
        """
        Starts asynchronous detection of segment detection in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_segment_detection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#start_segment_detection)
        """

    async def start_stream_processor(
        self,
        *,
        Name: str,
        StartSelector: StreamProcessingStartSelectorTypeDef = ...,
        StopSelector: StreamProcessingStopSelectorTypeDef = ...,
    ) -> StartStreamProcessorResponseTypeDef:
        """
        Starts processing a stream processor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_stream_processor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#start_stream_processor)
        """

    async def start_text_detection(
        self,
        *,
        Video: VideoTypeDef,
        ClientRequestToken: str = ...,
        NotificationChannel: NotificationChannelTypeDef = ...,
        JobTag: str = ...,
        Filters: StartTextDetectionFiltersTypeDef = ...,
    ) -> StartTextDetectionResponseTypeDef:
        """
        Starts asynchronous detection of text in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.start_text_detection)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#start_text_detection)
        """

    async def stop_project_version(
        self, *, ProjectVersionArn: str
    ) -> StopProjectVersionResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.stop_project_version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#stop_project_version)
        """

    async def stop_stream_processor(self, *, Name: str) -> Dict[str, Any]:
        """
        Stops a running stream processor that was created by  CreateStreamProcessor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.stop_stream_processor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#stop_stream_processor)
        """

    async def tag_resource(self, *, ResourceArn: str, Tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Adds one or more key-value tags to an Amazon Rekognition collection, stream
        processor, or Custom Labels
        model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from an Amazon Rekognition collection, stream
        processor, or Custom Labels
        model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#untag_resource)
        """

    async def update_dataset_entries(
        self, *, DatasetArn: str, Changes: DatasetChangesTypeDef
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.update_dataset_entries)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#update_dataset_entries)
        """

    async def update_stream_processor(
        self,
        *,
        Name: str,
        SettingsForUpdate: StreamProcessorSettingsForUpdateTypeDef = ...,
        RegionsOfInterestForUpdate: Sequence[RegionOfInterestTypeDef] = ...,
        DataSharingPreferenceForUpdate: StreamProcessorDataSharingPreferenceTypeDef = ...,
        ParametersToDelete: Sequence[StreamProcessorParameterToDeleteType] = ...,
    ) -> Dict[str, Any]:
        """
        Allows you to update a stream processor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.update_stream_processor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#update_stream_processor)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_project_versions"]
    ) -> DescribeProjectVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_projects"]
    ) -> DescribeProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_collections"]
    ) -> ListCollectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_entries"]
    ) -> ListDatasetEntriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_labels"]
    ) -> ListDatasetLabelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_faces"]) -> ListFacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_project_policies"]
    ) -> ListProjectPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_stream_processors"]
    ) -> ListStreamProcessorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_paginator)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["project_version_running"]
    ) -> ProjectVersionRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_waiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["project_version_training_completed"]
    ) -> ProjectVersionTrainingCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.get_waiter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/#get_waiter)
        """

    async def __aenter__(self) -> "RekognitionClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rekognition/client/)
        """
