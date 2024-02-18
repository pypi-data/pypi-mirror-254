from rdflib import Graph, Literal, URIRef

from nanopub import Nanopub, namespaces
from nanopub.client import DUMMY_NAMESPACE
from nanopub.sign_utils import add_signature
from tests.conftest import default_conf, java_wrap, profile_test


def test_nanopub_sign():
    expected_np_uri = "http://purl.org/np/RAoXkQkJe_lpMhYW61Y9mqWDHa5MAj1o4pWIiYLmAzY50"

    assertion = Graph()
    assertion.add((
        URIRef('http://test'), namespaces.HYCL.claims, Literal('This is a test of nanopub-python')
    ))

    np = Nanopub(
        conf=default_conf,
        assertion=assertion
    )
    java_np = java_wrap.sign(np)

    signed_g = add_signature(
        np.rdf,
        profile_test,
        DUMMY_NAMESPACE,
        np.pubinfo
    )
    np.update_from_signed(signed_g)
    assert np.source_uri == expected_np_uri
    assert np.source_uri == java_np
