import requests
from requests import Response


class SlackBot(object):
    def __init__(self, hubot_token: str, bot_name: str = None, icon_url: str = None):
        """
        Args:
            hubot_token(str): hubotのアクセストークン
            bot_name(str): Botの名前を指定したい場合に指定する。Noneの場合はAmebaRPAになります。
            icon_url(str): Botのアイコンを設定したい場合に指定する。
                           Noneの場合は"https://pbs.twimg.com/profile_images/878145658217091073/kTQc1kQ0_400x400.jpg"が反映される。
        Note:
            bot_name,icon_urlが一つでもNoneだとデフォルトの設定が反映されます。
        """
        self.token = hubot_token
        self.bot_name = bot_name
        self.icon_url = icon_url

        if self.bot_name and self.icon_url:
            self.as_user = False
        else:
            self.as_user = True

    def post_message(self, channel_id: str, text: str) -> Response:
        post_message_url: str = 'https://slack.com/api/chat.postMessage'
        data = {
            'token': self.token,
            'username': self.bot_name,
            'icon_url': self.icon_url,
            'as_user': self.as_user,
            'channel': channel_id,
            'text': text
        }
        response = requests.post(url=post_message_url, data=data)

        return response

    def post_file(self, channel_id: str, text: str, file_path: str = None) -> Response:
        """
        Note:
            空のファイルは送信することができません。
        """
        post_file_url: str = 'https://slack.com/api/files.upload'
        data = {
            'token': self.token,
            'username': self.bot_name,
            'icon_url': self.icon_url,
            'as_user': self.as_user,
            'channels': channel_id,
            'initial_comment': text
        }

        files = {'file': open(file_path, 'rb')}
        response = requests.post(post_file_url, data=data, files=files)

        return response
