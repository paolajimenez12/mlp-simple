
import hashlib
def sha256(path):
    h = hashlib.sha256()
    with open(path,'rb') as f:
        h.update(f.read())
    return h.hexdigest()

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Uso: python sha256.py <ruta-archivo>')
    else:
        print(sha256(sys.argv[1]))
