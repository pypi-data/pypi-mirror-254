from datetime import datetime
from typing import List

import boto3
from botocore.exceptions import ClientError
from logger_local.Logger import Logger
from message_local.MessageLocal import MessageLocal
from message_local.Recipient import Recipient
from python_sdk_remote.utilities import our_get_env

SMS_MESSAGE_AWS_SNS_LOCAL_PYTHON_PACKAGE_COMPONENT_ID = 208
SMS_MESSAGE_AWS_SNS_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME = "sms_message_aws_sns_local_python_package"
DEVELOPER_EMAIL = "akiva.s@circ.zone"
logger = Logger.create_logger(object={
    "component_id": SMS_MESSAGE_AWS_SNS_LOCAL_PYTHON_PACKAGE_COMPONENT_ID,
    "component_name": SMS_MESSAGE_AWS_SNS_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME,
    "component_category": "Code",
    "developer_email": DEVELOPER_EMAIL
})

# Set to 4 for testing API Management
SMS_MESSAGE_AWS_SNS_API_TYPE_ID = 6


class SmsMessageAwsSnsLocal(MessageLocal):
    """Assuming the usage is as follows:
    message_local = MessageLocal(...)
    message_local.__class__ = SmsMessageAwsSnsLocal
    message_local.__init__()  # calling the "init" of SmsMessageAwsSnsLocal
    message_local.send(...)  # calling the "send" of SmsMessageAwsSnsLocal
    """

    def __init__(self, sns_resource=boto3.resource("sns")):  # noqa
        # Don't call super().__init__(), we already have the message_local object
        self.sns_resource = sns_resource
        self._api_type_id = SMS_MESSAGE_AWS_SNS_API_TYPE_ID  # used by MessageLocal

    def __create_topic(self, name):
        """
        Creates a notification topic.

        :param name: The name of the topic to create.
        :return: The newly created topic.
        """
        try:
            topic = self.sns_resource.__create_topic(Name=name)
            logger.info("Created topic %s with ARN %s. " % (name, topic.arn))
        except ClientError:
            logger.exception("Couldn't create topic %s." % name)
            raise
        else:
            return topic

    def __publish_text_message(self, phone_number, message) -> int:
        try:
            # TODO: Why commented? We prefer not to push commented code to the repo.
            # if self.can_send(api_data=payload, outgoing_body=payload,
            #               sender_profile_id=self.get_sender_profile_id())):
            response = self.sns_resource.meta.client.publish(
                PhoneNumber=phone_number, Message=message
            )
            # self.after_send_attempt(outgoing_body=payload,
            #     incoming_message = response.json(),
            #     http_status_code = response.status_code,
            #     response_body = response.text)
            message_id = response["MessageId"]
            logger.info("Published message to %s, message id: %s." % (phone_number, message_id))
        except ClientError:
            logger.exception("Couldn't publish message to %s. message: %s" % (phone_number, message))
            raise
        return message_id

    @staticmethod  # TODO: currently not used
    def __publish_message(topic, message, attributes):
        """
        Publishes a message, with attributes, to a topic. Subscriptions can be filtered
        based on message attributes so that a subscription receives messages only
        when specified attributes are present.

        :param topic: The topic to publish to.
        :param message: The message to publish.
        :param attributes: The key-value attributes to attach to the body. Values
                           must be either `str` or `bytes`.
        :return: The ID of the message.
        """
        try:
            att_dict = {}
            for key, value in attributes.items():
                if isinstance(value, str):
                    att_dict[key] = {
                        "DataType": "String", "StringValue": value}
                elif isinstance(value, bytes):
                    att_dict[key] = {
                        "DataType": "Binary", "BinaryValue": value}
            response = topic.publish(
                Message=message, MessageAttributes=att_dict)
            message_id = response["MessageId"]
            logger.info("Published message with attributes %s to topic %s." % (attributes, topic.arn))
        except ClientError:
            logger.exception(
                "Couldn't publish message to topic %s." % topic.arn)
            raise
        else:
            return message_id

    def send(self, body: str = None, compound_message_dict: dict = None, recipients: List[Recipient] = None,
             cc: List[Recipient] = None, bcc: List[Recipient] = None,
             scheduled_timestamp_start: datetime = None,
             scheduled_timestamp_end: datetime = None, **kwargs) -> list[int]:
        """Returns a list of message ids (or 0 if failed) per recipient
        """
        recipients = recipients or self.get_recipients()
        logger.start(object={"body": body, "recipients": recipients,
                             "compound_message_dict": compound_message_dict})
        messages_ids = []
        for recipient in recipients:
            message = body or self.get_body_after_text_template(recipient)
            phone_number = recipient.get_normizalied_phone()
            if phone_number is not None:
                if our_get_env("IS_REALLY_SEND_SMS"):
                    message_id = self.__publish_text_message(phone_number, message)
                else:
                    print(f"SmsMessageAwsSnsLocal.send IS_REALLY_SEND_SMS is off: "
                          f"suppose to send sms to {phone_number} with body {message}")
                    message_id = 0
            else:
                logger.warn(f"recipient.get_canonical_telephone() is None: {recipient}")
                message_id = 0
            messages_ids.append(message_id)
        return messages_ids

    """  # replaced by __publish_text_message?
    # TODO: currently not used
    def __send_sms_using_aws_sms_using_api_getaway(self, phone_number, message):
        example_instance = APIManagementsLocal.get_api
        external_user_id = None
        api_type_id = SMS_MESSAGE_AWS_SNS_API_TYPE_ID
        PRODUCT_USER_IDENTIFIER = our_get_env("PRODUCT_USER_IDENTIFIER")
        PRODUCT_PASSWORD = our_get_env("PRODUCT_PASSWORD")
        # user_context._instance = None
        # url_circlez = OurUrl()
        # authentication_auth_login_endpoint_url = url_circlez.endpoint_url(
        #         brand_name=BRAND_NAME,
        #         environment_name=our_get_env('ENVIRONMENT_NAME'),
        #         component_name=component_name_enum.ComponentName.AUTHENTICATION.value,
        #         entity_name=entity_name_enum.EntityName.AUTH_LOGIN.value,
        #         version=AUTHENTICATION_API_VERSION,
        #         action_name=action_name_enum.ActionName.LOGIN.value
        #         )
        authentication_auth_login_endpoint_url = "AWS SNS"

        data = {"user_identifier": PRODUCT_USER_IDENTIFIER, "password": PRODUCT_PASSWORD}
        headers = {"Content-Type": "application/json"}
        debug_data = {"url": authentication_auth_login_endpoint_url, "data": json.dumps(
            data, separators=(",", ":")), "headers": headers}
        logger.info(json.dumps(debug_data, separators=(",", ":"), indent=4))
        outgoing_body = (PRODUCT_USER_IDENTIFIER, PRODUCT_PASSWORD)
        incoming_message = ""
        response_body = ""
        http_status_code = None
        while http_status_code != http.HTTPStatus.OK.value:
            # TODO Let's move all the API Management code to message-local so we will inherit it in all message classes.
            api_check, api_call_id, arr = example_instance.before_call_api(
                external_user_id=external_user_id,
                api_type_id=api_type_id,
                endpoint=authentication_auth_login_endpoint_url,
                outgoing_header=headers,
                outgoing_body=outgoing_body
            )
            
            if arr is None:
                used_cache = False
                if api_check == APILimitStatus.BETWEEN_SOFT_LIMIT_AND_HARD_LIMIT.value:
                    logger.warn("You passed the soft limit")
                if api_check != APILimitStatus.GREATER_THAN_HARD_LIMIT.value:
                    try:
                        if our_get_env("IS_REALLY_SEND_SMS"):
                            response = self.sns_resource.meta.client.publish(
                                PhoneNumber=phone_number, Message=message
                            )
                            message_id = response["MessageId"]
                            logger.info("Published message to %s, message id: %s." % (phone_number, message_id))
                        else:
                            print(f"SmsMessageAwsSnsLocal.send IS_REALLY_SEND_SMS is off: "
                                  f"suppose to send sms to {phone_number} with body {message}")
                            message_id = 0
                    except ClientError:
                        logger.exception("Couldn't publish message to %s." % phone_number)
                        raise
                    else:
                        http_status_code = http.HTTPStatus.OK.value
                else:
                    print(" You passed the hard limit")
                    seconds_to_sleep_after_passing_the_hard_limit = APIManagementsLocal.seconds_to_sleep_after_passing_the_hard_limit(api_type_id=api_type_id)
                    if seconds_to_sleep_after_passing_the_hard_limit > 0:
                        print("sleeping : " + str(seconds_to_sleep_after_passing_the_hard_limit) + " seconds")
                        time.sleep(seconds_to_sleep_after_passing_the_hard_limit)
                        # raise PassedTheHardLimitException

                    else:
                        print("No sleeping needed : seconds_to_sleep_after_passing_the_hard_limit= " + str(seconds_to_sleep_after_passing_the_hard_limit) + " seconds")
            else:
                used_cache = True
                print("result from cache")
                print(arr)
                http_status_code = http.HTTPStatus.OK.value
            example_instance.after_call_api(
                external_user_id=external_user_id,
                api_type_id=api_type_id,
                endpoint=authentication_auth_login_endpoint_url, outgoing_header=headers,
                outgoing_body=outgoing_body,
                incoming_message=incoming_message,
                http_status_code=http_status_code,
                response_body=response_body, api_call_id=api_call_id, used_cache=used_cache)
    """
