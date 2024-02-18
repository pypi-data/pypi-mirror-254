import time
import utils
from correction import Corrector

c = Corrector()
target_words = utils.read_files("target_words")
c.load_target_words(target_words)
test_words = utils.read_files("test_file", True)
start = time.time()
for w in test_words:
    print(w)
    res = c.recall_word(w)
    print(res)
    print("\n")
print(time.time() - start)



