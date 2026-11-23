import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)
os.chdir(REPO_ROOT)

import app  # noqa: E402


# main_data.csv stores several titles with a trailing NBSP followed by
# spaces, e.g. 'miami vice\xa0           '.  Lookup in rcmd() used an exact
# match against these untrimmed values, so these movies could never be found.


def test_rcmd_finds_title_stored_with_trailing_whitespace():
    recs = app.rcmd("miami vice")
    assert isinstance(recs, list) and len(recs) > 0


def test_rcmd_strips_whitespace_from_query():
    recs = app.rcmd("  Hannibal\xa0   ")
    assert isinstance(recs, list) and len(recs) > 0


def test_suggestions_have_no_trailing_whitespace():
    suggestions = app.get_suggestions()
    assert all(s == s.strip() for s in suggestions)
