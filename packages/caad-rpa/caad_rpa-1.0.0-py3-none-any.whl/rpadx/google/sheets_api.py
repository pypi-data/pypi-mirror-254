import pickle
from typing import Union

import pandas as pd
from pandas.core.frame import DataFrame
from googleapiclient.discovery import build


class SpreadSheet(object):
    """
    指定したスプレッドシートを操作するクラス

    Notes:
        本クラスは、スプレッドシート内の操作です。
        スプレッドシート自体の複製や削除はできません。
    """
    def __init__(self, spreadsheet_id: str):
        self.spreadsheet_id = spreadsheet_id

        with open('token.pickle', 'rb') as token:
            cred = pickle.load(token)
        self.spreadsheet = build(
            'sheets', 'v4', cache_discovery=False, credentials=cred).spreadsheets()

    def load_metadata(self) -> list:
        """
        スプレッドシートのメタデータ(シート名・シートID)を取得する

        Returns:
            meta_list (list): シート名・シートIDが辞書型に入った状態で格納されます。
        """
        sheet_metadata = self.spreadsheet.get(
            spreadsheetId=self.spreadsheet_id).execute()
        sheets = sheet_metadata.get('sheets', '')

        sheet_title_list = [Sheet_Name["properties"]["title"]
                            for Sheet_Name in sheets]

        sheet_id_list = [Sheet_id["properties"]["sheetId"]
                         for Sheet_id in sheets]

        meta_dict: dict = {}
        meta_list: list = []
        for i in range(len(sheet_title_list)):
            meta_dict['title'] = sheet_title_list[i]
            meta_dict['id'] = sheet_id_list[i]
            meta_list.append(meta_dict.copy())
        return meta_list

    def load_table(self, range_: str) -> DataFrame:
        """
        指定箇所をDataFrame形式で取得する

        Args:
            range_ (str): 取得したいセル範囲
        Notes:
            シート名を省略すると、0番目のシートから取得します。
        Examples:
            シートAのA1:A100セルを取得したい場合: ~.load_table("シートA!A1:A100")
        Returns:
            sheet_df (DataFrame): 指定したセルの値が入ったDataFrame
        """
        result = self.spreadsheet.values().get(
            spreadsheetId=self.spreadsheet_id, range=range_).execute()
        values = result.get('values', [])
        sheet_df = pd.DataFrame(values, columns=values[0])
        sheet_df = sheet_df.drop(0)
        sheet_df = sheet_df.reset_index(drop=True)
        return sheet_df

    def load_values(self, range_: str) -> list:
        """
        指定箇所をリスト形式で取得する

         Args:
            range_ (str): 取得したいセル範囲
        Notes:
            シート名を省略すると、0番目のシートから取得します。
        Examples:
            シートAのA1:A100セルを取得したい場合: ~.load_values("シートA!A1:A100")
        Returns:
            values (list): 指定したセルの値が入ったリスト
        """
        result = self.spreadsheet.values().get(
            spreadsheetId=self.spreadsheet_id, range=range_).execute()
        values = result.get('values', [])
        return values

    def append_dataframe(self, range_: str, dataframe: DataFrame) -> None:
        """
        指定箇所にDataFrameを追加する

        Args:
            range_ (str): 追加したいセルの場所
            dataframe (DataFrame): 追加したいDataFrame
        Notes:
            指定した範囲にすでに値が入っている場合、値が入っていない最下部に追加します。
            A1:A5までデータが入っていて、range_に「A1」を指定した場合、A6セルに追加されます。
        """
        self.spreadsheet.values().append(spreadsheetId=self.spreadsheet_id,
                                         valueInputOption="USER_ENTERED",
                                         insertDataOption='OVERWRITE',
                                         range=range_,
                                         body={"values": dataframe.values.tolist()}).execute()

    def set_values(self, range_: str, values: list) -> None:
        """
        指定箇所にリストを追加する

        Args:
            range_ (str): 追加したいセルの場所
            values (list): 追加したい値
        Notes:
            valuesについて
                単体の値を引数に入れる場合はリストをさらに[]で囲ってください。
                例：~.set_values("A1", [["hello"]])

                複数の値を入れる場合は以下を参考にしてください。
                ・横に追加したい場合:[[a, b, c]]
                ・縦に追加したい場合:[[a], [b], [c]]
                ・値を横2列、縦3列で追加したい場合:[[a1, a2], [b1, b2], [c1, c2]]
        """
        self.spreadsheet.values().update(spreadsheetId=self.spreadsheet_id,
                                         valueInputOption="USER_ENTERED",
                                         range=range_,
                                         body={"values": values}).execute()

    def clear_range(self, range_: str) -> None:
        """
        指定したRangeの値をクリアする

        Args:
            range_(str) : クリアしたいセルの場所。

        Notes:
            値のみのクリアのため、書式はリセットされません。
        """
        self.spreadsheet.values().clear(spreadsheetId=self.spreadsheet_id,
                                        range=range_, body={}).execute()

    def create_sheet(self, new_sheet_name: str) -> dict:
        """
        シートを作成する

        Args:
            new_sheet_name: 作成したいシート名
        Returns:
            sheet_id (dict): シートIDをdict型{'sheet_id': sheet_id}で返します。
        """
        requests = [{
            'addSheet': {
                "properties": {
                    "title": new_sheet_name,
                }
            }
        }]
        body = {'requests': requests}
        response = self.spreadsheet.batchUpdate(
            spreadsheetId=self.spreadsheet_id, body=body).execute()
        sheet_id = response['replies'][0]['addSheet']['properties']['sheetId']
        return {'sheet_id': sheet_id}

    def delete_sheet(self, sheet_id: Union[str, int]) -> None:
        """
        指定したシートを削除する

        Args:
            sheet_id (str|int): 削除したいシートのID。str・intどちらでも可。
        """
        requests = [{
            'deleteSheet': {
                "sheetId": sheet_id
            }
        }]

        body = {'requests': requests}
        self.spreadsheet.batchUpdate(
            spreadsheetId=self.spreadsheet_id, body=body).execute()

    def duplicate_sheet(self, master_sheet_id: Union[str, int], new_sheet_name: str, insert_index: int = 0) -> dict:
        """
        指定したシートを複製する

        Args:
            master_sheet_id (str|int): 複製元のシートID
            new_sheet_name(str): 新しいシートの名前
            insert_index(int): 追加したいシートの場所。省略すると0番目に追加。

        Notes:
            master_sheet_idはスプレッドシートの末尾につく数字(sheet_id部分)を記載してください。
            例：https://docs.google.com/spreadsheets/d/{spreadsheet_id}/edit#gid={sheet_id}

        Returns:
            result (dict): 複製したシートのデータ
        """

        body = {
            'requests': [
                {
                    'duplicateSheet': {
                        'sourceSheetId': master_sheet_id,
                        'newSheetName': new_sheet_name,
                        'insertSheetIndex': insert_index
                    }
                }
            ]
        }
        result: dict = self.spreadsheet.batchUpdate(spreadsheetId=self.spreadsheet_id, body=body).execute()
        return result
