from string_utils import StringUtils

utils = StringUtils()


def test_capitalize():
    assert utils.capitilize("women") == "Women"  # позитиная проверка
    assert utils.capitilize("woMen") == "Women"  # позитиная проверка
    assert utils.capitilize("") == ""  # пустая строка
    assert utils.capitilize("   ") == "   "  # пробелы


def test_trim():
    assert utils.trim("    women") == "women"  # позитиная проверка
    assert utils.trim("") == ""  # пустая строка
    assert utils.trim("   ") == ""  # пробелы


def test_to_list():
    assert utils.to_list("w,o,m,e,n") == ["w", "o", "m", "e", "n"]
    assert utils.to_list("1:2:3:4:5", ":") == ["1", "2", "3", "4", "5"]
    assert utils.to_list("") == []  # пустая строка
    assert utils.to_list(" , , ") == [" ", " ", " "]  # пробелы


def test_contains():
    assert utils.contains("women", "w") is True
    assert utils.contains("women", "a") is False
    assert utils.contains("", "w") is False


def test_delete_symbol():
    assert utils.delete_symbol("women", "w") == "omen"
    assert utils.delete_symbol("women", "wo") == "men"
    assert utils.delete_symbol("", "w") == ""  # пустая строка
    assert utils.delete_symbol("women", "y") == "women"


def test_starts_with():
    assert utils.starts_with("women", "w") is True
    assert utils.starts_with("women", "a") is False


def test_end_with():
    assert utils.end_with("women", "n") is True
    assert utils.end_with("women", "w") is False


def test_is_empty():
    assert utils.is_empty("") is True
    assert utils.is_empty("   ") is True
    assert utils.is_empty("women") is False


def test_list_to_string():
    assert utils.list_to_string([1, 2, 3, 4, 5]) == "1, 2, 3, 4, 5"
    assert utils.list_to_string(["Wo", "Men"]) == "Wo, Men"
    assert utils.list_to_string([]) == ""
    assert utils.list_to_string([""]) == ""
