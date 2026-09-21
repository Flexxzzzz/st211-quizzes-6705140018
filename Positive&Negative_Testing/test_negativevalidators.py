import pytest
from validators import validate_age, validate_email

def test_email_without_at_rejected():
    with pytest.raises(ValueError):
        validate_email("notanemail.com")

def test_email_without_domain_rejected():
    with pytest.raises(ValueError):
        validate_email("user@")

def test_negative_age_rejected():
    with pytest.raises(ValueError):
        validate_age(-5)

def test_negative_string_rejected():
    with pytest.raises(TypeError):
        validate_age("twenty")


