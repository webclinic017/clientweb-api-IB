# coding: utf-8

"""
    Client Portal Web API

    Production version of the Client Portal Web API  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse200(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'accounts': 'list[str]',
        'aliases': 'object',
        'selected_account': 'str'
    }

    attribute_map = {
        'accounts': 'accounts',
        'aliases': 'aliases',
        'selected_account': 'selectedAccount'
    }

    def __init__(self, accounts=None, aliases=None, selected_account=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501

        self._accounts = None
        self._aliases = None
        self._selected_account = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if aliases is not None:
            self.aliases = aliases
        if selected_account is not None:
            self.selected_account = selected_account

    @property
    def accounts(self):
        """Gets the accounts of this InlineResponse200.  # noqa: E501

        Unique account id  # noqa: E501

        :return: The accounts of this InlineResponse200.  # noqa: E501
        :rtype: list[str]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this InlineResponse200.

        Unique account id  # noqa: E501

        :param accounts: The accounts of this InlineResponse200.  # noqa: E501
        :type: list[str]
        """

        self._accounts = accounts

    @property
    def aliases(self):
        """Gets the aliases of this InlineResponse200.  # noqa: E501

        Account Id and its alias  # noqa: E501

        :return: The aliases of this InlineResponse200.  # noqa: E501
        :rtype: object
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this InlineResponse200.

        Account Id and its alias  # noqa: E501

        :param aliases: The aliases of this InlineResponse200.  # noqa: E501
        :type: object
        """

        self._aliases = aliases

    @property
    def selected_account(self):
        """Gets the selected_account of this InlineResponse200.  # noqa: E501


        :return: The selected_account of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._selected_account

    @selected_account.setter
    def selected_account(self, selected_account):
        """Sets the selected_account of this InlineResponse200.


        :param selected_account: The selected_account of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._selected_account = selected_account

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse200, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
