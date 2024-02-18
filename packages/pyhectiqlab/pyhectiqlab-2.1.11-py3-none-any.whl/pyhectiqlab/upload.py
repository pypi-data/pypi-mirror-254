import os
import requests
import io
from tqdm import tqdm
from google.resumable_media.requests import ResumableUpload
import logging
logger = logging.getLogger('pyhectiqlab')

use_tqdm = os.getenv("HECTIQLAB_NO_TQDM", "0")!="1"
def upload_by_fragments(filepath: str, resumable_session_url: str, chunk_size: int = 1024*1024*32):
    """
    chunk_size: Size of the fragments (1024*1024==1Mb)
    """
    logger.debug(f'Fragment upload for {filepath}\nresumable_session_url: {resumable_session_url}\nchunk_size: {chunk_size}')

    upload = ResumableUpload(
        upload_url=resumable_session_url,
        chunk_size=chunk_size
    )
    data = open(filepath, 'rb').read()
    upload._stream = io.BytesIO(data)
    upload._total_bytes = len(data)
    upload._resumable_url = resumable_session_url
    
    transport = requests.Session()
    if use_tqdm:
        progress_bar = tqdm(total=upload.total_bytes, unit='iB', unit_scale=True)

    bytes_uploaded = 0
    while upload.finished==False:
        res = upload.transmit_next_chunk(transport)
        if use_tqdm:
            progress_bar.update(upload.bytes_uploaded-bytes_uploaded)
        bytes_uploaded = upload.bytes_uploaded
        assert res.status_code in [200,308], f'An error occured while uploading the file {filepath}\n{res.status_code}:: {res.text}'
    return 

def upload_with_signed_url(filepath: str, bucket_name: str, url: str, fields: dict):
    logger.debug(f'Single upload for {filepath}\nbucket_name: {bucket_name}\nurl: {url}')
    content_bytes = open(filepath, "rb")
    files = {"file": (bucket_name, content_bytes)}
    requests.post(url, data=fields, files=files)

def upload_file(filepath: str, policy: dict):
    """
    """
    if policy.get("active"):
        # Skip if file is active
        return
    upload_method = policy.get('upload_method')
    if upload_method=='fragment':
        logger.debug(f'Fragment upload for {filepath}')
        upload_by_fragments(filepath, 
            resumable_session_url=policy.get('url'))
    elif upload_method is None or upload_method=='single':
        logger.debug(f'Single upload for {filepath}')

        creds = policy.get('policy')
        upload_with_signed_url(filepath, 
            bucket_name=policy.get('bucket_name'),
            url=creds.get('url'),
            fields=creds.get('fields')
            )
    else:
        assert False, f'Unrecognized upload_method ({upload_method}).'
    logger.debug(f'Upload completed for {filepath}')

    return