from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import calldetail as components_calldetail
from dataclasses_json import Undefined, dataclass_json
from retellclient import utils
from typing import List, Optional



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RegisterCallRequestBody:
    agent_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('agent_id') }})
    r"""Corresponding agent id of this call."""
    audio_encoding: components_calldetail.AudioEncoding = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('audio_encoding') }})
    r"""The audio encoding of the call."""
    audio_websocket_protocol: components_calldetail.AudioWebsocketProtocol = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('audio_websocket_protocol') }})
    r"""The protocol how audio websocket read and send audio bytes."""
    sample_rate: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sample_rate') }})
    r"""Sample rate of the conversation, the input and output audio bytes will all conform to this rate."""
    

@dataclasses.dataclass
class RegisterCallRequestResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    agent: Optional[components_calldetail.Agent] = dataclasses.field(default=None)
    r"""Successfully created a new agent."""