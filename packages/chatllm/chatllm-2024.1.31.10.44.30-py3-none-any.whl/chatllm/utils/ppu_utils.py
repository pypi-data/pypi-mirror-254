#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : ppu_utils
# @Time         : 2024/1/8 16:46
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : 按次计费

from meutils.pipe import *


@background_task
def get_ppu_usage(api_key: Optional[str] = None, base_url: Optional[str] = None, model: str = 'ppu'):
    from openai import OpenAI

    openai = OpenAI(api_key=api_key, base_url=base_url or "https://api.chatllm.vip/v1")
    return openai.chat.completions.create(model=model, messages=[{"role": "user", "content": "hi"}])


if __name__ == '__main__':
    print(get_ppu_usage())
