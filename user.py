import hashlib
import hmac

admins = {
    'K.Kolbek': {'password': 'admin123', 'role': 'admin'},
    'L.Fischer': {'password': 'admin123', 'role': 'admin'},
    'N.Razafindraibe': {'password': 'admin123', 'role': 'admin'},
    'E.Schaefer': {'password': 'admin123', 'role': 'admin'}
}

birthday = '01.01.2025'

users = {
    '10014729': {'password': f'{birthday}', 'role': 'patient'},
    '10003400': {'password': f'{birthday}', 'role': 'patient'},
    '10002428': {'password': f'{birthday}', 'role': 'patient'},
    '10032725': {'password': f'{birthday}', 'role': 'patient'},
    '10027445': {'password': f'{birthday}', 'role': 'patient'},
    '10022281': {'password': f'{birthday}', 'role': 'patient'},
    '10035631': {'password': f'{birthday}', 'role': 'patient'},
    '10024043': {'password': f'{birthday}', 'role': 'patient'},
    '10025612': {'password': f'{birthday}', 'role': 'patient'},
    '10003046': {'password': f'{birthday}', 'role': 'patient'},
    'D.Paris': {'password': 'test', 'role': 'doktor', 'department': 'radiology'},
    'M.Maier': {'password': 'test', 'role': 'doktor', 'department': 'gastroenterology'},
    'A.Mueller': {'password': 'test', 'role': 'doktor', 'department': 'oncology'}
}