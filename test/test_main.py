from main.main import merge_lists

def test_normal_output_case():
    lis_1 = [1, 2, 4, 5]
    lis_2 = [6]

    result = merge_lists(lis_1, lis_2)

    assert result == [1, 2, 4, 5, 6]

def test_normal_output_with_negative_case():
    lis_1 = [-30, -10, 0, 15, 16]
    lis_2 = [-20, -5, 5]

    result = merge_lists(lis_1, lis_2)

    assert result == [-30, -20, -10, -5, 0, 5, 15, 16]

def test_empty_list():
    lis_1 = [1, 2, 4, 5]
    lis_2 = []

    result = merge_lists(lis_1, lis_2)

    assert result == lis_1

def test_duplicate_list():
    lis_1 = [-30, -10, -5, 0, 15, 16]
    lis_2 = [-20, -5, 0, 5, 16]

    result = merge_lists(lis_1, lis_2)

    assert result == [-30, -20, -10, -5, -5, 0, 0, 5, 15, 16, 16]

def test_two_empty_list():
    lis_1 = []
    lis_2 = []

    result = merge_lists(lis_1, lis_2)

    assert result == []