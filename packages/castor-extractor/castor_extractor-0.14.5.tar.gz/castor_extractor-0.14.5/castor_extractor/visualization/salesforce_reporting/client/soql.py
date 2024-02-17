from ..assets import SalesforceReportingAsset

queries = {
    SalesforceReportingAsset.DASHBOARDS: """
        SELECT
            CreatedBy.Id,
            CreatedDate,
            Description,
            DeveloperName,
            FolderId,
            FolderName,
            IsDeleted,
            LastReferencedDate,
            LastViewedDate,
            NamespacePrefix,
            RunningUserId,
            Title,
            Type
        FROM Dashboard
    """,
    SalesforceReportingAsset.REPORTS: """
        SELECT
            Description,
            DeveloperName,
            FolderName,
            Format,
            IsDeleted,
            LastReferencedDate,
            LastRunDate,
            LastViewedDate,
            Name,
            NamespacePrefix,
            OwnerId
        FROM Report
    """,
    SalesforceReportingAsset.USERS: """
        SELECT
            Id,
            Email,
            FirstName,
            LastName,
            CreatedDate
        FROM User
    """,
}
