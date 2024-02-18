import pickle

from googleapiclient.discovery import build


with open('token.pickle', 'rb') as token:
    credentials = pickle.load(token)

SERVICE = build("docs", "v1", credentials=credentials)


def read_all_text(document_id: str) -> str:
    """ ドキュメントから本文を取得する
        Python クイックスタート (https://developers.google.com/docs/api/quickstart/python?hl=ja)
        ドキュメントからテキストを抽出する (https://developers.google.com/docs/api/samples/extract-text)
    """

    document = SERVICE.documents().get(documentId=document_id).execute()
    doc_contents = document.get('body').get('content')

    text = ''
    for value in doc_contents:
        if 'paragraph' in value:
            doc_contents = value.get('paragraph').get('elements')
            for elem in doc_contents:
                text_run = elem.get('textRun')
                if  text_run:
                    text += text_run.get('content')
                else:
                    text += ''

        elif 'table' in value:
            # (表セル内のテキストはネストされた構造要素にあり、表はネストされることがある)
            table = value.get('table')
            for row in table.get('tableRows'):
                cells = row.get('tableCells')
                for cell in cells:
                    text += read_all_text(cell.get('content'))
        elif 'tableOfContents' in value:
            # (TOCのテキストもStructural Elementの中にある)
            toc = value.get('tableOfContents')
            text += read_all_text(toc.get('content'))
    return text
