from google.cloud import dialogflowcx as cx
from google.protobuf.json_format import ParseDict
from google.protobuf.json_format import MessageToDict
from google.protobuf.struct_pb2 import Struct

# 2023-12-11 
# - Now with docstrings!

# 2023-12-01
# - Dialogflow CX WebhookRequest object has changed with breaking changes
# - addition of "query" helper method to work through incoming payloads created.

# 2023-10-28
# - Replacement of self.request with self.__message to represent the proto message
# - Addition of __getattr__ which fetches from the self.__message now

class WebhookRequest:

    """A facade representing the Dialogflow CX WebhookRequest object.

    This class provides a convenient way to access the fields of a
    WebhookRequest object.

    Args:
        body: A dictionary representing the JSON payload of the webhook request.
    """

    def __init__(self, body: dict = {}):
        self.__message = cx.WebhookRequest()
        # When a webhook comes in as JSON, we use ParseDict to convert JSON to Protobuf
        ParseDict(body, self.__message._pb, ignore_unknown_fields=True)
        self.__query = None
        self.__origin = None

    # gRPC Message attributes exposed as properties;
    # Easier on traditional linters and formatters.

    @property
    def detect_intent_response_id(self) -> str:
        """The unique identifier of the DetectIntentResponse that this webhook
        request is derived from.

        Returns:
            A string representing the unique identifier of the DetectIntentResponse.
        """
        return self.__message.detect_intent_response_id

    @property
    def language_code(self) -> str:
        """The language code of the query that the agent received.

        Returns:
            A string representing the language code of the query.
        """
        return self.__message.language_code

    @property
    def fulfillment_info(self) -> cx.WebhookRequest.FulfillmentInfo:
        """Information about the fulfillment that triggered this webhook call.

        Returns:
            A FulfillmentInfo object representing the fulfillment information.
        """
        return self.__message.fulfillment_info

    @property
    def intent_info(self) -> cx.WebhookRequest.IntentInfo:
        """Information about the intent matched by the agent.

        Returns:
            An IntentInfo object representing the intent information.
        """
        return self.__message.intent_info

    @property
    def session_info(self) -> cx.SessionInfo:
        """Information about the session for which this webhook request is made.

        Returns:
            A SessionInfo object representing the session information.
        """
        return self.__message.session_info

    @property
    def messages(self) -> list:
        """The list of messages that the agent has sent to the user.

        Returns:
            A list of Message objects representing the messages.
        """
        return self.__message.messages

    @property
    def payload(self) -> Struct:
        """The payload of the webhook request.

        Returns:
            A Struct object representing the payload.
        """
        return self.__message.payload

    @property
    def sentiment_analysis_result(self) -> cx.SentimentAnalysisResult:
        """The sentiment analysis result of the query.

        Returns:
            A SentimentAnalysisResult object representing the sentiment analysis result.
        """
        return self.__message.sentiment_analysis_result

    # Helper properties.  These class properties make basic access easier
    @property
    def tag(self) -> str:
        """The tag of the fulfillment that triggered this webhook call.

        Returns:
            A string representing the tag of the fulfillment.
        """
        return self.__message.fulfillment_info.tag

    @property
    def session(self) -> str:
        """The name of the session for which this webhook request is made.

        Returns:
            A string representing the name of the session.
        """
        return self.__message.session_info.session

    @property
    def session_id(self) -> str:
        """The unique identifier of the session for which this webhook request is made.

        Returns:
            A string representing the unique identifier of the session.
        """
        return self.session.split('/')[-1]

    @property
    def session_parameters(self):
        """The session parameters for this webhook request.

        Returns:
            A dictionary representing the parameters of the session.
        """
        return MessageToDict(
            self.__message.session_info._pb,
            including_default_value_fields=True,
        ).get('parameters')

    @property
    def query(self):
        """The query that the user sent to the agent.

        Returns:
            A tuple containing the query and the origin of the query.
        """
        if self.__query and self.__origin:
            return self.__query, self.__origin

        r = self.__message

        # q is for query, o is for origin
        q, o = '', ''
        if r.text:
            q = r.text
            o = 'text'
        elif r.trigger_event:
            q = r.trigger_intent
            o = 'trigger_intent'
        elif r.transcript:
            q = r.transcript
            o = 'transcript'
        elif r.trigger_event:
            q = r.trigger_event
            o = 'trigger_event'
        elif r.dtmf_digits:
            q = r.dtmf_digits
            o = 'dtmf_digits'
        else:
            ...

        self.__query = q
        self.__origin = o
        return self.__query, self.__origin

    @property
    def origin(self) -> str:
        """The origin of the query that the user sent to the agent.

        Returns:
            A string representing the origin of the query.
        """
        if not self.__origin:
            self.query
        return self.__origin

    # JSON Encoding methods.  These are primarily for testing and logging.
    def to_dict(self) -> dict:
        """Converts the WebhookRequest object to a dictionary.

        Returns:
            A dictionary representing the WebhookRequest object.
        """
        return MessageToDict(self.__message._pb, including_default_value_fields=True)

    @property
    def as_dict(self) -> dict:
        """Returns the WebhookRequest object as a dictionary.

        Returns:
            A dictionary representing the WebhookRequest object.
        """
        return self.to_dict()