import torch

from .llm import (BaseLLM, ChatCompletionRequest, ChatCompletionResponse,
                  ChatCompletionResponseChoice, ChatMessage, torch_gc)

# import time
# from typing import Any, Dict, List, Literal, Optional, Union


def create_chat_completion(model, tokenizer, request: ChatCompletionRequest):
    history = []
    system = ''
    for m in request.messages:
        if m.role == 'system':
            system += m.content
            continue
        history.append(m.dict())

    if system:
        history[-1]['content'] = system + history[-1]['content']

    with torch.no_grad():
        response = model.chat(tokenizer, history)

    choice_data = ChatCompletionResponseChoice(index=0,
                                               message=ChatMessage(
                                                   role='assistant',
                                                   content=response),
                                               finish_reason='stop')

    return ChatCompletionResponse(model=request.model,
                                  choices=[choice_data],
                                  object='chat.completion')


class XverseChat(BaseLLM):
    def __init__(self, **kwargs):
        pretrain_path = kwargs.get('pretrain_path')
        precision = kwargs.get('precision', 'fp16')
        gpu_memory = kwargs.get('gpu_memory')
        devices = kwargs.get('devices').split(',')
        self.devices = devices

        top_p = kwargs.get('top_p', 0.85)
        max_tokens = kwargs.get('max_tokens', 2048)
        do_sample = kwargs.get('do_sample', False)
        temperature = kwargs.get('temperature', 0.5)
        self.default_params = {
            'top_p': top_p,
            'max_new_tokens': max_tokens,
            'do_sample': do_sample,
            'temperature': temperature,
        }

        load_params = {}
        if precision == 'bf16':
            load_params = {'bf16': True}

        use_safetensors = bool(kwargs.get('use_safetensors', '0'))
        use_dispatch = bool(kwargs.get('use_dispatch', '0'))
        load_params.update(use_dispatch=use_dispatch)

        self._load(pretrain_path,
                   precision,
                   devices,
                   gpu_memory,
                   use_safetensors=use_safetensors,
                   **load_params)
        self.generation_config.update(**self.default_params)
        self.model.generation_config = self.generation_config

    def predict(self, kwargs):
        request = ChatCompletionRequest.parse_obj(kwargs)
        resp = create_chat_completion(self.model, self.tokenizer, request)
        torch_gc(self.devices)
        return resp.dict()

    def completion(self, kwargs):
        pass
