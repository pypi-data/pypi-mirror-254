import os

PYTHON_SDK_LOCAL_COMPONENT_ID = 184
PYTHON_SDK_LOCAL_COMPONENT_NAME = 'python_sdk_local'

ENVIRONMENT_NAME = os.getenv("ENVIRONMENT_NAME")
BRAND_NAME = os.getenv("BRAND_NAME")
LOGZIO_TOKEN = os.getenv("LOGZIO_TOKEN")
# TODO Shall Can we use python-sdk function to get the value from Environment?
# TODO Shall we get the value from environment here of send the value to the function as @akiva-skolnik did?
GOOGLE_PORT_FOR_AUTHENTICATION = os.getenv("PORT_FOR_AUTHENTICATION")

# dummy jwt for testing
TEST_USER_JWT = (
    'eyJhbGciObJIUzI1NiIsImR5cCI4DkpXWCJ9.'
    'eyJlbWFpbCI6ImR1bW15QGVtYWlsLmNvbSIsInVzZXJJZCI'
    '6IjEyMzQ1Njc4IiwicHJvZmlsZUlkIjoiMTIzNDU2NzgiLCJy'
    'b2xlcyI6WyJVU0VSIl0sImlhdCI6MTYxNTI0ODQ2MSwiZXhwIjoxNjE1MjUyMDYxfQ.'
    'SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
)