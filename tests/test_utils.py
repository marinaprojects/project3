import pytest
from src.utils import *


def test_get_executed_operation():
    assert get_executed_operation([{"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]
    assert get_executed_operation([{}]) == []


def test_sort_operations_date():
    assert sort_operations_date([{"date": "2019-07-03T18:35:29.512364"},
                                 {"date": "2018-06-30T02:08:58.425572"},
                                 {"date": "2018-03-23T10:45:06.972075"},
                                 {"date": "2019-04-04T23:20:05.206878"},
                                 {"date": "2018-12-20T16:43:26.929246"},
                                 {"date": "2018-08-19T04:27:37.904916"}]) == [{'date': '2019-07-03T18:35:29.512364'},
                                                                             {'date': '2019-04-04T23:20:05.206878'},
                                                                             {'date': '2018-12-20T16:43:26.929246'},
                                                                             {'date': '2018-08-19T04:27:37.904916'},
                                                                             {'date': '2018-06-30T02:08:58.425572'}]


def test_change_data():
    assert change_data([{"date": "2019-07-03T18:35:29.512364"}]) == ["03.07.2019"]


def test_mask_card_number():
    assert mask_card_number([{"from": "Visa Platinum 1246377376343588",
                              "description": "Перевод организации"}]) == ["Visa Platinum 1246 37** **** 3588"]


def test_mask_amount_number():
    assert mask_amount_number([{ "to": "Счет 84163357546688983493"}]) == ["**8349"]