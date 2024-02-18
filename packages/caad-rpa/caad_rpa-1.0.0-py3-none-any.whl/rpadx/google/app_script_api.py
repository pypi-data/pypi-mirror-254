import pickle
from googleapiclient.discovery import build


with open('token.pickle', 'rb') as token:
    cred = pickle.load(token)
service = build('script', 'v1', credentials=cred)


def run_func(script_id: str, func_name: str, param: list = None, dev_mode: bool = True) -> dict:
    """関数の実行

    Args:
        script_id(str) : GASのスクリプトID
        func_name (str): 実行したい関数名
        param (list): 実行したい関数の引数をリストに格納
        dev_mode (bool): 常に新しいデプロイのバージョンで実行する場合は、True

    Notes:
        script_idは事前にデブロイが必要
    """
    if param is None:
        param = []
    script = service.scripts()
    body: dict = {
        "scriptId": script_id,
        "body": {
            "devMode": dev_mode,
            "function": func_name,
            "parameters": param
        }
    }
    result_json = script.run(**body).execute()
    return result_json
