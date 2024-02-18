from azure.storage.blob import BlobServiceClient, ContentSettings, BlobSasPermissions
from datetime import datetime, timedelta

def generate_sas_url(account_name, account_key, container_name, blob_name, duration_hours):
    blob_service = BlobServiceClient(account_name=account_name, account_key=account_key)

    # Set the start time to the current time
    start_time = datetime.utcnow()
    # Set the expiration time for the SAS token
    expiration_time = start_time + timedelta(hours=duration_hours)

    # Set permissions
    permissions = BlobSasPermissions(read=True)

    # Generate the SAS token
    sas_token = blob_service.generate_blob_shared_access_signature(
        container_name,
        blob_name,
        permission=permissions,
        start=start_time,
        expiry=expiration_time
    )

    # Construct the SAS URL
    sas_url = f"https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_token}"

    return sas_url

# Replace these with your own values
account_name = 'devprofjim'
account_key = 'DPVwyxtT8Frao9ufKozJOsmhEZ33AOL65OdUmfmX+EVzEgPc2i7Qx5wfydPDcjSuCOIhItm6VVnv+AStI69doA=='
container_name = 'animations'
blob_name = 'C:/Users/srava/Downloads/test_heygen.wav'
duration_hours = 1  # Set the duration for which the SAS token is valid

audio_sas_url = generate_sas_url(account_name, account_key, container_name, blob_name, duration_hours)

# Now you can use 'audio_sas_url' in your API request
print(f"SAS URL for the audio file: {audio_sas_url}")