import json


class ChannelContext(object):
    def __init__(self, channel_context, mock_data=None):
        if mock_data is None:
            mock_data = dict()

        cc = json.loads(channel_context)
        self.sender_id = cc.get('sender_id', mock_data.get('sender_id', 'developer_id'))
        self.chat_id = cc.get('chat_id', mock_data.get('chat_id'))
        self.chat_type = cc.get('chat_type', mock_data.get('chat_type'))
        self.message_id = cc.get('message_id', mock_data.get('message_id'))
