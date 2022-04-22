
# Evaluation Script

## Reports Five Scores
- Accuracy on all evaluation (either dev or test) data
- "Both" accuracy on test pairs for which both the lemma and features are attested somewhere in training
- "Lemma" accuracy on test pairs whose lemma was attested in training but feature bundle was not
- "Feats" accuracy on test pairs whose feature bundle was attested somewhere in training but lemma was not
- "Unseen" accuracy on test pairs totally unattested in training

## Usage
```
$ python3 evaluate.py -h

usage: evaluate.py [-h] [--evaltype EVALTYPE] [--language [LANGUAGE]]
                   preddir datadir [outfname]

Partitioned Evaluation for SIGMORPHON 2022 Task 0

positional arguments:
  preddir               Directory with prediction files
  datadir               Directory containing original train, dev, test files
  outfname              Filename to write outputs to

optional arguments:
  -h, --help            show this help message and exit
  --evaltype EVALTYPE   evaluate [dev] predictions or [test] predictions
  --language [LANGUAGE]
                        Evaluate a specific language. Will run on all
                        languages in preddir if omitted
```

## Example Usage

Evaluates performance on dev for all part1 development languages
```
$ python3 evaluate.py my_predictions ../../part1/development_languages/ --evaltype dev --partition _small _large
```

Evaluates performance on dev for all part2 languages
```
evaluate.py my_predictions ../../part2/ --evaltype dev --partition ara eng deu
```

Evaluates performance on test for just goh_small
```
$ python3 evaluate.py my_predictions ../../part1/development_languages/ --evaltype test --language goh_small
```


