from nose.tools import *
from ex48 import parser


def test_peek():
    assert_equal(parser.peek([('direction', 'north')]), 'direction')
    assert_equal(parser.peek([]), None)

def test_match():
    assert_equal(parser.match([('direction', 'north')], 'direction'),
            ('direction', 'north'))
    assert_equal(parser.match([('noun', 'princess')], 'direction'),
            None)
    assert_equal(parser.match([('noun', 'princess'), ('direction', 'north')],
        'direction'), None)
    assert_equal(parser.match([], 'direction'), None)

def test_skip():
    word_list = [('direction', 'north'), ('direction', 'sound')]
    parser.skip(word_list, 'direction')
    assert_equal(word_list, [])

    word_list2 = [('direction', 'north'), ('noun', 'princess'), ('direction', 'sound')]
    parser.skip(word_list2, 'direction')
    assert_equal(word_list2, [('noun', 'princess'), ('direction', 'sound')])

def test_parse_verb():
    word_list = [('stop', 'the'), ('verb', 'kill')]
    assert_equal(parser.parse_verb(word_list), ('verb', 'kill'))

    word_list2 = [('stop', 'the'), ('noun', 'princess')]
    assert_raises(parser.ParserError, parser.parse_verb, word_list2)
