from promptmodel import DevClient, FunctionModel
from promptmodel.types import FunctionModelConfig

dev = DevClient()

config: FunctionModelConfig = FunctionModel("new_prompt").get_config()

@dev.register
def summarize(text: str) -> str:
    res = FunctionModel("summarize").run({"text" : text})
    print(res.raw_output)
    
# main
if __name__ == "__main__":
    summarize("This is a test")