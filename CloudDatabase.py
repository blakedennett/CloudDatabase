import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from google.cloud import storage

# "project_id": "cloud-database-69f2b"

key = {
  "type": "service_account",
  "project_id": "cloud-database-69f2b",
  "private_key_id": "78dfe8aee0e087b5fd821fae30dba22531abacf9",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDbtDPn6tbQx0FC\n5/5QGP+5GV7/aj1ucrQhDWdYTxod4FepDXOsgmu6yI7HAa/zdHJWaz83eheugm5G\nMAwpQIl13p0W2OA51lzZXCBw+NU+l8nOQlhWnOUdep7+EW714rFWo3Ll1MLWxoKP\npYqSS3HD26I9pqFZGqZdTNwEcjgIKxf2FSCxEkqOjWlsY6Lhi6Ps2vu7Pbwm/pNB\n/Xyar0F6aSD/uTa66mGty7hg3NPvnpMvl2hVEPTpQo+51vGEiaUZAhZCZU19vuN0\naQy/da1vcgHFHTw5gRI3SrT/VP50wEk/TkR4BptgdS/86cYHFWThUTJhQQFmaqBt\nwGXb/9j7AgMBAAECggEAGr5VQSpHatOOYKAPx107p6LseufKQYsJ3SoeBdRfJ/ra\ngNQH3BxmE679HkFY0yg+EMHuSIj+n/n1hWqs2EqoUOY/tfvBU5kB5V1+/3Fyt7NP\nV+Ggki53/z4hY2jo2lp1Xsf3oP1kmDNCykyK0SMI3p/6IEoLwuZpENtdvtbOdkPa\n36yEPr4FqJzGQ0Xr3Rp6Bfm1g4i1+RShRHq+8kjecHLRKnRJZwgab7csfVga17Nf\n9a4FQeby6o9RCOsqAh+yqwDbCjU5A/e1LEv1L8q56saJ2Ssk84aEzgZmfH2b8t7e\n2lhEyGcwbzdEyWmFd68MwbSVuo8dc9CNcOGUjTt0jQKBgQDx7YyBuo898WnOFubP\nxDE5SUV+dDg3wiyvEcEWhZJMxqCh88lLsNX39i4b/MvqfRdFThANvJjodu1mhD6L\nycYY7XcztxX755bbPz+L6lHIkmcBiLynSnP2wyqcu5kLPRdnAGMTX95E+t0zR1Iy\no1h0al/iAF560A/iMTbAc6rOhwKBgQDoe7mkM44XbIZFsxbF9PTpOHWPViD8d1lE\n21c6hNt38PR9BCglFJbQDxL5c7kbYtRU7EuvH7DOWghqAhFpfaxmrqWAnmUmIVc3\nXTj8wdMdujHDEK/G1CT84uDYMywr8AYlnMNEdI/2Tj3UWZyNuBYzRLHC52mHcKHY\nzzCAZb+q7QKBgBuTRgaraxRWZgb1mU1pQWsULPWi7Z19ZnZ2AZo9k1Vo9no/PVyB\nRYJD7zGFeQC7TWG66h2Gt68Xjyu2OyLX1tqUhpfAcKML3KgU53tdNAE2nsMQAODY\nnassx7ihsWoUhoxZAPH+ZWlbZscng/j9oWFzloY+IIbDHGxdy63YAUoVAoGBAJx2\noIMVO30iSd/g3uPNr4LCv8P/GGYxwL+pyzQUNEytuy3kPUxvZeyTKJcAPkVjJzoc\nafdroafPSjhmOefAb+YPhk1gzPxzleop8G+T1wz7wf/hXBu5rUcRPnfjQMg1Wz23\nGmgY9say88PVp5ptmWtZwTVGX2yK7jInhyHy2KMlAoGBANG+s/plM2ryChBtt3RW\npbkO+gJ6Z7/O/KP90kNSDaMyAbRiYN/hw7mQ7KRwZqP9XCwj7VLd/2KVbSdYsHP8\nqwMCPplqn+ofo+xGpTWbje0g06vssBe3Lb2jmFWaPI3HpYtcSSwMllJQ+Z4oeVEF\nS+nT+fLsK9WRYvdV/UimRaDi\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-74ql6@cloud-database-69f2b.iam.gserviceaccount.com",
  "client_id": "101214003603621301606",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-74ql6%40cloud-database-69f2b.iam.gserviceaccount.com"
}

# Application Default credentials are automatically created.
cred = credentials.Certificate(key)
firebase_admin.initialize_app(cred)


db = firestore.client()




w1 = {
    'date': 512023
}

w2 = {
    'date': 4282023
}

data = [w1, w2]

for record in data:
    rec = db.collection(r'C:\Users\Blake Dennett\Downloads\Spring2023\appliedProgramming\CloudDatabase').document('dat')
    rec.set(record)
