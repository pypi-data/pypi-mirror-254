class AnnoworkApiException(Exception):
    """
    annoworkapi に関するException
    """


class CredentialsNotFoundError(AnnoworkApiException):
    """
    Annoworkの認証情報が見つからないときのエラー
    """
