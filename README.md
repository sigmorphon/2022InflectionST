# SIGMORPHON–UniMorph Shared Task on Typologically Diverse and Acquisition-Inspired Morphological Inflection Generation

SIGMORPHON’s seventh installment of its inflection generation shared task will be divided into two parts:

+ ***Part 1***: [Typologically Diverse Morphological (Re-)Inflection](https://github.com/sigmorphon/2022InflectionST/tree/main/part1)
+ ***Part 2***: [(Automatic) Morphological Acquisition Trajectories](https://github.com/sigmorphon/2022InflectionST/tree/main/part2/README.md)

Please join our [Google Group](https://groups.google.com/g/sigmorphon2022-sharedtask0) to stay up to date.

***Click here to [register for the task](https://forms.gle/Wf1m5nAPzjVhzDLb7)!***


## Part 1: Typologically Diverse Morphological (Re-)Inflection


### Task Summary


In this shared task, participants will design a model that learns to generate morphological inflections from a lemma and a set of morphosyntactic features of the target form. Each language in the task has its own training, development, and test splits. Training and development splits contain triples, each consisting of a lemma, a target form, and a set of morphological features, provided in the UniMorph format (the “Data” section below provides an example of input format). Test splits only provide lemmas and morphological tags: your model will need to predict the missing target form.

The model should be general enough to work for natural languages of any typological patterning. For example, Tagalog verbs exhibit [circumfixation](https://en.wikipedia.org/wiki/Circumfix); thus, a model with a strong inductive bias towards suffixing will likely not work well for Tagalog.


### Task Details
This task will proceed in three phases: the ***Development Phase***, the ***Generalization Phase***, and the ***Evaluation Phase***. As the phases advance, more data and more languages will be released.

In the ***Development Phase***, we will provide training and development splits that should be used to *develop* your system.
We will refer to them as the *development languages*. The list of languages is below. There is a small training set for each languages and a large training set for languages with enough annotated paradigms.

In the ***Generalization Phase***, we will provide training and development splits for new languages where approximately half are genetically related (belong to the same family) and half are genetically *unrelated* (are isolates or belong to a different family) to the development languages.  We will also keep the genetically unrelated language *families* a surprise, though some languages will come from the same families as those in the Development Phase.

In the ***Evaluation Phase***, the participants’ models will be evaluated on held-out forms from all of the languages from the previous phases. The languages from the Development Phase and the Generalization Phase are evaluated simultaneously. The only difference is that there has been more time to construct a model for those languages released in the Development Phase. It follows that a model could easily overfit to or favor phenomena that are more frequent in languages presented in the Development Phase, especially if parameters are shared across languages. For instance, a model based on the morphological patterning of the Indo-European languages may end up with a bias towards suffixing and will struggle to learn prefixing or circumfixation, the degree to which only becomes apparent during experimentation on other languages whose inflectional morphology patterns differ. Of course, the model architecture itself could explicitly or implicitly favor certain word formation types (suffixing, prefixing, etc.).


#### Development Languages

| Language | Family| code | UM | Contributors |
|---|---|---|---|---|
| Arabic, Modern Standard | Semitic (Afro-Asiatic) | ara | https://github.com/unimorph/ara/ara_atb | Salam Khalifa, Nizar Habash |
| Assamese | Indic (Indo-European) | asm | https://github.com/unimorph/asm/ | Khuyagbaatar Batsuren, Aryaman Arora |
| Braj | Indic (Indo-European) | bra | https://github.com/unimorph/bra/ | Shyam Ratan, Ritesh Kumar |
| Chukchi | Chukotko-Kamchatkan | ckt | https://github.com/unimorph/ckt/ | Karina Sheifer, Maria Ryskina |
| English, Old | Germanic (Indo-European) | ang | https://github.com/unimorph/ang/ | Jeremiah Young |
| Evenki | Tungusic | evn | https://github.com/unimorph/evn/ | Elena Klyachko |
| Georgian | Kartvelian | kat | https://github.com/unimorph/kat/ | Simon Guriel, Silvia Guriel-Agiashvili & Nona Atanelov |
| German, Low | Germanic (Indo-European) | nds | https://github.com/unimorph/nds/ | Jeremiah Young |
| German, Middle Low | Germanic (Indo-European) | nds | https://github.com/unimorph/gml/ | Jeremiah Young |
| German, Old High | Germanic (Indo-European) | goh | https://github.com/unimorph/goh/ | Jeremiah Young |
| Gothic | Germanic (Indo-European) | got | https://github.com/unimorph/got/ | Jeremiah Young |
| Gujarati | Indic (Indo-European) | guj | https://github.com/unimorph/guj/ | Aryaman Arora, Khuyaagbaatar Batsuren |
| Hebrew | Semitic (Afro-Asiatic) | heb | https://github.com/unimorph/heb/ | Omer Goldman |
| Hungarian | Ugric (Uralic) | hun | https://github.com/unimorph/hun/ | Judit Ács, Khuyagbaatar Batsuren, Gábor Bella, Ryan Cotterell, Christo Kirov |
| Itelmen | Chukotko-Kamchatkan | itl | https://github.com/unimorph/itl/ | Karina Sheifer, Sofya Ganieva, Matvey Plugaryov |
| Karelian | Finnic (Uralic) | krl | https://github.com/unimorph/krl/ | (Wiktionary, [VepKar](http://dictorpus.krc.karelia.ru/en)) |
| Ket | Yeneisan | ket | https://github.com/unimorph/ket/ | Elena Budianskaya, Polina Mashkovtseva, Alexandra Serova |
| Kholosi | Indic (Indo-European) | hsi | https://github.com/unimorph/hsi/ | Aryaman Arora |
| Korean | Koreanic | kor | https://github.com/unimorph/kor/ | Maria Nepomniashchaya, Daria Rodionova, Anastasia Yemelina |
| Ludian | Finnic (Uralic) | lud | https://github.com/unimorph/lud/ | ([VepKar](http://dictorpus.krc.karelia.ru/en)) |
| Magahi | Indic (Indo-European) | mag | https://github.com/unimorph/mag/ | Mohit Raj, Ritesh Kumar |
| Mongolian, Khalkha | Mongolic | khk | https://github.com/unimorph/khk/ | Khuyagbaatar Batsuren |
| Norse, Old | Germanic (Indo-European) | non | https://github.com/unimorph/non/ | Jeremiah Young |
| Polish | Slavic (Indo-European) | pol | https://github.com/unimorph/pol/ | Marcin Woliński, Zygmunt Saloni, Robert Wołosz, Włodzimierz Gruszczyński, Danuta Skowrońska, Zigniew Bronk, Witold Kieraś |
| Pomak | Slavic (Indo-European) | poma| https://github.com/unimorph/poma/ | Ritvan Karahodja, Antonios Anastasopoulos |
| Slovak | Slavic (Indo-European) | slk | https://github.com/unimorph/slk/ | Jan Hajič, Jan Hric, Witold Kieraś |
| Sorbian, Upper | Slavic (Indo-European) | hsb | https://github.com/unimorph/hsb/ | Taras Andrushko, Igor Marchenko |
| Turkish | Turkic | tur | https://github.com/unimorph/tur/ | Omer Goldman, Duygu Ataman |
| Veps | Finnic (Uralic) | vep | https://github.com/unimorph/vep/ | ([VepKar](http://dictorpus.krc.karelia.ru/en)) |
| Xibe | Tungusic | sjo | https://github.com/unimorph/sjo/ | Elena Klyachko |

#### Surprise Languages
| Language | Family| code | UM | Contributors |
|---|---|---|---|---|
| Armenian | Indo-European | hye | https://github.com/unimorph/hye/ | Hossep Dolatian, Khuyagbaatar Batsuren, Ryan Cotterell |
| Kazakh | Turkic | kaz | https://github.com/unimorph/kaz/ | Eleanor Chodroff, Khuyagbaatar Batsuren |
| Lamahalot | Austronesian | slp | https://github.com/unimorph/slp  | Yustinus Ghanggo Ate |

### Timeline


**Stage 1: Development Phase**
* **March 29, 2022**: Training and development splits for development languages released; we invite participants to report errors.
* **March 29, 2022**: Neural and non-neural baselines for development languages released.

**Stage 2: Generalization Phase**
* **April 17, 2022**: Training and development splits for surprise languages released.
(This is not a zero-shot learning task. Participants will be given training data for all languages.)

**Stage 3: Evaluation Phase**
* **April 22, 2022**: Test splits for all languages (both development and surprise) released.
* **May ~~6~~ 17, 2022**: Participants submit test predictions on all languages.

**Stage 4: Write-up Phase**
* **June 3, 2022**: Participants’ system description papers due.

### Data

The training and development data are provided in a simple utf-8 encoded text format for both the development and surprise languages. Each line in a file is an example that consists of word forms and corresponding morphosyntactic descriptions (MSDs) provided as a set of features, separated by semicolons. We refer to the MSDs as (morphological) tags for simplicity. The fields on a line are TAB-separated.
The fields are: lemma, target form, tag. Here we present an example from the Akan training data (the Akan verb “bisa” means “to ask” in English):

```
bisa     mmbisa     V;PRS;HAB;NEG
```

In the training data, we give all three fields. In the test phase, we omit field 2.

We will provide varying amounts of labeled training data, depending on the language, to assess models’ ability to generalize to novel forms, in addition to information about each language’s family and sub-family, and WALS features which participants may optionally use. For each language, the possible inflections are taken from a finite set of morphological tags, presented in the UniMorph schema.

Two training sets are provided for most languages in order to test models' behavior on smaller and larger data sets.

### Evaluation

***Evaluation script available here https://github.com/sigmorphon/2022InflectionST/tree/main/evaluation***

The language generalization evaluation is extended from previous years' design. We will simultaneously evaluate models for both the Development languages, whose training and development sets will be available for an elongated period of time, and the Surprise languages, whose training and development sets will only be available for a short time prior to submission, which precludes extensive tuning. To be officially ranked, you must submit results for **all** evaluation languages. Thus, to succeed, your class of models (e.g. neural sequence-to-sequence models or weighted finite-state transducers with hand-crafted features) must generalize well to the group of Surprise languages that are typologically distinct from the Development languages you performed model selection on. To repeat: This is not a zero-shot learning task, but rather our evaluation set-up is designed to test the inherent inductive bias in the participants' chosen model class.

Evaluation is designed to provide insights into performance over typologically distinct languages. Accuracy on held out forms will be evaluated separately for three classes of languages:
* held-out forms from the Development languages
* held-out forms from genetically related Surprise languages
* held-out forms from genetically unrelated Surprise languages

For each language, accuracy will be evaluated on the entirety of the held-out forms as well as the following subsets. This will provide insights into systems' ability to generalize across morphological information within languages. Since (lemma, features) pairs are provided at test time and no (lemma, features) pair can have been attested at training time, there are three logical subsets
* held-out forms for lemmas attested in training, feature sets unattested in training
* held-out forms for feature sets attested in training, lemmas unattested in training
* held-out forms for (lemma, feature) pairs completely unattested in training


The human-like generalization part of this shared task will be evaluated as described above but with an additional analysis of error types and their relationships to attested error types observed during child development: the distribution of ''over-regularization'' and ''over-irregularization'' errors, omission and comisson errors, whether errors yield *U*-shaped developmental trajectories on languaegs for which the phenomenon is well attested, and relative order of acquisition of generalizations as data size increases.

### Submission Instructions 

Please submit your team's results to jordan.kodner@stonybrook.edu CCing your team mates by May ~~6th~~ 17th, 2022.


### Baselines

***Baseline results available here https://github.com/sigmorphon/2022InflectionST/tree/main/evaluation***

The organizers will provide one non-neural and one neural baseline for the participants’ consumption.
Its use is optional and is provided to help the participants develop their own models faster.
The neural baseline is a multilingual transformer ([Vaswani et al., 2017](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf)). The version of this model adopted for character-level tasks currently holds the state-of-the-art on the 2017 SIGMORPHON shared task data. The transformer takes the lemma and morphological tags as input and outputs the target inflection. Given the low-resource setup, a single model will be trained on all languages. Additionally, we consider the data augmentation technique used by [Anastasopoulos and Neubig (2019)](https://www.aclweb.org/anthology/D19-1091/) as another baseline.

To run the non-neural baseline use command:
```bash
$ python baselines/nonneural/baseline.py --path part1/development_languages/
```

To run the neural baseline first download and augment [(Anastasopoulos and Neubig, 2019)](https://arxiv.org/abs/1908.05838) the data
```bash
$ mkdir part1/original
$ cp part1/development_languages/* part1/original

$ bash baselines/neural/example/sigmorphon2021-shared-tasks/augment.sh
$ python baselines/neural/example/sigmorphon2021-shared-tasks/task0-build-dataset.py all
```

Then, to run the transducer [(Wu et al, 2021)](https://arxiv.org/abs/2005.10213), one model per language.
```bash
$ bash baselines/neural/example/sigmorphon2021-shared-tasks/task0-launch.sh
```


### Organizers

**Task Logistics**: Jordan Kodner, Salam Khalifa, Khuyagbaatar Batsuren, Ekaterina Vylomova, Maria Ryskina, Omer Goldman, Jeffrey Heinz, Ryan Cotterell, Mans Hulden, Garret Nicolai, David Yarowsky

**Data Preparation**: Antonios Anastasopoulos, Taras Andrushko, Aryaman Arora, Duygu Ataman, Nona Atanelov, Khuyagbaatar Batsuren, Zigniew Bronk, Elena Budianskaya, Hossep Dolatian, Sofya Ganieva, Omer Goldman, Włodzimierz Gruszczyński, Simor Guriel, Silvia Guriel-Agiashvili, David Guriel, Nizar Habash, Jan Hajič, Jan Hric, Salam Khalifa, Witold Kieraś, Elena Klyachko, Ritesh Kumar, Ritvan Karahodja, Igor Marchenko, Polina Mashkovtseva, Maria Nepomniashchaya, Matvey Plugaryov, Mohit Raj, Shyam Ratan, Daria Rodionova, Maria Ryskina, Zygmunt Saloni, Alexadra Serova, Karina Sheifer, Danuta Skowrońska, Marcin Woliński, Robert Wołosz, Anastasia Yemelina, Jeremiah Young 



## Part 2: (Automatic) Morphological Acquisition Trajectories

### Task Description
How exactly it is that children acquire their native morphologies and carry out morphological generalization in practice remains a major question in language acquisition and theoretical morphology, one that has major implications for cognitive science more broadly. Neural approaches have long played a role is these discussions, with their early promise kicking off the so-called "Past-Tense Debate" of the 1980s and 90s. See Gary Marcus’ book [The Algebraic Mind](https://mitpress.mit.edu/books/algebraic-mind) for an overview. 

The recent success and popularity of improved neural methods has brought renewed interest in these questions from the computional linguistics and cognitive science communities. A series of papers and responses have been published in the last few years [Kirov and Cotterell (2018)](https://transacl.org/index.php/tacl/article/view/1420), [Corkery et al. (2019)](https://aclanthology.org/P19-1376/) [McCurdy et al. (2020)](https://www.aclweb.org/anthology/2020.acl-main.159/), [Belth, Payne, et al. (2021)](https://escholarship.org/uc/item/1md2p6j5), and [Dankers et al. (2021)](https://aclanthology.org/2021.conll-1.8/). [Last year's SIGMORPHON shared task](https://github.com/sigmorphon/2021Task0/) threw its hat into the ring as well, offering a subtask correlating predicted and human-wellformedness ratings for inflected forms.

This year's subtask approaches the question from a different angle. Instead of predicting well-formedness of nonce word forms, systems will instead be evaluated on their ability to generalize over naturalistic low-resource inputs. We have prepared data to determine systems' learning trajectories and compare them against the wealth of data that has been collected about human learning trajectories for three famous problems: English past tense, the namesake of the Past-Tense Debate (e.g., [Marcus et al. 1992](https://www.jstor.org/stable/1166115?seq=1#metadata_info_tab_contents)), German noun plurals, a well-studied challenge case which may have a minority-default pattern ([Clahsen et al. 1992](https://www.sciencedirect.com/science/article/pii/001002779290018D), [Marcus et al. 1995](https://d1wqtxts1xzle7.cloudfront.net/30270110/Marcus_Pinker_et_al_1995_German_Inflection_Cognitive_Psychology-with-cover-page-v2.pdf?Expires=1646265841&Signature=PRNt6JeRUZYQ0KBtfJMzRH3cQPySiWtycYIZqkYPBoxn2-Y3k6zgLMpUHKLE3RFPMajxCT0ReU-~CuADL66-hk7zI9eT6pcoj-jBOTr5Yt4NbjEoHs~o4-AXB6J1sdKcKLqMLH3x6h41Dtnp-tgviym3GV42e6usK0yQyMM9O0KiEY~nWulXAqVFTeY~CL8~0PBYEHXRywsTm6ZOMI7kTZzefyg1ZLGlrGtHcZyHMV4KO0ibT7SddhQgiiuHh6j4jIlCwdxiovf~MPqu5lpJqxDdlOoJS8AktpmsCTipAw4Q2~frNXr1rJ2GM2WBUABjugH0JbBhhvB4TpLzPZ6qrA__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)), and Arabic noun plurals, an even more challenging case with several competing affixal and templatic patterns ([Ravid & Farah 1999](https://journals.sagepub.com/doi/pdf/10.1177/014272379901905603?casa_token=RHoIAWxOousAAAAA:NpjamGN3dzbA43WuEpZzKbBApqyYol5jI9vqJ3C7NKGigY5nSmm5ZA18sciRfWFESETqXL21chgi), [Dawdy-Hesterberg & Pierrehumbert (2014)](https://www.tandfonline.com/doi/pdf/10.1080/23273798.2014.899377)).

Generalization is a core task facing any morphology learner, human or otherwise, because morphological data is extremely sparse. Even for languages with moderately sized paradigms, the vast majority of possible forms will not be attested even in millions of tokens of input. These distributions are highly skewed such that a few lemmas may have mostly complete paradigms, while most lemmas will only be attested in a couple forms [Chan 2008](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.152.9420&rep=rep1&type=pdf). Due to this speakers young and old are often forced to infer inflected forms that were not well-attested in their inputs up to that point, even for known lemmas.

Children make mistakes when inferring forms which provide insights into the organization of their grammars over time. Much has been discovered about the learning trajectories of children acquiring these patterns. Learners are more likely to over-apply apparently productive patterns than over-apply non-productive patterns (over-regularization over "over-irregularization") and are more likely to omit inflectional information than substitute other inflectional information (omission over comission). English past tense and Arabic noun plural learners exhibit u-shaped developmental regression where their accuracy improves, degrades, and improves again.



### Data and Evaluation

In order to evaluate to what extent automatic systems achieve these patterns or different patterns, we have prepared a series of training sets of increasing size so that performance can be calculated as input increases and the presence or absence of particular inputs can be correlated with particular model behaviors. Training sets are sampled weighted by frequency from German and English child-directed speech corpora available from UniMorph with frequencies from the CHILDES database [MacWhinney 2000](https://childes.talkbank.org/access/) such that the smallest training sets contain only the highest frequency words. Arabic is sampled in the same way, but words and their frequencies are taken from the [Penn Arabic Treebank](https://www.marefa.org/images/e/e8/The_penn_arabic_treebank_Building_a_large-scale_an_%281%29.pdf). A development and test set are held out in each case.

Performance will be evaluated by accuracy across attested and unattested lemmas and features as in Part 1 for each training size. This will provide a developmental trajectory. In addition, error types will be analyzed and classified in a manner similar to [Gorman et al. (2019)](https://aclanthology.org/K19-1014/) but with reference to the error types attested and unattested in acquisition. In the lowest training settings, it may not be possible for a system to achieve perfect accuracy on the test set. Those cases will provide insights into what generalizations systems are taking. Considering the following hypothetical example from English, the following verb lemmas are phonotactially similar but inflect the past tense differently. If a system were to adopt any one pattern based on the *-ing* verbs in the training it would not achieve 100% accuracy, but which generalization it picks (*-ed* or another one) would reveal something about the model.

```
sing	sang	V;PST
sting	stung	V;PST
bring	brought	V;PST
ping	pinged	V;PST
```

Training and dev data may be downloaded [here](https://github.com/sigmorphon/2022InflectionST/tree/main/part2). 

The data are in the standard UniMorph triple file format:

<div class="language-plaintext highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code>swim swam V;PST</code></pre>
</div>
</div>

### Timeline

* **March 15, 2022**: Training data for English, German, and Arabic are released. We invite participants to report errors.
* **March 29, 2022**: Neural and non-neural baselines for English, German, and Arabic are released.
* **April 22, 2022**: Test splits for all languages (both development and surprise) released.
* **May ~~6~~ ~~13~~ 17, 2022**: Participants submit test predictions on all languages.
* **June 3, 2022**: Participants’ system description papers due.


### Submission Instructions 

Please submit your team's results to [jordan.kodner@stonybrook.edu](jordan.kodner@stonybrook.edu) CCing your team mates by May 6, 2022. Please use "SIGMORPHON Task 0 Part 2" in your subject line.


### Organizers

* Jordan Kodner (Stony Brook University)
* Salam Khalifa (Stony Brook University)


### References

Belth, C. A., Payne, S. R., Beser, D., Kodner, J., & Yang, C. (2021). [The Greedy and Recursive Search for Morphological Productivity.](https://escholarship.org/uc/item/1md2p6j5) In *Proceedings of the Annual Meeting of the Cognitive Science Society* (Vol. 43, No. 43).

Chan, Erwin. (2008). [*Structures and distributions in morphology learning.*](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.152.9420&rep=rep1&type=pdf) Doctoral dissertation, University of Pennsylvania.

Clahsen, H., Rothweiler, M., Woest, A., & Marcus, G. F. (1992). [Regular and irregular inflection in the acquisition of German noun plurals.](https://www.sciencedirect.com/science/article/pii/001002779290018D) *Cognition*, 45(3), 225-255.

Corkery, M., Matusevych, Y., and Goldwater, S. (2019). [Are we there yet? Encoder-decoder neural networks as cognitive models of English past tense inflection](). In *Proceedings of ACL 2019.*

Dankers, V., Langedijk, A., McCurdy, K., Williams, A., & Hupkes, D. (2021). [Generalising to German Plural Noun Classes, from the Perspective of a Recurrent Neural Network.](https://aclanthology.org/2021.conll-1.8/). In *Proceedings of CoNLL 2021* (pp. 94-108).

Dawdy-Hesterberg, L. G., & Pierrehumbert, J. B. (2014). [Learnability and generalisation of Arabic broken plural nouns.](https://www.tandfonline.com/doi/pdf/10.1080/23273798.2014.899377) *Language, cognition and neuroscience*, 29(10), 1268-1282.

Gorman, K., McCarthy, A. D., Cotterell, R., Vylomova, E., Silfverberg, M., & Markowska, M. (2019, November). [Weird Inflects but OK: Making Sense of Morphological Generation Errors.](https://aclanthology.org/K19-1014/) In *Proceedings of CoNLL 2019* (pp. 140-151).

Kirov, C. and Cotterell, R. (2018). [Recurrent Neural Networks in Linguistic Theory: Revisiting Pinker and Prince (1988) and the Past Tense Debate](). *TACL*, 6, 651-665.

Kirov, C., Cotterell, R., Sylak-Glassman, J., Walther, G., Vylomova, E., Xia, P., Faruqui, M., Mielke, S., McCarthy, A., Kübler, S., Yarowsky, D., Eisner, J., and Hulden, M. (2018). [UniMorph 2.0: Universal Morphology](https://arxiv.org/abs/1810.11101). In *Proceedings of LREC* 2018.

Maamouri, M., Bies, A., Buckwalter, T., & Mekki, W. (2004. [The Penn Arabic Treebank: Building a large-scale annotated Arabic corpus.](https://www.marefa.org/images/e/e8/The_penn_arabic_treebank_Building_a_large-scale_an_%281%29.pdf) In *NEMLAR conference on Arabic language resources and tools* (Vol. 27, pp. 466-467).

MacWhinney, B. (2000). [The CHILDES project: The database.](https://childes.talkbank.org/access/)

Marcus, G. F. (2001). [The Algebraic Mind: Integrating Connectionism and Cognitive Science](https://mitpress.mit.edu/books/algebraic-mind). MIT Press.

Marcus, G. F., Pinker, S., Ullman, M., Hollander, M., Rosen, T. J., Xu, F., & Clahsen, H. (1992). [Overregularization in language acquisition.](https://www.jstor.org/stable/1166115?seq=1#metadata_info_tab_contents) *Monographs of the society for research in child development*.

Marcus, G. F., Brinkmann, U., Clahsen, H., Wiese, R., & Pinker, S. (1995). [German inflection: The exception that proves the rule.](https://d1wqtxts1xzle7.cloudfront.net/30270110/Marcus_Pinker_et_al_1995_German_Inflection_Cognitive_Psychology-with-cover-page-v2.pdf?Expires=1646265841&Signature=PRNt6JeRUZYQ0KBtfJMzRH3cQPySiWtycYIZqkYPBoxn2-Y3k6zgLMpUHKLE3RFPMajxCT0ReU-~CuADL66-hk7zI9eT6pcoj-jBOTr5Yt4NbjEoHs~o4-AXB6J1sdKcKLqMLH3x6h41Dtnp-tgviym3GV42e6usK0yQyMM9O0KiEY~nWulXAqVFTeY~CL8~0PBYEHXRywsTm6ZOMI7kTZzefyg1ZLGlrGtHcZyHMV4KO0ibT7SddhQgiiuHh6j4jIlCwdxiovf~MPqu5lpJqxDdlOoJS8AktpmsCTipAw4Q2~frNXr1rJ2GM2WBUABjugH0JbBhhvB4TpLzPZ6qrA__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA) *Cognitive psychology*, 29(3), 189-256.

McCurdy, K., Goldwater, S., and Lopez, A. (2020). [Inflecting When There’s No Majority: Limitations of Encoder-Decoder Neural Networks as Cognitive Models for German Plurals](https://www.aclweb.org/anthology/2020.acl-main.159/). In *Proceedings of ACL 2020*.

Ravid, D., & Farah, R. (1999). [Learning about noun plurals in early Palestinian Arabic.](https://journals.sagepub.com/doi/pdf/10.1177/014272379901905603?casa_token=RHoIAWxOousAAAAA:NpjamGN3dzbA43WuEpZzKbBApqyYol5jI9vqJ3C7NKGigY5nSmm5ZA18sciRfWFESETqXL21chgi) *First Language*, 19(56), 187-206.


# Participation Policy

We do not tolerate harassment in our shared task. Anyone who has been previously found to have harassed one of the organizers cannot participate in our task in any capacity. There are too few organizers for us to accomodate the harasser in a manner that ensures the safety of their victims. (This policy was written on June 22nd and cannot be applied retroactively, but will be in place for all future iterations of the task.)

