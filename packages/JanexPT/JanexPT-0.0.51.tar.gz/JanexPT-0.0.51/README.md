# Janex: PyTorch Edition

A free open-source framework which can be used to build Machine Learning tools, LLMs, and Natural Language Processing scripts with full simplicity. This edition of Janex is built reliant on the main Janex library, and utilises PyTorch and the Natural Language Toolkit to attempt a slightly different approach of Intent Classification.

<h3> How to use? </h3>

Firstly, you need to install the Janex: PyTorch Edition library.
```bash
pip install JanexPT
```

Secondly, you need to import JanexPT into your code.
```python
from JanexPT import *
```

Next, create an instance of the JanexPT class and define the path to your intents, thesaurus, and the name you wish to give to your AI.
```python
intents_file_path = "intents.json"

janexpt = JanexPT(intents_file_path)

```

Then, you will need to train your intents data into a pth file. If you do not have a training program, it will curl install the pre-built one from this repo.
```
janexpt.trainpt()
```

Next, you need to give the program some text you wish to send to your AI, and then send it.
```python
YourInput = input("You: ")

classification = JanexPT.pattern_compare(YourInput)

print(classification)
```

And there we have it, the code will use a triple-layer NeuralNet to predict which class your input belongs in, and then uses the Janex library to pick the best response from those available.