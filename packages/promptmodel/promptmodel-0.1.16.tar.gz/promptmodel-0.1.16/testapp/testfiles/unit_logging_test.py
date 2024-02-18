from promptmodel import FunctionModel, UnitLogger, init
from datetime import datetime

init(use_cache=False)

async def test():
    current_time = datetime.now()
    
    
    unit: UnitLogger = await UnitLogger("test_unit", 1).log_start()
    res = await FunctionModel("summarize", unit_config=unit.config).arun({"text": "hello, world!"})
    await FunctionModel("summarize").log_score(res.pm_detail.log_uuid, {"accuracy" : 3})
    await unit.log_score({"user_submit" : 1})
    
    
    print("Time Usage: ", datetime.now() - current_time)
    
    current_time = datetime.now()
    res = await FunctionModel("summarize", unit_config=unit.config).arun({"text": "hello, world!"})
    print("Time Usage: ", datetime.now() - current_time)
    
    
    # unit: UnitLogger = UnitLogger("test_unit", 1).log_start()
    # summarize = FunctionModel("summarize", unit_config=unit.config)
    # res = await summarize.arun({"text": "hello, world!"})
    # summarize.log_score({"accuracy" : 3})
    # unit.log_score({"user_submit" : 1})
    

async def test_2():
    unit: UnitLogger = await UnitLogger("test_unit", 2).log_start()
    res = await FunctionModel("summarize", unit_config=unit.config).arun({"text": "hello, world!"})
    print(res.raw_output)
    print(res.pm_detail.log_uuid)
    await unit.log_score({"user_submit" : 1})

if __name__ == "__main__":
    import asyncio
    asyncio.run(test())
    # asyncio.run(test_2())
    
    
