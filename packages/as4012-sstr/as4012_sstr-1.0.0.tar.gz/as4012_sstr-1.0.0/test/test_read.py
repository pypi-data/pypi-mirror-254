from as4012_sstr import reader


def test_read_history(history_fname):
    reader.read_history(history_fname)


def test_read_profile(profile_fname):
    reader.read_profile(profile_fname)


def test_read_index(index_fname):
    reader.find_read_profile(index_fname, 5950)
