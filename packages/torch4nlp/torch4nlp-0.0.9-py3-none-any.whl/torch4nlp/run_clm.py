from argparse import ArgumentParserimport torch
from torch.utils.data import TensorDataset, DataLoader, RandomSampler
import transformers
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
from torch4nlp import read_jsonl, read_txt
import pdb
import os
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(filename)s - %(message)s')


indir='model_hub/'
plm_dir = os.path.join(indir, 'gpt2-xl')
# model_name="gpt2-cp"
# dump_checkpoint=f"{model_name}-20240109-history-textbook"


logging.info('transformers version: {}'.format(transformers.__version__))


def load_examples_from_files(file_list):
    examples = []
    for file_path in file_list:
        for x in read_txt(file_path):
            examples.append(x)
    return examples


def build_dataloader(file_list, tokenizer, batch_size, max_len=1024):
    examples = load_examples_from_files(file_list)
    logging.info('tokenizing train data...')
    
    block_size = 4096
    
    # batch encoding
    total_ids = []
    i = 0
    while i < len(examples):
        batch_examples = examples[i:i + block_size]
        for ids in tokenizer(batch_examples)['input_ids']:
            total_ids += ids
        i += block_size

    # group text
    input_ids = []
    i = 0
    while i + max_len <= len(total_ids):
        input_ids.append(total_ids[i: i + max_len])
        i += max_len
    
    # build dataloader
    dataset = TensorDataset(torch.LongTensor(input_ids))
    sampler = RandomSampler(dataset)
    return DataLoader(dataset, sampler=sampler, batch_size=batch_size)
    

def main():
    
    batch_size
    tokenizer = GPT2TokenizerFast.from_pretrained(plm_dir)
    model = GPT2LMHeadModel.from_pretrained(plm_dir).to('cuda')
    dataloader = build_dataloader([r'C:\Users\owen\Documents\Projects\torch4nlp\torch4nlp\中国通史.txt'], tokenizer, 3)
    for input_ids in dataloader:
        
    
    
if __name__ == '__main__':
    main()
    exit(0)
    ds = load_dataset(
        "text", 
        data_files={
            "train": '中国通史.txt',
            "validation": 'eval.txt'
        }
    )
    print('===> dataset loaded!')
    print('data sample:', ds["train"][10])


    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, use_fast=True)

    def tokenize_function(examples):
        return tokenizer(examples["text"])

    print('===> tokenizer built!')

    tokenized_datasets = ds.map(tokenize_function, batched=True, remove_columns=["text"])

    print('===> dataset tokenized!')
    print('sample:', tokenized_datasets["train"][1])

    block_size = 128
    def group_texts(examples):
        # Concatenate all texts.
        concatenated_examples = {k: sum(examples[k], []) for k in examples.keys()}
        total_length = len(concatenated_examples[list(examples.keys())[0]])
        # We drop the small remainder, we could add padding if the model supported it instead of this drop, you can
            # customize this part to your needs.
        total_length = (total_length // block_size) * block_size
        # Split by chunks of max_len.
        result = {
            k: [t[i : i + block_size] for i in range(0, total_length, block_size)]
            for k, t in concatenated_examples.items()
        }
        result["labels"] = result["input_ids"].copy()
        return result


    lm_datasets = tokenized_datasets.map(
        group_texts,
        batched=True,
        batch_size=1000,
        # num_proc=4,
    )

    print('===> text grouped!')
    print(tokenizer.decode(lm_datasets["train"][1]["input_ids"]))


    model = AutoModelForCausalLM.from_pretrained(model_checkpoint)
    # pdb.set_trace()


    from transformers import Trainer, TrainingArguments

    model_name = model_checkpoint.split("/")[-1]
    training_args = TrainingArguments(
        dump_checkpoint,
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        gradient_accumulation_steps=16,
        num_train_epochs=1.0,
        evaluation_strategy = "epoch",
        learning_rate=2e-5,
        weight_decay=0.01,
        push_to_hub=False,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=lm_datasets["train"],
        eval_dataset=lm_datasets["validation"],
    )

    trainer.train()

    import math
    eval_results = trainer.evaluate()
    print(f"Perplexity: {math.exp(eval_results['eval_loss']):.2f}")