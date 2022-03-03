from yoti_python_sdk.doc_scan import (DocScanClient)

sandbox_client_sdk_id = '73c1e9e7-3fd4-4530-8cb3-5009ddfa12f4'
pem_file_path = 'C:\privateKey.pem'

doc_scan_client = DocScanClient(sandbox_client_sdk_id, pem_file_path, api_url="https://api.yoti.com/sandbox/idverify/v1")

from yoti_python_sandbox.doc_scan.client import DocScanSandboxClient


doc_scan_client = DocScanClient(sandbox_client_sdk_id, pem_file_path)



from yoti_python_sdk.doc_scan import (
    DocScanClient,
    RequestedDocumentAuthenticityCheckBuilder,
    RequestedFaceMatchCheckBuilder,
    RequestedIDDocumentComparisonCheckBuilder,
    RequestedLivenessCheckBuilder,
    RequestedTextExtractionTaskBuilder,
    RequestedSupplementaryDocTextExtractionTaskBuilder,
    SdkConfigBuilder,
    SessionSpecBuilder,
    NotificationConfigBuilder

)

doc_scan_client = DocScanClient(sandbox_client_sdk_id, pem_file_path)



sdk_config = (
        SdkConfigBuilder()
        .with_allows_camera_and_upload()
        .with_primary_colour("#2d9fff")
        .with_secondary_colour("#FFFFFF")
        .with_font_colour("#FFFFFF")
        .with_locale("en-GB")
        .with_preset_issuing_country("GBR")

        .build()
    )


notification_config = (
    NotificationConfigBuilder()
    .with_endpoint('https://api.yoti.com/sandbox/idverify/v1')
    .with_auth_token('username:password')
    .for_resource_update()
    .for_task_completion()
    .for_check_completion()
    .for_session_completion()
    .build()
)

session_spec = (
    SessionSpecBuilder()
    .with_client_session_token_ttl(600)
    .with_resources_ttl(90000)
    .with_user_tracking_id("some-user-tracking-id")
    .with_requested_check(RequestedDocumentAuthenticityCheckBuilder().build()
    )
    
    .with_requested_task(
        RequestedTextExtractionTaskBuilder().with_manual_check_always().build()
    )
    .with_sdk_config(sdk_config)
    .with_notifications(notification_config)

    .build()
)

session = doc_scan_client.create_session(session_spec)
