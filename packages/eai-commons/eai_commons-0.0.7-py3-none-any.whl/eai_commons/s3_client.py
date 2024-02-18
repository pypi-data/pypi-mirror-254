try:
    import boto3
except ImportError:
    raise ImportError(
        "Could not import boto3 python package. "
        "Please install it with `pip install boto3` and `pip install botocore`."
    )
import os
from eai_commons.utils.file import create_dir_if_not_existed


class S3Client:
    def __init__(
        self,
        endpoint_url: str,
        use_ssl: bool,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        bucket: str,
        region_name: str = "us-east-1",
    ) -> None:
        self.client = boto3.client(
            "s3",
            endpoint_url=endpoint_url,
            use_ssl=use_ssl,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
            config=boto3.session.Config(s3={"addressing_style": "path"}),
        )
        self.bucket = bucket

    def upload_s3_object(self, content: bytes, filepath: str):
        self.client.put_object(
            Bucket=self.bucket,
            Key=filepath,
            Body=content,
        )

    def list_s3_files(self, prefix: str) -> list[str]:
        if not prefix.endswith("/"):
            prefix = prefix + "/"
        resp = self.client.list_objects(
            Bucket=self.bucket,
            Prefix=prefix,
            Delimiter="/",
        )
        if "Contents" in resp:
            return [content["Key"] for content in resp["Contents"]]
        return []

    def download_s3_files_local(
        self, keys: list[str], local_dir: str, skip_if_existed: bool = True
    ):
        create_dir_if_not_existed(local_dir)
        for key in keys:
            # Extract the file name from the object key
            file_name = key.split("/")[-1]
            if os.path.exists(f"{local_dir}/{file_name}") and skip_if_existed:
                continue
            self.client.download_file(self.bucket, key, f"{local_dir}/{file_name}")

    def delete_file(self, filepath: str):
        self.client.delete_object(Bucket=self.bucket, Key=filepath)
