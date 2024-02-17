
from google.cloud import dialogflowcx as cx

from google.protobuf.json_format import MessageToDict
from google.protobuf.struct_pb2 import Struct

# 2023-12-11 
# - Now with docstrings!

class WebhookResponse:

    """
    Class to build a WebhookResponse object.

    Args:
        None.
    """

    def __init__(self):
        self.__message: cx.WebhookResponse = cx.WebhookResponse(
            fulfillment_response=self.FulfillmentResponse(messages=[])
        )

    # gRPC Message attributes exposed as properties;
    # Easier on traditional linters and formatters.

    @property
    def fulfillment_response(self) -> cx.WebhookResponse.FulfillmentResponse:
        """
        Returns the fulfillment response.

        Args:
            None.

        Returns:
            cx.WebhookResponse.FulfillmentResponse: The fulfillment response.
        """
        return self.__message.fulfillment_response

    @property
    def page_info(self) -> cx.PageInfo:
        """
        Returns the page info.

        Args:
            None.

        Returns:
            cx.PageInfo: The page info.
        """
        return self.__message.page_info

    @property
    def session_info(self) -> cx.SessionInfo:
        """
        Returns the session info.

        Args:
            None.

        Returns:
            cx.SessionInfo: The session info.
        """
        return self.__message.session_info

    @property
    def payload(self) -> Struct:
        """
        Returns the payload.

        Args:
            None.

        Returns:
            Struct: The payload.
        """
        return self.__message.payload

    @property
    def FulfillmentResponse(self) -> cx.WebhookResponse.FulfillmentResponse:
        """
        Returns the FulfillmentResponse class.

        Args:
            None.

        Returns:
            cx.WebhookResponse.FulfillmentResponse: The FulfillmentResponse class.
        """
        return cx.WebhookResponse.FulfillmentResponse

    @property
    def ResponseMessage(self) -> cx.ResponseMessage:
        """
        Returns the ResponseMessage class.

        Args:
            None.

        Returns:
            cx.ResponseMessage: The ResponseMessage class.
        """
        return cx.ResponseMessage

    @property
    def Text(self) -> cx.ResponseMessage.Text:
        """
        Returns the Text class.

        Args:
            None.

        Returns:
            cx.ResponseMessage.Text: The Text class.
        """
        return cx.ResponseMessage.Text

    @property
    def ConversationSuccess(self) -> cx.ResponseMessage.ConversationSuccess:
        """
        Returns the ConversationSuccess class.

        Args:
            None.

        Returns:
            cx.ResponseMessage.ConversationSuccess: The ConversationSuccess class.
        """
        return cx.ResponseMessage.ConversationSuccess

    @property
    def OutputAudioText(self) -> cx.ResponseMessage.OutputAudioText:
        """
        Returns the OutputAudioText class.

        Args:
            None.

        Returns:
            cx.ResponseMessage.OutputAudioText: The OutputAudioText class.
        """
        return cx.ResponseMessage.OutputAudioText

    @property
    def LiveAgentHandoff(self) -> cx.ResponseMessage.LiveAgentHandoff:
        """
        Returns the LiveAgentHandoff class.

        Args:
            None.

        Returns:
            cx.ResponseMessage.LiveAgentHandoff: The LiveAgentHandoff class.
        """
        return cx.ResponseMessage.LiveAgentHandoff

    @property
    def PlayAudio(self) -> cx.ResponseMessage.PlayAudio:
        """
        Returns the PlayAudio class.

        Args:
            None.

        Returns:
            cx.ResponseMessage.PlayAudio: The PlayAudio class.
        """
        return cx.ResponseMessage.PlayAudio

    @property
    def TelephonyTransferCall(self) -> cx.ResponseMessage.TelephonyTransferCall:
        """
        Returns the TelephonyTransferCall class.

        Args:
            None.

        Returns:
            cx.ResponseMessage.TelephonyTransferCall: The TelephonyTransferCall class.
        """
        return cx.ResponseMessage.TelephonyTransferCall

    def add_response(self, response_message: cx.ResponseMessage):
        """Adds a response message to the WebhookResponse object.

        Args:
            response_message: The response message to add.

        Returns:
            The WebhookResponse object.
        """
        self.fulfillment_response.messages.append(response_message)
        return self

    def add_text_response(self, *texts, channel=""):
        """Adds a text response message to the WebhookResponse object.

        Args:
            *texts: The text messages to add.
            channel: The channel to send the response message to.

        Returns:
            The WebhookResponse object.
        """
        text = self.Text(text=texts)
        response_message = self.ResponseMessage(text=text, channel=channel)
        self.add_response(response_message)
        return self

    def add_conversation_success(self, metadata: dict, channel=""):
        """Adds a conversation success response message to the WebhookResponse object.

        Args:
            metadata: The metadata to include in the response message.
            channel: The channel to send the response message to.

        Returns:
            The WebhookResponse object.
        """
        conversation_success = self.ConversationSuccess(metadata=metadata)
        response_message = self.ResponseMessage(conversation_success=conversation_success, channel=channel)
        self.add_response(response_message)
        return self

    def add_payload_response(self, payload: dict, channel=""):
        """Adds a payload response message to the WebhookResponse object.

        Args:
            payload: The payload to include in the response message.
            channel: The channel to send the response message to.

        Returns:
            The WebhookResponse object.
        """
        # ResponseMessage instantiation with value of Payload handles this automatically
        # This is the "mapping" interface; no need for Struct and ParseDict
        response_message = self.ResponseMessage(payload=payload, channel=channel)
        self.add_response(response_message)
        return self

    def add_ssml_response(self, ssml: str, channel=""):
        """Adds a SSML response message to the WebhookResponse object.

        Args:
            ssml: The SSML to include in the response message.
            channel: The channel to send the response message to.

        Returns:
            The WebhookResponse object.
        """
        output_audio_text = self.OutputAudioText(ssml=ssml)
        response_message = cx.ResponseMessage(output_audio_text=output_audio_text, channel=channel)
        self.add_response(response_message)
        return self

    def add_play_audio(self, audio_uri: str, channel=""):
        """Adds a play audio response message to the WebhookResponse object.

        Args:
            audio_uri: The audio URI to include in the response message.
            channel: The channel to send the response message to.

        Returns:
            The WebhookResponse object.
        """
        play_audio = self.PlayAudio(audio_uri=audio_uri)
        response_message = cx.ResponseMessage(play_audio=play_audio, channel=channel)
        self.add_response(response_message)
        return self

    def add_live_agent_handoff(self, metadata: dict, channel=""):
        """Adds a live agent handoff response message to the WebhookResponse object.

        Args:
            metadata: The metadata to include in the response message.
            channel: The channel to send the response message to.

        Returns:
            The WebhookResponse object.
        """
        live_agent_handoff = self.LiveAgentHandoff(metadata=metadata)
        response_message = cx.ResponseMessage(live_agent_handoff=live_agent_handoff, channel=channel)
        self.add_response(response_message)
        return self

    def add_telephony_transfer_call(self, phone_number: str, channel=""):
        """Adds a telephony transfer call response message to the WebhookResponse object.

        Args:
            phone_number: The phone number to transfer the call to.
            channel: The channel to send the response message to.

        Returns:
            The WebhookResponse object.
        """
        telephony_transfer_call = self.TelephonyTransferCall(phone_number=phone_number)
        response_message = cx.ResponseMessage(telephony_transfer_call=telephony_transfer_call, channel=channel)
        self.add_response(response_message)
        return self

    def add_session_parameters(self, parameters: dict):
        """Adds session parameters to the WebhookResponse object.

        Args:
            parameters: The session parameters to add.

        Returns:
            The WebhookResponse object.
        """
        session_info = cx.SessionInfo(parameters=parameters)
        self.__message.session_info = session_info
        return self

    def set_payload(self, payload: dict):
        """Sets the payload of the WebhookResponse object.

        Args:
            payload: The payload to set.

        Returns:
            The WebhookResponse object.
        """
        self.__message.payload = payload
        return self

    def set_transition(self, target: str):
        """Sets the transition of the WebhookResponse object.

        Args:
            target: The target of the transition.

        Returns:
            The WebhookResponse object.
        """
        target_length = len(target.split('/'))
        if target_length == 10:
            self.__message.target_page = target
        elif target_length == 8:
            self.__message.target_flow = target
        return self

    # JSON Encoding methods.  These are primarily for testing and logging.
    def to_dict(self) -> dict:
        """Converts the WebhookResponse object to a dictionary.

        Args:
            None

        Returns:
            A dictionary representation of the WebhookResponse object.
        """
        return MessageToDict(self.__message._pb, including_default_value_fields=True)

    @property
    def as_dict(self) -> dict:
        """Returns the WebhookResponse object as a dictionary.

        Args:
            None

        Returns:
            A dictionary representation of the WebhookResponse object.
        """
        return self.to_dict()
