from promptmodel import FunctionModel, init

init(use_cache=False, mask_inputs=False)

async def test():
    api_res = None
    stream_res = await FunctionModel("ENG").astream()
    async for res in stream_res:
        print(res.api_response)
        api_res = res.api_response
    
    print(api_res)
    print(api_res._response_ms)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test())
