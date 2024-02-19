import os
import pickle


def to_text(list, path):
    with open(path, 'w') as f:
        f.write('\n'.join(list))
        # pickle.dump(list, f)

    print("done file at the", path)
