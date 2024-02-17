import os
import shutil
import websockets
from websockets.sync.client import connect
import socket
import numpy
from tqdm import tqdm
import requests
import struct
import pickle
from typing import Optional, Any
from pathlib import Path

from pydantic import BaseModel

from xflow._private.request_vo import SourceDataInfo, DataSetInfo
from xflow._private._constants import RequestPath, STREAM_DATA_SIZE
from xflow._private._types import DataSourceType, StreamedDataInfo, PacketHeaderType, StreamedDataSetInfo
from xflow._utils import request_util
from xflow._utils.utils import (RollbackContext, PacketHeader, chunker, get_project, get_dataset_upload_url,
                                get_pipeline_info, get_dataset_download_url)
from xflow._utils.decorators import executor_method, client_method
import xflow._private.client as xflow_client


@client_method
def list_dataset():
    xflow_client.init_check()
    client_info: xflow_client.ClientInformation = xflow_client.client_info
    project = client_info.project
    url = client_info.xflow_server_url + RequestPath.dataset_list + f"?project={project}"
    code, msg = request_util.get(url=url)
    if code != 0:
        raise RuntimeError(msg)
    return msg["DATASETS"]


class LoadSteps(BaseModel):
    progress: Any = None
    is_done: bool = False


def load_dataset(name: str, rev: int, trial: int,
                 with_label: bool = False) -> tuple[dict, list] | dict[str, numpy.ndarray | list]:
    project = get_project()
    download_url = get_dataset_download_url()
    req_data = DataSetInfo(PRJ_ID=project, DS_NM=name, REV=rev, TRIAL=trial).dict()
    load_steps = LoadSteps()
    data_info = None
    with requests.post(url=download_url, json=req_data, stream=True) as req:
        res_data = bytearray()
        with RollbackContext(task=clear_get_dataset, steps=load_steps):
            for chunk in req.iter_content(chunk_size=None):
                if chunk is None:
                    raise RuntimeError
                header_len = struct.unpack('H', chunk[:2])[0]
                header = chunk[:header_len]
                data = chunk[header_len:]
                header = struct.unpack("=HcQ", header)
                header_type = header[1]
                contents_length = header[2]
                if header_type == b'0':
                    if data_info is None:
                        raise RuntimeError
                    res_data.extend(data)
                    load_steps.progress.update(contents_length)

                elif header_type == b'1':
                    if data_info is not None:
                        raise RuntimeError
                    data_info = StreamedDataSetInfo(**pickle.loads(data))
                    load_steps.progress = tqdm(total=data_info.SIZE, initial=0, ascii=False)
            load_steps.is_done = True
    res_data = pickle.loads(res_data)
    if with_label:
        return res_data["dataset"], res_data["label"]
    else:
        return res_data["dataset"]


def clear_get_dataset(steps: LoadSteps):
    if steps.progress is not None:
        steps.progress.close()


@executor_method
def save_dataset(name: str, dataset: dict[str, numpy.ndarray], desc: Optional[str] = '',
                 label: Optional[list[str]] = None):
    project, pipeline, rev, trial, reg_id = get_pipeline_info()
    upload_url = get_dataset_upload_url()
    info_data = {"name": name, "project": project, "desc": desc, "pipeline": pipeline, "rev": rev, "trial": trial,
                 "reg_id": reg_id}
    ds_data = {"dataset": dataset, "label": label}
    ds_data = pickle.dumps(ds_data)
    header = PacketHeader(header_type=PacketHeaderType.DATA_INFO)
    data_info = info_data
    data_info = bytearray(pickle.dumps(data_info))
    data = header.create_packet(data=data_info)
    with connect(upload_url) as websocket:
        websocket.send(data)
        message = websocket.recv(1)
        if message != PacketHeaderType.SUCCESS:
            raise RuntimeError
        progress = tqdm(total=len(ds_data), initial=0, ascii=False)
        header = PacketHeader(header_type=PacketHeaderType.DATA)
        try:
            for chunk in chunker(ds_data, STREAM_DATA_SIZE):
                data = header.create_packet(data=chunk)
                websocket.send(data)
                message = websocket.recv(1)
                if message != PacketHeaderType.SUCCESS:
                    raise RuntimeError
                progress.update(len(chunk))
            header = PacketHeader(header_type=PacketHeaderType.EOF)
            data = header.create_packet(data=b'')
            websocket.send(data)
        except Exception as exc:
            raise exc
        finally:
            progress.close()
