import io
import mimetypes
import os
import pickle

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload


with open('token.pickle', 'rb') as token:
    credentials = pickle.load(token)

SERVICE = build("drive", "v3", credentials=credentials)


def search_files(folder_id: str) -> list[dict]:
    """ 入力されたフォルダIDに保存されているファイルとフォルダのIDと名前をリストに格納されたdictで返します。

    Args:
        folder_id (str): 検索をかけたいDriveフォルダID
    Note:
        search_fileというメソッド名ですがフォルダも検索されます。
        検索されたフォルダ内のファイルは検索されません。
    """

    query = f"'{folder_id}' in parents and trashed=false"
    page_token = None
    items: list[dict] = []
    while True:
        result = SERVICE.files().list(
            fields="nextPageToken, files(id, name)",
            q=query,
            pageToken=page_token
        ).execute()

        items.extend(result.get('files', []))
        page_token = result.get('nextPageToken', None)

        if page_token is None:
            break

    return items


def download_file(file_id: str, destination_path: str, new_file_name: str) -> None:
    """ ファイルIDを指定して、そのファイルをダウンロードします。

    Args:
        file_id(str): ダウンロードしたいファイルのファイルID
        destination_path(str): ダウンロードしたファイルの保存先の絶対パス
        new_file_name(str): ローカルディレクトリに保存する際のファイル名
    Note:
        このメソッドでフォルダはダウンロードできません。
    """
    request = SERVICE.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()

    fh.seek(0)

    with open(os.path.join(destination_path, new_file_name), 'wb') as f:
        f.write(fh.read())
        f.close()


def upload_file(folder_id: str, file_path: str) -> str:
    """ ローカルに保存されているファイルを、入力されたIDのフォルダにアップロードします。

    Args:
        folder_id (str): アップロード先のフォルダID
        file_path (str): アップロードしたいファイルパス
    Note:
        このメソッドではフォルダはアップロードできません。
        file_pathはフルパスで入力した方が安定します。

    Return:
        uploaded_file['id'] (str): アップロードされたファイルのID
        uploaded_fileはdictでidが格納されている。{'id': 'XXXXXXXXXXXXX'}
    """
    mime = mimetypes.guess_type(f"{file_path}")[0]
    file_name = os.path.basename(file_path)

    body = {"name": file_name, "mimeType": mime, "parents": [folder_id] }
    media = MediaFileUpload(file_path, mimetype=mime, resumable=True)

    uploaded_file: dict = SERVICE.files().create(body=body, media_body=media, fields='id').execute()

    return uploaded_file['id']


def delete_file(file_id: str) -> None:
    """入力されたIDのファイルまたはフォルダを削除します。

    Args:
        file_id (str): 削除したいファイルのファイルID
    Note:
        delete_fileというメソッド名ですがフォルダも削除できます。
    """
    SERVICE.files().delete(fileId=file_id).execute()


def create_folder(parent_folder_id: str, new_folder_name: str) -> str:
    """入力されたフォルダID内に、入力されたフォルダ名で新しいフォルダを作成する。

    Args:
        parent_folder_id (str): 作成したフォルダの格納先
        new_folder_name (str): 作成したいフォルダの名前
    Return:
        created_folder['id'](str): 作成したフォルダのIDを返します。
        created_folder_id = {'id': 'XXXXXXXXXXXXXXXXXX'}
    """

    body = {
        'name': new_folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_folder_id]
    }

    created_folder: dict = SERVICE.files().create(body=body, fields='id').execute()

    return created_folder['id']


def download_folder(folder_id: str, destination_path: str) -> None:
    """ folder_idで指定したフォルダより下の階層の全フォルダとファイルをダウンロードする。

    Args:
        folder_id: ダウンロードしたいフォルダのID
        destination_path: 保存先のパス。絶対パス推奨。
    Notes:
        folder_idで指定したフォルダは作成されません。指定したい場合はdestination_pathで同じ名前にしてください。
    """

    # フォルダの中身を取得する
    results = SERVICE.files().list(q=f"trashed = false and parents in '{folder_id}'",
                                   fields="nextPageToken, files(id, name, mimeType)").execute()
    items = results.get('files', [])

    # フォルダの名前でディレクトリを作成する
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    # ファイルをダウンロードする
    for item in items:
        item_id = item['id']
        item_name = item['name']
        item_type = item['mimeType']
        path = os.path.join(destination_path, item_name)

        # ファイルの場合
        if item_type != 'application/vnd.google-apps.folder':
            request = SERVICE.files().get_media(fileId=item_id)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                _, done = downloader.next_chunk()

            # ファイルを保存する
            with open(path, 'wb') as f:
                fh.seek(0)
                f.write(fh.read())
        # フォルダの場合
        else:
            download_folder(item_id, path)


def upload_folder(folder_path: str, parent_folder_id: str = None, new_folder_name: str = None) -> None:
    """ 指定したパスのフォルダごとドライブにアップロードする。

    Args:
        folder_path: アップロードしたいフォルダパス
        parent_folder_id: アップロード先の親フォルダID。指定がない場合はマイドライブ内にアップロードされます。
        new_folder_name: アップロード時のフォルダ名。デフォルトはfolder_pathで指定したフォルダ名になります。
    """
    # フォルダの作成
    if new_folder_name is None:
        new_folder_name = os.path.basename(folder_path)
    folder_metadata = {'name': new_folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
    if parent_folder_id:
        folder_metadata['parents'] = [parent_folder_id]
    folder = SERVICE.files().create(body=folder_metadata, fields='id').execute()
    folder_id = folder.get('id')

    # フォルダ内のファイルとフォルダをアップロードする
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)

        # ファイルの場合
        if os.path.isfile(filepath):
            file_metadata = {'name': filename, 'parents': [folder_id]}
            media = MediaFileUpload(filepath, resumable=True)
            SERVICE.files().create(body=file_metadata, media_body=media, fields='id').execute()
        # フォルダの場合
        elif os.path.isdir(filepath):
            upload_folder(filepath, parent_folder_id=folder_id)
