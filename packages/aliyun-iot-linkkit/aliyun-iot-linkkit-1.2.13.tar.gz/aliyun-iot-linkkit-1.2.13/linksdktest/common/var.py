'''**************************三元组信息*********************************'''
HOST_NAME_IOT = "cn-shanghai"
PRODUCT_KEY_IOT = ""
DEVICE_NAME_IOT = ""
DEVICE_SECRET_IOT = ""
PRODUCT_SECRET_IOT = ""
TOPIC_IOT = ""
TOPIC_IOT_GET = ""

HOST_NAME_LIVING = "cn-shanghai"
PRODUCT_KEY_LIVING = "a1K1YKPvdRn"
DEVICE_NAME_LIVING = "SDK-PY-TEST_02"
DEVICE_SECRET_LIVING = "f9KcXZqDW3Y6w2qsCxzZjinQRD8EBLYq"
PRODUCT_SECRET_LIVING = "bdUZd0qmIppC5xBc"

HOST_NAME_RAW = ""
PRODUCT_KEY_RAW = ""
DEVICE_NAME_RAW = ""
DEVICE_SECRET_RAW = ""

HOST_NAME_GLOBLE = ""
PRODUCT_KEY_GLOBLE = ""
DEVICE_NAME_GLOBLE = ""
DEVICE_SECRET_GLOBLE = ""

'''**************************字符串长度*********************************'''
STR_LEN_NULL = ''
STR_LEN_1 = 'a'
STR_LEN_4 = 'a'*4
STR_LEN_32 = 'a'*32
STR_LEN_128 = 'a'*128
STR_LEN_129 = 'a'*129
STR_LEN_160 = 'a'*160
STR_LEN_161 = 'a'*161


'''**************************CA证书*********************************'''
ALIYUN_BROKER_CA_DATA = "\
-----BEGIN CERTIFICATE-----\n\
MIIDdTCCAl2gAwIBAgILBAAAAAABFUtaw5QwDQYJKoZIhvcNAQEFBQAwVzELMAkG\
A1UEBhMCQkUxGTAXBgNVBAoTEEdsb2JhbFNpZ24gbnYtc2ExEDAOBgNVBAsTB1Jv\
b3QgQ0ExGzAZBgNVBAMTEkdsb2JhbFNpZ24gUm9vdCBDQTAeFw05ODA5MDExMjAw\
MDBaFw0yODAxMjgxMjAwMDBaMFcxCzAJBgNVBAYTAkJFMRkwFwYDVQQKExBHbG9i\
YWxTaWduIG52LXNhMRAwDgYDVQQLEwdSb290IENBMRswGQYDVQQDExJHbG9iYWxT\
aWduIFJvb3QgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDaDuaZ\
jc6j40+Kfvvxi4Mla+pIH/EqsLmVEQS98GPR4mdmzxzdzxtIK+6NiY6arymAZavp\
xy0Sy6scTHAHoT0KMM0VjU/43dSMUBUc71DuxC73/OlS8pF94G3VNTCOXkNz8kHp\
1Wrjsok6Vjk4bwY8iGlbKk3Fp1S4bInMm/k8yuX9ifUSPJJ4ltbcdG6TRGHRjcdG\
snUOhugZitVtbNV4FpWi6cgKOOvyJBNPc1STE4U6G7weNLWLBYy5d4ux2x8gkasJ\
U26Qzns3dLlwR5EiUWMWea6xrkEmCMgZK9FGqkjWZCrXgzT/LCrBbBlDSgeF59N8\
9iFo7+ryUp9/k5DPAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNVHRMBAf8E\
BTADAQH/MB0GA1UdDgQWBBRge2YaRQ2XyolQL30EzTSo//z9SzANBgkqhkiG9w0B\
AQUFAAOCAQEA1nPnfE920I2/7LqivjTFKDK1fPxsnCwrvQmeU79rXqoRSLblCKOz\
yj1hTdNGCbM+w6DjY1Ub8rrvrTnhQ7k4o+YviiY776BQVvnGCv04zcQLcFGUl5gE\
38NflNUVyRRBnMRddWQVDf9VMOyGj/8N7yy5Y0b2qvzfvGn9LhJIZJrglfCm7ymP\
AbEVtQwdpf5pLGkkeB6zpxxxYu7KyJesF12KwvhHhm4qxFYxldBniYUr+WymXUad\
DKqC5JlR3XC321Y9YeRq4VzW9v493kHMB65jUr9TU/Qr6cf9tveCX4XSQRjbgbME\
HMUfpIBvFSDJ3gyICh3WZlXi/EjJKSZp4A==\n\
-----END CERTIFICATE-----"
ALIYUN_BROKER_CA_DATA_ERROR = '123'

'''**************************抛出异常*********************************'''
EXCEPTION = Exception('without Error throw')
EXCEPTION_CALLBACK = Exception('without callback')


'''**************************返回结果*********************************'''
RESULT_SUCCESS = 0
RESULT_FAIL = 1


'''**************************日志格式*********************************'''
LOG_FORMAT = {'format': '%(asctime)s-%(process)d-%(thread)d - %(name)s:%(module)s:%(funcName)s - %(levelname)s - %(message)s'}


'''**************************TSL*********************************'''
TSL_EVENT = 'Error'
TSL_PATH = 'D:/PyCharm Community Edition 2018.1.3/testcase/common/tsl.json'
TSL_PATH_ERROR_PATH = 'error_path'
TSL_PATH_ERROR_FORMAT = 'D:/PyCharm Community Edition 2018.1.3/testcase/common/tsl_error.json'


'''**************************LOOP TIMES*********************************'''
LOOP_TIMES_10 = 10
LOOP_TIMES_100 = 100
LOOP_TIMES_1000 = 1000
SLEEP_TIME_01 = 0.1
THREAD_COUNT_2 = 2
