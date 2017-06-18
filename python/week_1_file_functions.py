import os


def main():
    path = get_dir('./files')
    files = get_files(path)
    renamed = translate_list(files, '0123456789')
    perform_rename(path, files, renamed)


def get_dir(path: str) -> str:
    '''
    Adds a trailing slash to the file path so it can be used to
    append files
    '''
    return os.path.abspath(os.path.realpath(path)) + '/'


def test_get_dir():
    assert get_dir("./foo") == os.getcwd() + '/foo/'


def get_files(file_path: str) -> list:
    return os.listdir(get_dir(file_path))


def test_get_files():
    '''
    This does not use any code of my own, only python native code.
    There's a rule that says "Don't test what you don't own".
    Since I don't own this code, there isn't any point in testing it in
    a unit test.  There are special tests called functional and acceptance
    tests that deal with testing other people's code.
    '''
    pass


def translate_list(names: list, strip=None) -> list:
    '''
    Given a list of strings, using the strip argument to remove
    those values from the string
    '''
    name_list = []
    for name in names:
        cleaned = name.translate({ord(k): None for k in strip})
        name_list.append(cleaned)
    return name_list


def test_translate_list():
    test_list = ['foo1bar', 'aaa', '1324b']
    stripped_list = translate_list(test_list, '0123456789')
    assert stripped_list == ['foobar', 'aaa', 'b']


def perform_rename(path: str, old: list, new: list) -> None:
    '''
    Given a path, change the old files to the new file names
    '''
    old_total = len(old)
    new_total = len(new)
    if old_total != new_total:
        raise IndexError(
            "the number of old items must match the number of new items"
        )
    for i in range(0, old_total):
        os.rename(path + old[i], path + new[i])


if __name__ == '__main__':
    main()
