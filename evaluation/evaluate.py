import argparse
from os import listdir
from os.path import join
import unicodedata

def read_dir(datadir, split, language):
    return {fname.split(".")[0]:join(datadir,fname) for fname in sorted(listdir(datadir)) if ("."+split in fname and language in fname)}


def read_train(trainfname, pos):
    trainlemmas = set()
    trainfeats = set()
    trainpairs = set()
    with open(trainfname, "r") as ftrain:
        for line in ftrain:
            lemma, infl, feats = line.split("\t")
            if pos and pos not in feats.split(";"):
                continue
            trainlemmas.add(lemma.strip())
            trainfeats.add(feats.strip())
            trainpairs.add((lemma.strip(), feats.strip()))
    return trainlemmas, trainfeats, trainpairs

def read_eval(evalfname, pos):
    evallemmas = []
    evalinfls = []
    evalfeats = []
    with open(evalfname, "r") as feval:
        for line in feval:
            if not line.strip():
                continue
            lemma, infl, feats = line.split("\t")
            if pos and pos not in feats.split(";"):
                continue
            evallemmas.append(lemma.strip())
            evalinfls.append(infl.strip())
            evalfeats.append(feats.strip())
    return evallemmas, evalinfls, evalfeats


def get_acc(preds):
    if len(preds) == 0:
        return 0
    return sum(preds)/len(preds)
   #return round(100*sum(preds)/len(preds),3)



def evaluate(lang, predfname, trainfname, evalfname, pos):

    trainlemmas, trainfeats, trainpairs = read_train(trainfname, pos)
    evallemmas, evalinfls, evalfeats = read_eval(evalfname, pos)
    predlemmas, predinfls, predfeats = read_eval(predfname, pos)

    if len(predlemmas) != len(evallemmas):
        print("PREDICTION (%d) AND EVAL (%d) FILES HAVE DIFFERENT LENGTHS. SKIPPING %s..." % (len(predlemmas), len(evallemmas), lang))
        return -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,[],[],[],[],[],[],[]

    predictions = [int(unicodedata.normalize("NFC",pred)==unicodedata.normalize("NFC",gold)) for pred, gold in zip(predinfls, evalinfls)]

    seenlemma_preds = [pred for pred, lemma, feats in zip(predictions, evallemmas, evalfeats) if (lemma in trainlemmas and feats not in trainfeats)]
    seenfeats_preds = [pred for pred, lemma, feats in zip(predictions, evallemmas, evalfeats) if (lemma not in trainlemmas and feats in trainfeats)]
    seenboth_preds = [pred for pred, lemma, feats in zip(predictions, evallemmas, evalfeats) if (feats in trainfeats and lemma in trainlemmas)]
    unseen_preds = [pred for pred, lemma, feats in zip(predictions, evallemmas, evalfeats) if (feats not in trainfeats and lemma not in trainlemmas)]
    bad_preds = [(pred, lemma, feats) for pred, lemma, feats in zip(predictions, evallemmas, evalfeats) if (lemma, feats) in trainpairs]
    if len(bad_preds) > 0:
        print(len(bad_preds), "(LEMMA, FEATS) IN TRAIN AND EVAL.")# SKIPPING %s" % lang)
#        print(bad_preds)
#        return -1,-1,-1,-1, -1,-1,-1,-1

    total_acc = get_acc(predictions)
    both_feats_acc = get_acc(seenfeats_preds + seenboth_preds)
    lemma_unseen_acc = get_acc(seenlemma_preds + unseen_preds)
    seenlemma_acc = get_acc(seenlemma_preds)
    seenfeats_acc = get_acc(seenfeats_preds)
    seenboth_acc = get_acc(seenboth_preds)
    unseen_acc = get_acc(unseen_preds)
    return total_acc, both_feats_acc, lemma_unseen_acc, seenboth_acc,seenlemma_acc, seenfeats_acc, unseen_acc, len(predictions), len(seenboth_preds)+len(seenfeats_preds), len(seenlemma_preds)+len(unseen_preds), len(seenboth_preds), len(seenlemma_preds), len(seenfeats_preds), len(unseen_preds), predictions, seenfeats_preds+seenboth_preds, seenlemma_preds+unseen_preds, seenboth_preds,seenlemma_preds, seenfeats_preds, unseen_preds


def evaluate_all(predfnames, trainfnames, evalfnames, partitions, pos):

    def rnd(num):
        return round(100*num, 3)

    print("Lang\t\tall acc\tboth+feats\tlemma+unseen\tboth\tlemma\tfeats\tunseen\t\t#total\t#both\t#lemma\t#feats\t#unseen")
    allpredictions = []
    allpreds_both_feats = []
    allpreds_lemma_unseen = []
    allpreds_both = []
    allpreds_lemma = []
    allpreds_feats = []
    allpreds_unseen = []
    part_predictions = {part:[] for part in partitions}
    part_preds_both_feats = {part:[] for part in partitions}
    part_preds_lemma_unseen = {part:[] for part in partitions}
    part_preds_both = {part:[] for part in partitions}
    part_preds_lemma = {part:[] for part in partitions}
    part_preds_feats = {part:[] for part in partitions}
    part_preds_unseen = {part:[] for part in partitions}

    for lang, predfname in predfnames.items():
#        agglutinative = False
#        for agg in ("ckt", "evn", "kat", "hun", "itl", "krl", "ket", "kaz", "kor", "lud", "khk", "tur", "vep", "sjo"):
#            agglutinative = agglutinative or agg in lang
#        if not agglutinative:
#            continue
        try:
            trainfname = trainfnames[lang]
            evalfname = evalfnames[lang.split("_")[0]]
            total_acc, both_feats_acc, lemma_unseen_acc, seenboth_acc, seenlemma_acc, seenfeats_acc, unseen_acc, num_predictions, num_both_feats, num_lemma_unseen,num_seenboth, num_seenlemma_preds, num_seenfeats_preds, num_unseen_preds, predictions, both_feats_preds, lemma_unseen_preds, seenboth_preds, seenlemma_preds, seenfeats_preds, unseen_preds = evaluate(lang, predfname, trainfname, evalfname, pos)
            allpredictions.extend(predictions)
            allpreds_both_feats.extend(both_feats_preds)
            allpreds_lemma_unseen.extend(lemma_unseen_preds)
            allpreds_both.extend(seenboth_preds)
            allpreds_lemma.extend(seenlemma_preds)
            allpreds_feats.extend(seenfeats_preds)
            allpreds_unseen.extend(unseen_preds)
            for part in partitions:
                if part in lang:
                    part_predictions[part].extend(predictions)
                    part_preds_both_feats[part].extend(both_feats_preds)
                    part_preds_lemma_unseen[part].extend(lemma_unseen_preds)
                    part_preds_both[part].extend(seenboth_preds)
                    part_preds_lemma[part].extend(seenlemma_preds)
                    part_preds_feats[part].extend(seenfeats_preds)
                    part_preds_unseen[part].extend(unseen_preds)
            if num_predictions == 0:
                continue
            print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t\t%s\t%s\t%s\t%s\t%s" % (lang, rnd(total_acc), rnd(both_feats_acc), rnd(lemma_unseen_acc), rnd(seenboth_acc), rnd(seenlemma_acc), rnd(seenfeats_acc), rnd(unseen_acc), num_predictions, num_seenboth, num_seenlemma_preds, num_seenfeats_preds, num_unseen_preds))
        except KeyError:
            print("ORIGINAL DATA FOR %s NOT FOUND. SKIPPING..." % lang)

    for part in partitions:
        total_acc = get_acc(part_predictions[part])
        both_feats_acc = get_acc(part_preds_both_feats[part])
        lemma_unseen_acc = get_acc(part_preds_lemma_unseen[part])
        seenboth_acc = get_acc(part_preds_both[part])
        seenlemma_acc = get_acc(part_preds_lemma[part])
        seenfeats_acc = get_acc(part_preds_feats[part])
        unseen_acc = get_acc(part_preds_unseen[part])
        print("%s\t\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (part.upper(), rnd(total_acc), rnd(both_feats_acc), rnd(lemma_unseen_acc), rnd(seenboth_acc), rnd(seenlemma_acc), rnd(seenfeats_acc), rnd(unseen_acc)))

    total_acc = get_acc(allpredictions)
    seenboth_acc = get_acc(allpreds_both)
    seenlemma_acc = get_acc(allpreds_lemma)
    seenfeats_acc = get_acc(allpreds_feats)
    unseen_acc = get_acc(allpreds_unseen)
    print("TOTAL\t\t%s\t%s\t%s\t%s\t%s" % (rnd(total_acc), rnd(seenboth_acc), rnd(seenlemma_acc), rnd(seenfeats_acc), rnd(unseen_acc)))
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Partitioned Evaluation for SIGMORPHON 2022 Task 0")
    parser.add_argument("preddir", help="Directory with prediction files")
    parser.add_argument("datadir", help="Directory containing original train, dev, test files")
    parser.add_argument("outfname", nargs="?", help="Filename to write outputs to")
    parser.add_argument("--evaltype", type=str, help="evaluate [dev] predictions or [test] predictions", default="test")
    parser.add_argument("--language", nargs="?", type=str, help="Evaluate a specific language. Will run on all languages in preddir if omitted", default="")
    parser.add_argument("--partition", nargs="+", help="List of partitions over which to calculate aggregate scores. Example --partition _large _small", default=[])
    parser.add_argument("--pos", nargs = "?", help="Only evaluate for a given POS extracted from the tags. Evaluates everything if arg is omitted")

    args = parser.parse_args()

    evaltype = args.evaltype.lower()
    if evaltype not in ("dev", "test"):
        exit("Eval type must be 'dev' or 'test'")

    lang_to_predfname = read_dir(args.preddir, evaltype, args.language)
    lang_to_trainfname = read_dir(args.datadir, "train", args.language)
    evaltype = evaltype if evaltype == "dev" else "gold"
    lang_to_evalfname = read_dir(args.datadir, evaltype, args.language.split("_")[0])
    evaluate_all(lang_to_predfname, lang_to_trainfname, lang_to_evalfname, args.partition, args.pos)
