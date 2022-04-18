import argparse
from os import listdir
from os.path import join

def read_dir(datadir, split, language):
    return {fname.split(".")[0]:join(datadir,fname) for fname in listdir(datadir) if ("."+split in fname and language in fname)}


def read_train(trainfname):
    trainlemmas = set()
    trainfeats = set()
    trainpairs = set()
    with open(trainfname, "r") as ftrain:
        for line in ftrain:
            lemma, infl, feats = line.split("\t")
            trainlemmas.add(lemma.strip())
            trainfeats.add(feats.strip())
            trainpairs.add((lemma.strip(), feats.strip()))
    return trainlemmas, trainfeats, trainpairs

def read_eval(evalfname):
    evallemmas = []
    evalinfls = []
    evalfeats = []
    with open(evalfname, "r") as feval:
        for line in feval:
            lemma, infl, feats = line.split("\t")
            evallemmas.append(lemma.strip())
            evalinfls.append(infl.strip())
            evalfeats.append(feats.strip())
    return evallemmas, evalinfls, evalfeats


def get_acc(preds):
    if len(preds) == 0:
        return 0
    return sum(preds)/len(preds)
   #return round(100*sum(preds)/len(preds),3)



def evaluate(lang, predfname, trainfname, evalfname):

    trainlemmas, trainfeats, trainpairs = read_train(trainfname)
    evallemmas, evalinfls, evalfeats = read_eval(evalfname)
    predlemmas, predinfls, predfeats = read_eval(predfname)

    if len(predlemmas) != len(evallemmas):
        print("PREDICTION (%d) AND EVAL (%d) FILES HAVE DIFFERENT LENGTHS. SKIPPING %s..." % (len(predictions), len(evallemmas), lang))
        return -1,-1,-1,-1, -1,-1,-1,-1

    predictions = [int(pred==gold) for pred, gold in zip(predinfls, evalinfls)]

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
    seenlemma_acc = get_acc(seenlemma_preds)
    seenfeats_acc = get_acc(seenfeats_preds)
    seenboth_acc = get_acc(seenboth_preds)
    unseen_acc = get_acc(unseen_preds)
    return total_acc, seenboth_acc,seenlemma_acc, seenfeats_acc, unseen_acc, len(predictions), len(seenboth_preds), len(seenlemma_preds), len(seenfeats_preds), len(unseen_preds), predictions, seenboth_preds,seenlemma_preds, seenfeats_preds, unseen_preds


def evaluate_all(predfnames, trainfnames, evalfnames):

    def rnd(num):
        return round(100*num, 3)

    print("Lang\t\tall acc\tboth\tlemma\tfeats\tunseen\t\t#total\t#both\t#lemma\t#feats\t#unseen")
    allpredictions = []
    allpreds_both = []
    allpreds_lemma = []
    allpreds_feats = []
    allpreds_unseen = []
    for lang, predfname in predfnames.items():
        try:
            trainfname = trainfnames[lang]
            evalfname = evalfnames[lang.split("_")[0]]
            total_acc, seenboth_acc, seenlemma_acc, seenfeats_acc, unseen_acc, num_predictions, num_seenboth, num_seenlemma_preds, num_seenfeats_preds, num_unseen_preds, predictions, seenboth_preds, seenlemma_preds, seenfeats_preds, unseen_preds = evaluate(lang, predfname, trainfname, evalfname)
            allpredictions.extend(predictions)
            allpreds_both.extend(seenboth_preds)
            allpreds_lemma.extend(seenlemma_preds)
            allpreds_feats.extend(seenfeats_preds)
            allpreds_unseen.extend(unseen_preds)
            if num_predictions == 0:
                continue
            print("%s\t%s\t%s\t%s\t%s\t%s\t\t%s\t%s\t%s\t%s\t%s" % (lang, rnd(total_acc), rnd(seenboth_acc), rnd(seenlemma_acc), rnd(seenfeats_acc), rnd(unseen_acc), num_predictions, num_seenboth, num_seenlemma_preds, num_seenfeats_preds, num_unseen_preds))
        except KeyError:
            print("ORIGINAL DATA FOR %s NOT FOUND. SKIPPING..." % lang)

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

    args = parser.parse_args()

    evaltype = args.evaltype.lower()
    if evaltype not in ("dev", "test"):
        exit("Eval type must be 'dev' or 'test'")

    lang_to_predfname = read_dir(args.preddir, evaltype, args.language)
    lang_to_trainfname = read_dir(args.datadir, "train", args.language)
    evaltype = evaltype if evaltype == "dev" else "gold"
    lang_to_evalfname = read_dir(args.datadir, evaltype, args.language.split("_")[0])
    evaluate_all(lang_to_predfname, lang_to_trainfname, lang_to_evalfname)