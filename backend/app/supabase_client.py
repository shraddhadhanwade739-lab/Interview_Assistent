import os
from supabase import create_client, Client

# Use environment variables in Render
SUPABASE_URL = os.getenv( "https://dycqfwvouusuktsfvjun.supabase.co"
)
SUPABASE_SERVICE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR5Y3Fmd3ZvdXVzdWt0c2Z2anVuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1NDQ2NDY2MiwiZXhwIjoyMDcwMDQwNjYyfQ.e0g_42t4XXygLCg3_MJIlOm13JWaOIKEtGfsVle-cPk")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

def upload_file(bucket_name: str, file_path: str):
    """Uploads a file to the given bucket and returns the public URL."""
    file_name = os.path.basename(file_path)
    
    with open(file_path, "rb") as f:
        res = supabase.storage.from_(bucket_name).upload(file_name, f, {"upsert": True})
    
    if res is None or "error" in str(res).lower():
        raise Exception(f"Failed to upload {file_name}: {res}")
    
    # Get public URL
    public_url = supabase.storage.from_(bucket_name).get_public_url(file_name)
    return public_url
