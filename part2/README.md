# SIGMORPHON–UniMorph Shared Task on Generalization in Morphological Inflection Generation 
## Part 2: (Automatic) Morphological Acquisition Trajectories

[***Data available here***](https://github.com/sigmorphon/2022InflectionST/tree/main/part2)

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
* **May 6, 2022**: Participants submit test predictions on all languages.
* **June 3, 2022**: Participants’ system description papers due.


### Submission Instructions 

Please submit your team's results to [jordan.kodner@stonybrook.edu](jordan.kodner@stonybrook.edu) CCing your team mates by May 6, 2022. Please use "SIGMORPHON Task 0 Part 2" in your subject line.


### Organizers

* Jordan Kodner (Stony Brook University)
* Salam Khalifa (Stony Brook University)
* *and more on the way*


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

