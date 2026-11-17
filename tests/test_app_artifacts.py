import os
import sys

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO_ROOT)
os.chdir(REPO_ROOT)

import app  # noqa: E402


def test_artifacts_load():
    assert app.clf is not None, "nlp_model.pkl failed to load"
    assert app.vectorizer is not None, "tranform.pkl failed to load"


def test_create_similarity():
    data, similarity = app.create_similarity()
    assert data is not None and similarity is not None
    assert "comb" in data.columns
    assert similarity.shape[0] == len(data)


def test_get_suggestions():
    suggestions = app.get_suggestions()
    assert isinstance(suggestions, list) and len(suggestions) > 0
    assert all(isinstance(s, str) for s in suggestions)


def test_rcmd_returns_recommendations():
    recs = app.rcmd("avatar")
    assert isinstance(recs, list) and len(recs) > 0
