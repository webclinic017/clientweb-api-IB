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


class HistoryData(object):
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
        'start': 'str',
        'md_availability': 'str',
        'bar_length': 'int',
        'delay': 'int',
        'high': 'str',
        'low': 'str',
        'symbol': 'str',
        'text': 'str',
        'tick_num': 'str',
        'time_period': 'str',
        'data': 'list[HistorydataData]',
        'points': 'float',
        'travel_time': 'float'
    }

    attribute_map = {
        'start': 'start',
        'md_availability': 'mdAvailability',
        'bar_length': 'barLength',
        'delay': 'delay',
        'high': 'high',
        'low': 'low',
        'symbol': 'symbol',
        'text': 'text',
        'tick_num': 'tickNum',
        'time_period': 'timePeriod',
        'data': 'data',
        'points': 'points',
        'travel_time': 'travelTime'
    }

    def __init__(self, start=None, md_availability=None, bar_length=None, delay=None, high=None, low=None, symbol=None, text=None, tick_num=None, time_period=None, data=None, points=None, travel_time=None):  # noqa: E501
        """HistoryData - a model defined in Swagger"""  # noqa: E501

        self._start = None
        self._md_availability = None
        self._bar_length = None
        self._delay = None
        self._high = None
        self._low = None
        self._symbol = None
        self._text = None
        self._tick_num = None
        self._time_period = None
        self._data = None
        self._points = None
        self._travel_time = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if md_availability is not None:
            self.md_availability = md_availability
        if bar_length is not None:
            self.bar_length = bar_length
        if delay is not None:
            self.delay = delay
        if high is not None:
            self.high = high
        if low is not None:
            self.low = low
        if symbol is not None:
            self.symbol = symbol
        if text is not None:
            self.text = text
        if tick_num is not None:
            self.tick_num = tick_num
        if time_period is not None:
            self.time_period = time_period
        if data is not None:
            self.data = data
        if points is not None:
            self.points = points
        if travel_time is not None:
            self.travel_time = travel_time

    @property
    def start(self):
        """Gets the start of this HistoryData.  # noqa: E501

        start date time  # noqa: E501

        :return: The start of this HistoryData.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this HistoryData.

        start date time  # noqa: E501

        :param start: The start of this HistoryData.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def md_availability(self):
        """Gets the md_availability of this HistoryData.  # noqa: E501

        Market Data Availability. The field may contain two chars. The first char is the primary code: R = Realtime, D = Delayed, Z = Frozen, Y = Frozen Delayed. The second char is the secondary code: P = Snapshot Available, p = Consolidated.   # noqa: E501

        :return: The md_availability of this HistoryData.  # noqa: E501
        :rtype: str
        """
        return self._md_availability

    @md_availability.setter
    def md_availability(self, md_availability):
        """Sets the md_availability of this HistoryData.

        Market Data Availability. The field may contain two chars. The first char is the primary code: R = Realtime, D = Delayed, Z = Frozen, Y = Frozen Delayed. The second char is the secondary code: P = Snapshot Available, p = Consolidated.   # noqa: E501

        :param md_availability: The md_availability of this HistoryData.  # noqa: E501
        :type: str
        """

        self._md_availability = md_availability

    @property
    def bar_length(self):
        """Gets the bar_length of this HistoryData.  # noqa: E501


        :return: The bar_length of this HistoryData.  # noqa: E501
        :rtype: int
        """
        return self._bar_length

    @bar_length.setter
    def bar_length(self, bar_length):
        """Sets the bar_length of this HistoryData.


        :param bar_length: The bar_length of this HistoryData.  # noqa: E501
        :type: int
        """

        self._bar_length = bar_length

    @property
    def delay(self):
        """Gets the delay of this HistoryData.  # noqa: E501


        :return: The delay of this HistoryData.  # noqa: E501
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this HistoryData.


        :param delay: The delay of this HistoryData.  # noqa: E501
        :type: int
        """

        self._delay = delay

    @property
    def high(self):
        """Gets the high of this HistoryData.  # noqa: E501

        price/volume/...  # noqa: E501

        :return: The high of this HistoryData.  # noqa: E501
        :rtype: str
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this HistoryData.

        price/volume/...  # noqa: E501

        :param high: The high of this HistoryData.  # noqa: E501
        :type: str
        """

        self._high = high

    @property
    def low(self):
        """Gets the low of this HistoryData.  # noqa: E501

        price/volume/...  # noqa: E501

        :return: The low of this HistoryData.  # noqa: E501
        :rtype: str
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this HistoryData.

        price/volume/...  # noqa: E501

        :param low: The low of this HistoryData.  # noqa: E501
        :type: str
        """

        self._low = low

    @property
    def symbol(self):
        """Gets the symbol of this HistoryData.  # noqa: E501


        :return: The symbol of this HistoryData.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this HistoryData.


        :param symbol: The symbol of this HistoryData.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def text(self):
        """Gets the text of this HistoryData.  # noqa: E501


        :return: The text of this HistoryData.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this HistoryData.


        :param text: The text of this HistoryData.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def tick_num(self):
        """Gets the tick_num of this HistoryData.  # noqa: E501


        :return: The tick_num of this HistoryData.  # noqa: E501
        :rtype: str
        """
        return self._tick_num

    @tick_num.setter
    def tick_num(self, tick_num):
        """Sets the tick_num of this HistoryData.


        :param tick_num: The tick_num of this HistoryData.  # noqa: E501
        :type: str
        """

        self._tick_num = tick_num

    @property
    def time_period(self):
        """Gets the time_period of this HistoryData.  # noqa: E501


        :return: The time_period of this HistoryData.  # noqa: E501
        :rtype: str
        """
        return self._time_period

    @time_period.setter
    def time_period(self, time_period):
        """Sets the time_period of this HistoryData.


        :param time_period: The time_period of this HistoryData.  # noqa: E501
        :type: str
        """

        self._time_period = time_period

    @property
    def data(self):
        """Gets the data of this HistoryData.  # noqa: E501


        :return: The data of this HistoryData.  # noqa: E501
        :rtype: list[HistorydataData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this HistoryData.


        :param data: The data of this HistoryData.  # noqa: E501
        :type: list[HistorydataData]
        """

        self._data = data

    @property
    def points(self):
        """Gets the points of this HistoryData.  # noqa: E501

        total number of points  # noqa: E501

        :return: The points of this HistoryData.  # noqa: E501
        :rtype: float
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this HistoryData.

        total number of points  # noqa: E501

        :param points: The points of this HistoryData.  # noqa: E501
        :type: float
        """

        self._points = points

    @property
    def travel_time(self):
        """Gets the travel_time of this HistoryData.  # noqa: E501


        :return: The travel_time of this HistoryData.  # noqa: E501
        :rtype: float
        """
        return self._travel_time

    @travel_time.setter
    def travel_time(self, travel_time):
        """Sets the travel_time of this HistoryData.


        :param travel_time: The travel_time of this HistoryData.  # noqa: E501
        :type: float
        """

        self._travel_time = travel_time

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
        if issubclass(HistoryData, dict):
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
        if not isinstance(other, HistoryData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other