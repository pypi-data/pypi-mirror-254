import time
import shutil 
import os
import io
import boto3
import botocore
from typing import List
import pickle

from .io_config import IO_Config



class IO_Reader:
    def __init__(self, settings: IO_Config) -> None:
        try:
            config = settings
            self.cloud_data = config.cloud_data
            if self.cloud_data:
                self.resource = boto3.resource(
                    "s3",
                    region_name=config.region_name,
                    aws_access_key_id=config.aws_access_key_id,
                    aws_secret_access_key=config.aws_secret_access_key,
                )
                self.region_name = config.region_name
        except Exception as e:
            raise e

    def read(self, bucket_name: str, path: str, compress: bool) -> str:
        try:
            if self.cloud_data:
                response_body = io.BytesIO()
                self.resource.Object(bucket_name, path).download_fileobj(response_body)
                response = response_body.getvalue()
            else:
                with open(path, "rb") as f:
                    response = f.read()
            return response
        except Exception as e:
            raise e

    def read_string(self, path: str, name: str, compress: bool) -> str:
        try:
            if self.cloud_data:
                response = self.resource.Object(path, name).get()
            else:
                with open(name, "rb") as f:
                    response = {"Body": f}
            return response["Body"].read().decode("utf-8")
        except Exception as e:
            raise e

    def read_csv(self, path: str, name: str, compress: bool) -> List[str]:
        try:
            if self.cloud_data:
                response_body = self.resource.Object(path, name).get()
                response = response_body["Body"].read().decode("utf-8").split("\r\n")
            else:
                with open(name, "rb") as f:
                    response = f.read().decode("utf-8").split("\r\n")
            return response
        except Exception as e:
            raise e
        
    def read_pickle(self, path: str, name: str) -> any:
        try:
            if self.cloud_data:
                response_body = self.resource.Object(path, name).get()
                response = response_body["Body"].read()
                obj = pickle.loads(response)
                return obj
            else:
                return pickle.load(name, 'rb')
            return response
        except Exception as e:
            raise e


    def read_zip_directory(
        self,
        bucket_name: str,
        path: str,
        directory_path: str,
        directory_name: str,
    ) -> bool:
        try:
            if self.cloud_data:

                full_directory_path = os.path.join(directory_path, directory_name)

                if not os.path.exists(full_directory_path):
                    os.makedirs(full_directory_path)

                self.resource.Object(bucket_name, os.path.join(path, f'{directory_name}.zip').replace("\\","/")).download_file(f'{full_directory_path}.zip')
                
                shutil.unpack_archive(f'{full_directory_path}.zip', full_directory_path, 'zip') # , directory_path, 'zip'

                if os.path.exists(f'{full_directory_path}.zip'):
                    os.remove(f'{full_directory_path}.zip')
        except Exception as e:
            raise e

    def object_exists(self, path: str, object_type: str) -> bool:
        try:
            self.resource.Object(path).load()
        except botocore.exceptions.ClientError:
            return False
        return True
