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


class SummaryTotal(object):
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
        'chg': 'str',
        'rtn': 'str',
        'incomplete_data': 'bool',
        'end_val': 'str',
        'start_val': 'str'
    }

    attribute_map = {
        'chg': 'chg',
        'rtn': 'rtn',
        'incomplete_data': 'incompleteData',
        'end_val': 'endVal',
        'start_val': 'startVal'
    }

    def __init__(self, chg=None, rtn=None, incomplete_data=None, end_val=None, start_val=None):  # noqa: E501
        """SummaryTotal - a model defined in Swagger"""  # noqa: E501

        self._chg = None
        self._rtn = None
        self._incomplete_data = None
        self._end_val = None
        self._start_val = None
        self.discriminator = None

        if chg is not None:
            self.chg = chg
        if rtn is not None:
            self.rtn = rtn
        if incomplete_data is not None:
            self.incomplete_data = incomplete_data
        if end_val is not None:
            self.end_val = end_val
        if start_val is not None:
            self.start_val = start_val

    @property
    def chg(self):
        """Gets the chg of this SummaryTotal.  # noqa: E501

        total change amount  # noqa: E501

        :return: The chg of this SummaryTotal.  # noqa: E501
        :rtype: str
        """
        return self._chg

    @chg.setter
    def chg(self, chg):
        """Sets the chg of this SummaryTotal.

        total change amount  # noqa: E501

        :param chg: The chg of this SummaryTotal.  # noqa: E501
        :type: str
        """

        self._chg = chg

    @property
    def rtn(self):
        """Gets the rtn of this SummaryTotal.  # noqa: E501

        change percent  # noqa: E501

        :return: The rtn of this SummaryTotal.  # noqa: E501
        :rtype: str
        """
        return self._rtn

    @rtn.setter
    def rtn(self, rtn):
        """Sets the rtn of this SummaryTotal.

        change percent  # noqa: E501

        :param rtn: The rtn of this SummaryTotal.  # noqa: E501
        :type: str
        """

        self._rtn = rtn

    @property
    def incomplete_data(self):
        """Gets the incomplete_data of this SummaryTotal.  # noqa: E501

        set to true if any external account data is not available for starting or ending date, resulting in potentially unusual total values.  # noqa: E501

        :return: The incomplete_data of this SummaryTotal.  # noqa: E501
        :rtype: bool
        """
        return self._incomplete_data

    @incomplete_data.setter
    def incomplete_data(self, incomplete_data):
        """Sets the incomplete_data of this SummaryTotal.

        set to true if any external account data is not available for starting or ending date, resulting in potentially unusual total values.  # noqa: E501

        :param incomplete_data: The incomplete_data of this SummaryTotal.  # noqa: E501
        :type: bool
        """

        self._incomplete_data = incomplete_data

    @property
    def end_val(self):
        """Gets the end_val of this SummaryTotal.  # noqa: E501


        :return: The end_val of this SummaryTotal.  # noqa: E501
        :rtype: str
        """
        return self._end_val

    @end_val.setter
    def end_val(self, end_val):
        """Sets the end_val of this SummaryTotal.


        :param end_val: The end_val of this SummaryTotal.  # noqa: E501
        :type: str
        """

        self._end_val = end_val

    @property
    def start_val(self):
        """Gets the start_val of this SummaryTotal.  # noqa: E501


        :return: The start_val of this SummaryTotal.  # noqa: E501
        :rtype: str
        """
        return self._start_val

    @start_val.setter
    def start_val(self, start_val):
        """Sets the start_val of this SummaryTotal.


        :param start_val: The start_val of this SummaryTotal.  # noqa: E501
        :type: str
        """

        self._start_val = start_val

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
        if issubclass(SummaryTotal, dict):
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
        if not isinstance(other, SummaryTotal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
