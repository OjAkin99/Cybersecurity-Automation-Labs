import boto3

# Step 1: Connect to the AWS cloud storage service using the boto3 library
s3_client = boto3.client('s3')

# ⚠️ CHANGE THIS: Replace the text inside the quotation marks with your exact AWS folder name
BUCKET_NAME = "aws-coud-project-2026"

try:
    # Step 2: Query AWS to find out the public access settings for your folder
    response = s3_client.get_public_access_block(Bucket=BUCKET_NAME)
    
    # Step 3: Check if the master "block all public access" rule is set to True
    is_secure = response['PublicAccessBlockConfiguration''BlockPublicPolicy']
    
    print("--- [ CLOUD SECURITY AUDITOR ] ---")
    if is_secure:
        print(f"✅ SUCCESS: Bucket '{BUCKET_NAME}' is secure. Public access is blocked.")
    else:
        print(f"🚨 WARNING: Bucket '{BUCKET_NAME}' is exposed to the public internet!")

except Exception as e:
    # If the folder has no security block configured at all, AWS will trigger an error
    print("--- [ CLOUD SECURITY AUDITOR ] ---")
    print(f"🚨 WARNING: Bucket '{BUCKET_NAME}' has NO security configurations! Error: {e}")
