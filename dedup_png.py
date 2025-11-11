#!/usr/bin/env python3
import os
import hashlib

DIRECTORY = "."

def hash_file(path):
    """Zwraca SHA256 zawartości pliku."""
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def main():
    seen = {}
    deleted = 0

    for root, _, files in os.walk(DIRECTORY):
        for name in files:
            if not name.lower().endswith(".png"):
                continue
            path = os.path.join(root, name)
            file_hash = hash_file(path)

            if file_hash in seen:
                print(f"Duplikat: {path} (oryginał: {seen[file_hash]})")
                os.remove(path)
                deleted += 1
            else:
                seen[file_hash] = path

    print(f"\nUsunięto {deleted} duplikat(ów).")

if __name__ == "__main__":
    main()
