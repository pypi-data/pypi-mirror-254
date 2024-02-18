from .constants import BRAND_NAME, ENVIRONMENT_NAME, LOGZIO_TOKEN


# TODO: I think this should be in logger-local, not here (akiva)
# TODO Align with https://github.com/circles-zone/typescript-sdk-remote-typescript-package/edit/dev/typescript-sdk/src/utils/index.ts validateTenantEnvironmentVariables()  # noqa501
def validate_enviroment_variables(brand_name: str = BRAND_NAME, environment_name: str = ENVIRONMENT_NAME,
                                  logzio_token: str = LOGZIO_TOKEN):
    validate_brand_name(brand_name)
    validate_environment_name(environment_name)
    # if(os.getenv("PRODUCT_USER_IDENTIFIER") is None):
    #     raise Exception("logger-local-python-package LoggerLocal.py please add Environment Variable called "
    #                     "PRODUCT_USER_IDENTIFIER (instead of PRODUCT_USERNAME)")
    # removed by Idan because it dont has to be in every project
    # if(os.getenv("PRODUCT_PASSWORD") is None):
    #     raise Exception("logger-local-python-package LoggerLocal.py please add Environment Variable called PRODUCT_PASSWORD")
    validate_logzio_token(logzio_token)


def validate_environment_name(environment_name: str = ENVIRONMENT_NAME):
    if environment_name is None:
        raise Exception(
            "logger-local-python-package LoggerLocal.py in case of Play1 environment, please add Environment Variable called "
            "ENVIRONMENT_NAME=local or play1 (instead of ENVIRONMENT)")


def validate_brand_name(brand_name: str = BRAND_NAME):
    if brand_name is None:
        raise Exception(
            "logger-local-python-package LoggerLocal.py please add Environment Variable called BRAND_NAME=Circlez")


def validate_logzio_token(logzio_token: str = LOGZIO_TOKEN):
    if logzio_token is None:
        raise Exception("logger-local-python-package LoggerLocal.py please add Environment Variable called"
                        " LOGZIO_TOKEN=cXNHuVkkffkilnkKzZlWExECRlSKqopE")
