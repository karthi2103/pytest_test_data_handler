import pytest

from exceptions.email import InvalidEmailException, InvalidMessageBodyException
from service.send_email import send_email
from tests.data_util.data_resolver import inject_test_data


class TestData:
    test_data = inject_test_data(file="email/emailTestSet.json")

    @pytest.mark.parametrize("input", test_data.happyPath)
    def test_email_happy_path(self, input):
        print(input.description)
        response = send_email(input.from_, input.to, input.message)
        assert response.sent
        assert response.error is None

    @pytest.mark.parametrize("input", test_data.invalidEmail)
    def test_email_validation_failed(self, input):
        print(input.description)
        with pytest.raises(InvalidEmailException) as e:
            send_email(input.from_, input.to, input.message)

    @pytest.mark.parametrize("input", test_data.invalidMessage)
    def test_email_body_validation_failed(self, input):
        print(input.description)
        with pytest.raises(InvalidMessageBodyException) as e:
            send_email(input.from_, input.to, input.message)
