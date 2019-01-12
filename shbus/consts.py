from Crypto.Cipher import AES

key = bytes.fromhex('2FD3028E14A45D1F8B6EB0B2ADB7CAAF')
iv = bytes.fromhex('754C8FD584FACF6210376B2B72B063E4')
aes_mode = AES.MODE_CBC
MONITOR_URL = 'http://lbs.jt.sh.cn:8082/app/rls/monitor'