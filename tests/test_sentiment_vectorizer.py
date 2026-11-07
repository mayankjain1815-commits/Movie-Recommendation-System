import pickle
from pathlib import Path

ARTIFACT = Path(__file__).resolve().parents[1] / "Artifacts" / "tranform.pkl"


def test_vectorizer_can_transform_review_text():
    """The shipped sentiment vectorizer must be fitted, not just pickled.

    It was saved with an older scikit-learn whose ``idf_`` was a property
    backed by ``_idf_diag``. Newer scikit-learn versions (>=1.5) removed that
    property, so unpickling leaves the transformer without the fitted ``idf_``
    attribute and every ``transform()`` call raises NotFittedError.
    """
    with open(ARTIFACT, "rb") as handle:
        vectorizer = pickle.load(handle)

    matrix = vectorizer.transform(
        [
            "This movie was absolutely wonderful and I loved it.",
            "Terrible waste of time, awful acting.",
        ]
    )

    assert matrix.shape == (2, 2011)
    assert matrix.nnz > 0
