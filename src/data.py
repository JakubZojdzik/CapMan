import base64
import os
from hashlib import sha256
from shutil import rmtree

data_files = {}
creators = {}
fixed_salt = base64.b16encode(os.urandom(16)).decode('ascii').lower()

def create_data_dir():
    if os.path.exists('../data'):
        if os.path.isdir('../data'):
            rmtree('../data')
        else:
            os.remove('../data')
    os.mkdir('../data')

    global data_files
    data_files = {}
    save_data_digest()

def generate_data_digest():
    text = ''
    for filename, hash in sorted(data_files.items()):
        text += base64.b64encode(filename.encode('utf-8')).decode('ascii') + ':' + hash + '\n'

    return generate_digest(text)

def check_data_digest():
    if not os.path.isfile('../data/.digest'):
        create_data_dir()
        return False
    
    if not os.path.isfile('../data/.salt'):
        create_data_dir()
        return False
    
    with open('../data/.salt', 'r') as f:
        salt = f.read()
        if salt.find('\n') != 32 or len(salt) != 65:
            create_data_dir()
            return False
    
    text = ''
    for filename in sorted(os.listdir('../data')):
        path = '../data/' + filename
        if os.path.isdir(path):
            rmtree(path)
            continue
        if path == '../data/.digest':
            continue
        with open(path, 'r') as f:
            text += base64.b64encode(filename.encode('utf-8')).decode('ascii') + ':' + generate_digest(f.read()) + '\n'

    digest = generate_digest(text)
    with open('../data/.digest', 'r') as f:
        current_digest = f.read()
    if digest != current_digest:
        create_data_dir()
        return False
    return True

def check_file_digest(filename):
    if not os.path.isdir('../data'):
        create_data_dir()
        return False
    path = '../data/'+filename
    if (filename in data_files) != os.path.exists(path):
        create_data_dir()
        return False
    if os.path.exists(path):
        if not os.path.isfile(path):
            create_data_dir()
            return False
    else:
        return True
    with open('../data/'+filename, 'r') as f:
        digest = generate_digest(f.read())
    if digest != data_files[filename]:
        create_data_dir()
        return False
    return True
    

def save_data_digest():
    if not os.path.isdir('../data'):
        create_data_dir()
    global fixed_salt
    if not os.path.isfile('../data/.salt'):
        if os.path.isdir('../data/.salt'):
            rmtree('../data/.salt')
        with open('../data/.salt', 'w') as f:
            fixed_salt = base64.b16encode(os.urandom(16)).decode('ascii').lower()
            salt = fixed_salt+'\n'+base64.b16encode(os.urandom(16)).decode('ascii').lower()
            f.write(salt)
            data_files['.salt'] = generate_digest(salt)
    else:
        salt = fixed_salt+'\n'+base64.b16encode(os.urandom(16)).decode('ascii').lower()
        with open('../data/.salt', 'w') as f:
            f.write(salt)
            data_files['.salt'] = generate_digest(salt)
    
    if os.path.isdir('../data/.digest'):
        rmtree('../data/.digest')
    
    with open('../data/.digest', 'w') as f:
        f.write(generate_data_digest())

def generate_digest(text):
    return sha256(text.encode('ascii')).hexdigest()

def load_files():
    if not os.path.isdir('../data'):
        create_data_dir()
    global data_files
    data_files = {}
    for filename in sorted(os.listdir('../data')):
        path = '../data/' + filename
        if os.path.isdir(path):
            rmtree(path)
            continue
        if path == '../data/.digest':
            continue
        with open(path, 'r') as f:
            data_files[filename] = generate_digest(f.read())
    
    check_data_digest()
    global fixed_salt
    with open('../data/.salt', 'r') as f:
        fixed_salt = f.read().split('\n')[0]

class Data:
    @staticmethod
    def create_file(filename, creator=None, override=False):
        if '/' in filename:
            raise Exception('Directories with data not supported')
        check_file_digest(filename)
        
        if creator is None:
            if filename in creators:
                creator = creators[filename]
            else:
                creator = ''
        
        path = '../data/'+filename
        if os.path.isdir(path):
            rmtree(path)
        
        if (not os.path.isfile(path)) or override:
            if callable(creator):
                text = str(creator())
            else:
                text = str(creator)
            with open(path, 'w') as f:
                f.write(text)
            data_files[filename] = generate_digest(text)
        if creator != '':
            creators[filename] = creator
        save_data_digest()
            
    @staticmethod
    def write_to_file(filename, content):
        if not os.path.isfile('../data/'+filename):
            Data.create_file(filename)
        else:
            if not check_file_digest(filename):
                Data.create_file(filename)
        with open('../data/'+filename, 'w') as f:
            f.write(content)
            data_files[filename] = generate_digest(content)
        save_data_digest()

    @staticmethod
    def read_from_file(filename):
        if not os.path.isfile('../data/'+filename):
            Data.create_file(filename)
        else:
            if not check_file_digest(filename):
                Data.create_file(filename)
        with open('../data/'+filename, 'r') as f:
            content = f.read()
        
        return content

load_files()