# spaCy powered Label Studio ML backend

spaCy integration for Label Studio.
this is running besides the azure functions.

[Demo video](https://youtu.be/F19NT-21uT4)

## running the backend

1. prepare environment

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
```

2. start label studio
```
label-studio
```

3. Start the backend and add the URL to your Label Studio project settings.

```
label-studio-ml start channel_ml_ner
```

4. As you train new models, they will appear in a `checkpoints` directory. The latest checkpoint will be symlinked to `latest-model`.



## modifying the config

In the `channel_ml_ner` directory, add your spaCy `config.cfg` file. You can optionally add a `model-best` folder from a pre-trained model, to get started with predictions straight away. 
